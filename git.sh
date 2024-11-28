#!/bin/bash

# Ensure the main branch exists and switch to it
if git rev-parse --verify main >/dev/null 2>&1; then
    echo "Switching to the 'main' branch."
    git checkout main
else
    echo "Creating and switching to the 'main' branch."
    git checkout -b main origin/main
fi

# Stage all changes
echo "Staging changes."
git add .

# Commit changes
echo "Committing changes."
git commit -m "Updated site content"

# Push changes to the main branch
echo "Pushing changes to 'origin/main'."
git push origin main
