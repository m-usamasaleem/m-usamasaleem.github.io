#!/bin/bash

# Set Git username and email globally
git config --global user.name "m-usamasaleem"
git config --global user.email "21100273@lums.edu.pk"

# Stage all changes
git add .

# Commit changes if there are any
if ! git diff-index --quiet HEAD --; then
    git commit -m "added"
    echo "Changes committed."
else
    echo "No changes to commit."
fi

# Ensure the remote 'origin' exists and is correctly set
if ! git remote | grep -q "^origin$"; then
    git remote add origin https://github.com/m-usamasaleem/m-usamasaleem.github.io.git
    echo "Remote 'origin' added."
else
    echo "Remote 'origin' already exists."
fi

# Determine the current branch
current_branch=$(git rev-parse --abbrev-ref HEAD)

# Ensure the branch is either 'main' or 'master'
if [ "$current_branch" != "main" ] && [ "$current_branch" != "master" ]; then
    echo "Error: Current branch is '$current_branch'. Please switch to 'main' or 'master'."
    exit 1
fi

# Push changes to the current branch and set upstream if not already set
git push --set-upstream origin "$current_branch"

# Confirm successful push
if [ $? -eq 0 ]; then
    echo "Changes pushed to 'origin/$current_branch' successfully."
else
    echo "Failed to push changes. Please check your Git configuration."
fi
