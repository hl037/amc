# Introduction

AMC est un transpileur machine de Turing -> Python.
Il y a plusieurs niveaux de représentation intermédiaire. La machine de Turing étant un modèle assez simple, mais dont le nombre d'état peut vite grandir avec les m-fonctions.

# Installation

À la racine du projet, faire :
```
pip install --user -e .
```

# Ligne de commande

Si le module a été installé par pip et que les points d'entrée setuptools sont supportés, alors un exécutable `amc` a été créé. Sinon, il faudra remplacer `amc` par `python -m amc.cli`.

------

`amc ast <machine>`
Affiche l'AST généré au parsing de cette machine

------

`amc pp <machine`
Appelle le pretty printer qui regénère la même machine.

------

`amc exec [-f|-s|-i|-c] <ruban> <machine>`
Permet d'interpréter la machine avec le ruban donné en argument (voir `amc exec --help`).

Exemple : 
`amc exec -g -a -t --halt-action -k -c '25' ./examples/01_n_times.amachine`
Permet d'exécuter la machine `01_n_times.amachine` qui affiche une alternance de 0 et de 1 n fois, où n est un nombre à 2 chiffre (préfixé par 0 si inférieur à 10) qui se situe initialement sur le ruban. L'option `-c` permet de spécifier le ruban comme une suite de caractères (une lettre par case).

------

`amc compile-python <machine>`
Écrit sur l'entrée standard un script python qui permettra d'exécuter la machine directement. Le module `amc` est reste malgré tout une dépendance runtime, et doit donc être installé là où la machine de turing est exécutée.

exemple : 

```
amc compile-python 01_n_times.amachine > 01_n_times.py
python 01_n_times.py -c 25
```

# Test / coverage

Pour les tests, `pytest` est nécessaire. Pour le coverage, `coverage` et `pytest-cov` sont nécessaires.

Les tests ne testent pas la validité des machines ou de la compilation, mais permette d'exécuter le modules et d'emprunter la plupart des chemins d'exécution.

Pour le coverage faire : 
```
pytest --cov=amc --cov-report=html:_me_coverage .
```
...À la racine du projet après l'avoir installé

# Syntaxe amachine

Il y a 5 type de blocs.
Un bloc commence par une ligne sans espaces au début, et se poursuit sur toutes les lignes suivantes non-vides comportant au moins un espace au début.

Les lignes ne comportant que des espaces sont ignorées.

## Commentaires
Un commentaire commence par `#)` et s'étend jusqu'à la fin de la ligne. Le choix de ces deux symboles est motivé par le fait que `#` est utilisé dans beaucoup de langages. Néanmoins, une grande liberté a été laissé sur les symboles de bandes autorisé et `#` en particulier est un symbole de bande valide. Cependant, les parenthèses, elles, ne sont autorisée qu'en étant échapées. Le choix s'est ensuite tourné vers `)` plutôt que `(` pour des raisons esthétiques.

## Symbols

Un symbole est n'importe quelle chaîne de caractère ne commençant ni par une majuscule, ni par `_` s'il comporte plusieurs caractères (un seul `_` est autorisé), et ne comportant pas d'espace. Les caracrères `\\`, `(` et `)` doivent être échapés par un `\\`.

## Nom d'État

Un nom d'état (et de m-fonction) doit impérativement commencer par une lettre en majuscule (`[A-Z]`). Les autres caractères peuvent être n'importe lesquels hormis les espaces, les parenthèses, `:`, `,` et la suite de caractère `#(` qui démarre un commentaire 

## `include`

Permet d'inclure un autre fichier à du chemin du fichier courant.

Sa syntaxe ne comporte qu'une ligne:
```
include(chemin/vers/fichiers/sans/guillemets.amachine)
```

Chaque fichier ne peut être inclus qu'une seule fois, ce qui élimine la possibilité d'une récursivité infinie.

## `symbols`

Déclare des symboles de bande.
Les symboles apparaissant directement dans les règles sont automatiquement ajoutés à la liste des symboles de bandes.
Cette directive permet de rajouter des symboles n'apparaissant pas directement, et qui pourront être utilisés dans les règles génériques.

```
symbols
  0
  1
  etc.
```

Un symbole peut contenir à peu près n'importe quel caractère qui n'est pas un espace. Seuls les caractères suivant doivent être échappés par un `\` : `\`, `(`, `)`, `,`.

Le symbole "Vide" peut être désigné par : `\0`. Un symbole peut commencer par une majuscule si celle-ci est échapée par `\`. (`\Symbol` est un symbole valide).

## `init`

Déclare l'état initial.
Si plusieurs `init` sont présents, le dernier (en considérant les includes) est celui qui sera utilisé.

```
init
  RefEtatInitial
```

`RefEtatInitial` peut soit être un nom d'état, soit l'instanciation d'une m-fonction.

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
```
nomSymbole actions RefEtatFinal
```

Quand le symbole `nomSymbole` correspond à ce qui est sur la bande à la position de la tête de lecture, `actions` sont exécutées, et la machine passe à l'état `RefEtatFinal`.

`nomSymbole` est soit un symbole de bande, soit un nom de symbole générique (commence par `_` puis suit les même règle de nom que les symboles). Auquel cas, pour chaque symbole n'apparaissant pas en tête d'une règle de cet état, une nouvelle règle est ajoutée en remplaçant le symbole générique par le symbole manquant.

`nomSymbole` peut aussi être `...` s'il n'y a pas besoin de capturer le symbole sous la tête de lecture.

Si deux règle ont le même symbole de tête, la dernière est celle utilisée.

Les `actions` possibles sont une liste (séparée par un ou des espaces, mais sans nouvelle ligne, et qui peut être vide) parmi ces possibilités:

- `->` Déplacement de la tête de lecture vers la droite
- `<-` Déplacement de la tête de lecture vers la gauche
- `P:nomSymbole` Écrire `nomSymbole` sur la bande à l'emplacement de la tête de lecture après exécution des actions précédentes

`RefEtatFinal` est soit le nom d'un état, soit l'instanciation d'une m-fonction (voir section suivante)

## M-fonction
Une m-fonction correspond exactement à ce que Turing appelait ainsi. C'est un template d'état prenant en paramètre d'autres état et des symboles. À chaque instanciation d'une m-fonction avec une combinaison d'arguments pas encore rencontrée, un état est ajouté à la machine en remplaçant chaque occurrence d'un nom d'argument par sa valeur lors de l'instanciation. Les prochaines instanciations avec les mêmes arguments réfèreront cet état. (Note : pour l'interpréteur python, les états correspondants aux instances de m-fonction sont créés à la volée, et ne sont donc pas réutilisés)

Les arguments doivent commencer par `_` et ensuite respecter les règle de nommage des états et des symboles.

```
M-fonction1(_ArgEtat1, _argSymbol1, _ArgEtat2)
  règle1
  règle2
  etc.
```

Les règles reprennent la syntaxe de la section précédente. Si `_argSymbol1` apparait en tête de règle, une seule règle sera ajoutée en reprenant sa valeur lors de l'instanciation.

## État Builtin

Les états builtin `STOP(ACCEPT)` et `STOP(REJECT)` permettent d'arrêter la machine en acceptant ou en rejetant l'entrée. Ils ne sont pas à déclarer

# Comportement

La machine s'arrête en rejettant le mot si elle n'a pas de règle pour le symbole sous la tête de lecture.

Le ruban est bi-infini (de nouvelles cases sont créées à la volée

