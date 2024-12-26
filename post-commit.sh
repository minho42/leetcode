#!/bin/sh

# this script is called from ".git/hooks/post-commit" like so:
# "$(git rev-parse --show-toplevel)/post-commit.sh"

echo "post-commit"

GENERATE_README_SCRIPT="./generate_readme.py"

if [ -x "$GENERATE_README_SCRIPT" ]; then
    echo "generating readme"
    python3 "$GENERATE_README_SCRIPT"
    git add README.md
    git commit --amend --no-edit
else
    echo "error generating readme"
    exit 1
fi
