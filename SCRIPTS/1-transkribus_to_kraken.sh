#!/bin/bash
for fullpath  in data/*.html; do
    export filename=$(basename -- "$fullpath")
    export target_dir=extracted/${filename%%.*}
    mkdir $target_dir --parents
    /Users/ljudmilapetkovic/Desktop/OCRcat/env/bin/ketos extract --binarize --normalization NFD --normalize-whitespace --output extracted data/*html
done
