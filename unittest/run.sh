#!/bin/bash

# Get a list of all subdirectories under the current directory
subdirs=$(find . -type d)

# Loop through each subdirectory and run the unittest command
for dir in $subdirs; do
  # Check if the directory contains Python files
  if ls "$dir"/*.py &>/dev/null; then
    echo "Running tests in $dir..."
    (cd "$dir" && python3 -m unittest *.py)
    echo "Finished running tests in $dir"
    echo
  fi
done
