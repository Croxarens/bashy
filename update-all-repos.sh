#!/bin/env bash

# Bulk update of all the GIT repos

# Place the script where there are all the folder with a GIT repo
# Then run the script for updating each single repo.

for b in $(ls -F ./ | grep /); do
    GIT=$(whereis -b git | awk '{print $2}')
    REPO=$(pwd)
    $(cd "$REPO/$b" && $GIT pull origin master > /dev/null)
    echo ''
done

exit 0
