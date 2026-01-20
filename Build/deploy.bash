# to work you must have the following structure of cloned repos
# GitHub Folder
    # sequence repo
        # Build
            # this script
    # kontinuafoundation.github.io repo 
# ------------------
cd ../../
# pwd

# copies files from a source to a destinationwhat are 
# overwrites files with the same name/path
# skips files that haven’t changed
# adds all new files
rsync -av sequence/Build/Resources-en_US/ kontinuafoundation.github.io/


# commit & push if there are changes

cd kontinuafoundation.github.io
if [ -n "$(git status --porcelain)" ]; then
  git add -A
  git commit -m "Deploy site: $(date -u +"%Y-%m-%d %H:%M:%SZ")"
  git push origin main
else
  echo "No changes to deploy."
fi
