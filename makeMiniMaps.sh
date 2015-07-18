#!/bin/bash

# WoT installation directory, may contain spaces
WOT="/path/to/World of Tanks/"

# remove old files
rm -rf ./mapsRaw/*
rm -rf ./arena_defs/*
rm -rf ./arena_defs_decoded/*
rm -rf ./gridding/in/*
rm -rf ./gridding/out/*

./copyRawMaps.sh "$WOT"

./imgconverter.sh

cp -v "$WOT"res/scripts/arena_defs/* ./arena_defs/
rm -vrf ./arena_defs/_common_.xml
rm -vrf ./arena_defs/_default_.xml
rm -vrf ./arena_defs/_list_.xml
rm -vrf ./arena_defs/00_tank_tutorial.xml
rm -vrf ./arena_defs/59_asia_great_wall.xml # this is exclusively on china's servers
rm -vrf ./arena_defs/109_battlecity_ny.xml # special 8-bit map
rm -vrf ./arena_defs/_deathtrack_10.xml
rm -vrf ./arena_defs/hangar_*.xml
rm -vrf ./arena_defs/h01_bday_2015.xml

python ./fixdefnames.py

mono xmlconverter.exe arena_defs/ arena_defs_decoded/

python ./makemaps.py

python ./gridding/gridder.py

./compressMaps.sh
