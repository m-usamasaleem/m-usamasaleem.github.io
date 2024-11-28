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

# Switch to the 'main' branch
if [ "$(git rev-parse --abbrev-ref HEAD)" != "main" ]; then
    echo "Switching to 'main' branch."
    git checkout main 2>/dev/null || {
        echo "Branch 'main' does not exist locally. Creating and switching to 'main'."
        git checkout -b main
    }
fi

# Push changes to the 'main' branch and set upstream if needed
git push --set-upstream origin main

# Confirm successful push
if [ $? -eq 0 ]; then
    echo "Changes pushed to 'origin/main' successfully."
else
    echo "Failed to push changes. Please check your Git configuration."
fi
