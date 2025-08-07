#!/bin/bash

# Assumes the following directory structure:
# wfmeta
#  |
#  + aggregate (this repository)
#  + dask (dask capture repo)

PYTHONPATH=src python -m aggregate --drsh-ignore --dask-i ../dask/tests/example_output --verbose