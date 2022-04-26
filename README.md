# Introduction

AMC est un transpileur machine de Turing -> Python.
Il y a plusieurs niveau de représentation intermédiaire. La machine de Turing étant un modèle assez simple, mais dont le nombre d'état peut vite grandir avec les m-fonctions.

# Syntaxe amachine

Il y a 5 type de blocs.
Un bloc commence par une ligne sans espaces au début, et se poursuit sur toutes les lignes suivantes non-vides comportant au moins un espace au début.

Les lignes ne comportant que des espaces sont ignorées.

## Commentaires
Un commentaire commance par `#)` et s'étend jusqu'à la fin de la ligne. Le choix de ces deux symboles est motivé par le fait que `#` est utilisé dans beaucoup de langages. Néanmoins, une grande liberté a été laissé sur les symboles de bandes autorisé et `#` en particulier est un symbole de bande valide. Cependant, les parenthèses, elles, ne sont autorisée qu'en étant échapée. Le choix s'est ensuite tourné vers `)` plutôt que `(` pour des raisons esthétiques.

## Symbols

Un symbol est n'importe quel chaine de caractère ne commençant ni par une majuscule, ni par `_` s'il comporte plusieurs caractères (un seul `_` est autorisé), et ne comportant pas d'espace. Les caracrère `\\`, `(` et `)` doivent être échapés par un `\\`.

## Nom d'État

Un nom d'état (et de m-fonction) doit impérativement commencé par une lettre en majuscule (`[A-Z]`). Les autres caractères peuvent être n'importe lesquels ormis les espaces, les parenthèse, `:`, `,` et la suite de caractère `#(` qui démarre un commentaire 

## `include`

Permet d'inclure un autre fichier à du chemin du fichier courant.

Sa syntaxe ne comporte qu'une ligne:
```
include(chemin/vers/fichiers/sans/guillemets.amachine)
```

Chaque fichier ne peut être inclu qu'une seule fois, ce qui élimine la possibilité d'une récursivité infinie.

## `symbols`

Déclare des ymbols de bande.
Les symbols apparaissant directement dans les règles sont automatiquement ajoutés à la liste des symbols de bandes.
Cette directive permet de rajouter des symbols n'apparaissant pas directement, et qui pourront être utilisés dans les règles génériques.

```
symbols
  0
  1
  etc.
```


## `init`

Déclare l'état initial.
Si plusieurs init sont présents, le dernier (en considérant les includes) est celui qui sera utilisé.

```
init
  RefEtatInitial
```

`RefEtatInitial` peut être l'instanciation d'une m-fonction.

## État

Un état est déclaré comme suit:

```
NomEtat
  règle1
  règle2
  etc.
```

`NomEtat` doit commencer par une majuscule comme expliqué à la section "Nom d'État".
Une règle suit cette syntaxe:
`nomSymbole actions RefEtatFinal`
Quand le symbole `nomSymbole` correspond à ce qui est sur la bande à la position de la tête de lecture, `actions` sont exécutées, et la machnie passe à l'état `RefEtatFinal`.

`nomSymbole` est soit un symbole de bande, soit un nom de symbol générique (commence par `_` puis suit les même règle de nom que les symbole). Auquel cas, pour chaque symbole n'apparaissant pas en tête d'une règle de cet état, une nouvelle règle est ajoutée en remplaçant le symbole générique par le symbole manquant.

`nomSymbole` peut aussi être `...` s'il n'y a pas besoin de capturer le symbole sous la tête de lecture.

Une erreur est émise si deux règles ont le même symbole en tête.

Les `actions` possibles sont une liste (séparaée par un ou des espaces, mais sans nouvelle ligne, et qui peut être vide) parmis ces possibilités:

- `->` Déplacement de la tête de lecture vers la droite
- `<-` Déplacement de la tête de lecture vers la gauche
- `P:nomSymbole` Écrire `nomSymbole` sur la bande à l'emplacement de la tête de lecture après exécution des action précédentes

`RefEtatFinal` est soit le nom d'un état, soit l'instanciation d'une m-fonction (voir section suivante)

## M-fonction
Une m-fonction correspond exactement à ce que Turing appelait ainsi. C'est un template d'état prenant en paramètre d'autres état et des symboles. À chaque instanciation d'une m-fonction avec une combinaison d'arguments pas encore rencontrée, un état est ajouté à la machine en remplaçant chaque occurence d'un nom d'argument par sa valeur lors de l'instenciation. Les prochaines instanciation avec les mêmes argument réfèreront cet état.

Les arguments doivent commencer par `_` et ensuite respecter les règle de nomage des état et des symboles.

```
M-fonction1(_ArgEtat1, _argSymbol1, _ArgEtat2)
  règle1
  règle2
  etc.
```

Les règles reprennent la syntaxe de la section précédentes. Si `_argSymbol1` apparait en tête de règle, une seule règle sera ajoutée en reprenant sa valeur lors de l'instanciation, émettant la même erreur que dans la section précédente si le symbole apparaît déjà dans l'état.



