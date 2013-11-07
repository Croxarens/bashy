#!/bin/bash

# Python is required

[  -z "$1" ] && Port="56840" || Port=$1

echo "To end sharing, press Ctrl + C - server on port $Port"
python -m SimpleHTTPServer $Port
