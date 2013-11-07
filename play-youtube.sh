#!/bin/bash

LinkVideo=$1
#YoutubeOpt=$2	# Default: -f 18
[  -z "$2" ] && YoutubeOpt="-f 18" || YoutubeOpt=$2

mplayer -cookies -cookies-file /tmp/ytcookie.txt $(youtube-dl $YoutubeOpt -g --cookies /tmp/ytcookie.txt "$LinkVideo")
