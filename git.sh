#!/bin/bash

# Stage all changes
git add .

# Commit with a default message
git commit -m "added"

# Check if the remote 'origin' already exists
if ! git remote | grep -q "^origin$"; then
    # Add the remote only if it doesn't exist
    git remote add origin https://github.com/m-usamasaleem/m-usamasaleem.github.io.git
fi

# Push changes to the remote repository and set upstream for the master branch
git push --set-upstream origin master
