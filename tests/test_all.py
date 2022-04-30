"""
Ces tests sont juste là pour faire un coverage du code. Il ne vérifie pas la validité de celui-ci
"""

import pytest

@pytest.fixture
def cli():
  from amc.cli import main
  return main

@pytest.mark.parametrize('m', [
  'tm',
  '01',
  '01_n_times',
  'symb_LETTERS',
  'symb_letters',
  'symb_nums',
  'symb_signs',
  'interlace',
  'libstd',
  'libturing',
])
def test_pp(cli, m):
  with pytest.raises(SystemExit, match='0'):
    cli.main(['pp', f'./examples/{m}.amachine'])
  
@pytest.mark.parametrize('m', [
  'tm',
  '01',
  '01_n_times',
  'symb_LETTERS',
  'symb_letters',
  'symb_nums',
  'symb_signs',
  'interlace',
  'libstd',
  'libturing',
])
def test_ast(cli, m):
  with pytest.raises(SystemExit, match='0'):
    cli.main(['ast', f'./examples/{m}.amachine'])


@pytest.mark.parametrize('m', [
  'tm',
  '01',
  '01_n_times',
  'interlace',
])
def test_compile(cli, m):
  with pytest.raises(SystemExit, match='0'):
    cli.main(['compile-python', f'./examples/{m}.amachine'])
  
  
@pytest.mark.parametrize('m', [
  'tm',
  '01_n_times',
  'interlace',
])
def test_exec(cli, m):
  with pytest.raises(SystemExit, match='0'):
    cli.main(['exec', '-c', '25', f'./examples/{m}.amachine'])

