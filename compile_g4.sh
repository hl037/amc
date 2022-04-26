#!/bin/bash

antlr4 -Dlanguage=Python3 -o amc/parsing -visitor -no-listener amachine.g4
