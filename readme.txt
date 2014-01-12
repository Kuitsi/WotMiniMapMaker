First time:
- remove FolderHolder.txt files
- set WoT installation path in makeMiniMaps.sh (Linux only)
- if needed, fresh icons can be extracted using SWFExtract from
  res/packages/gui.pkg/gui/scaleform/Minimap.swf

Usage (Windows):
- unpack all packages and put the maps into mapsRaw
- remove all .chunk .cdata files via del /S *.chunk from the mapsRaw directory
- run imgconverter.bat to convert all dds to png
- copy all arena_defs from res/scripts/arena_defs
- run fixdefnames.py to fix the arena_defs names
- run usexmlconverter.bat to convert all xml to readable
- run makemaps.py
- copy all maps to gridding in
- run gridding.py
- move all out to mapsFinal

Usage (Linux):
- execute makeMiniMaps.sh
- optionally execute renameJpg.sh

Requirements:
- Python 2.x
- Python libraries: beautifulsoup4, lxml, PIL
- mogrify (from ImageMagick)
- SWFExtract (part of SWFTools, http://www.swftools.org/)

Linux:
- Additional requirements:
  - unzip
  - mono
- Permissions to execute:
  - makeMiniMaps.sh
  - imgconverter.sh
  - copyRawMaps.sh
  - compressMaps.sh
  - renameJpg.sh
