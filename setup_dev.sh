#!/bin/sh
pip install .[tests]
git config --local core.hooksPath .github/hooks
