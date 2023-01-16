#!/bin/sh
pip install .[test]
git config --local core.hooksPath .github/hooks
