#!/bin/bash

python3 SetGame.py
pdflatex SetGame.tex

rm SetGame.aux
rm SetGame.log
rm texput.log