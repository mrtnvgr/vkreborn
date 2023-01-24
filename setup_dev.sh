#!/bin/sh
poetry install --all-extras
git config --local core.hooksPath .github/hooks
