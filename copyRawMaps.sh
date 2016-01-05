#!/bin/bash

if [ $# -lt 1 ]; then
	echo "ERROR: $0 requires full path to WoT installation directory as a first parameter"
elif [ $# -ge 1 ]; then
    # ignore hd resources as they do not contain the minimaps anyway
    GLOBIGNORE="*_hd.pkg"
	for file in "$1"res/packages/[0-9][0-9]{[0-9],}_*.pkg
	do
		BN=`basename "${file}" .pkg`
		unzip -j "$file" spaces/*/mmap.dds -d mapsRaw/"$BN"
	done

	while [ $# -gt 1 ]; do
		shift
		echo "WARNING: $0 discarded argument:" $1
	done
fi
