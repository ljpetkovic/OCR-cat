#!/bin/bash
for g in /Users/ljudmilapetkovic/Desktop/Katabase/ALTO_trans/*
do
        echo Processing $g
        for f in $g/*
        do
                python3 /Users/ljudmilapetkovic/Desktop/Katabase/alto_corr.py $f $g
                echo Processing $f
        done
done