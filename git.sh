#!/bin/bash

# Stage all changes (including new files)
git add .

# Check if there are changes to commit
if ! git diff-index --quiet HEAD --; then
    # Commit changes if any
    git commit -m "added"
else
    echo "No changes to commit."
fi

# Check if the remote 'origin' exists
if ! git remote | grep -q "^origin$"; then
    git remote add origin https://github.com/m-usamasaleem/m-usamasaleem.github.io.git
fi

# Push changes to the remote repository
git push --set-upstream origin main
