#!/bin/bash

./clean.sh
python -m build
twine upload dist/*
