git branch -a  # Lists all branches
git checkout main  # Switch to the main branch
git checkout -b main origin/main
git add .
git commit -m "Updated site content"
git pull origin main --rebase
git push origin main
