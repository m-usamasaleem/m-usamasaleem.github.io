#!/bin/bash

# Stage all changes
git add .

# Commit changes
if ! git diff-index --quiet HEAD --; then
    git commit -m "added"
else
    echo "No changes to commit."
fi

# Ensure the remote 'origin' exists
if ! git remote | grep -q "^origin$"; then
    git remote add origin https://github.com/m-usamasaleem/m-usamasaleem.github.io.git
fi

# Push to the current branch
current_branch=$(git rev-parse --abbrev-ref HEAD)
git push --set-upstream origin "$current_branch"
