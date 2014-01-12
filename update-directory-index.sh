#!/bin/bash

if [ $# -lt 1 ]; then
    echo "ERROR: $0 requires WoT version number as a first parameter"
elif [ $# -ge 1 ]; then
  (
    echo -e "<html>\n<body>\n<h1>World of Tanks (version "$1") minimaps</h1>\n"
    echo -e "<p>Maps generated using <a href="https://github.com/Kuitsi/WotMiniMapMaker">WotMiniMapMaker</a>.<br />"
    echo -e "Team 1 = green, Team 2 = red.</p>\n<hr/>\n<pre>"
    ls -1pa ./maps | grep -v "^\./$" | grep -v "^\.\./$" | awk '{ printf "<a href=\"maps/%s\">%s</a>\n",$1,$1 }' 
    echo -e "</pre>\n</body>\n</html>"
  ) > index.html
fi
