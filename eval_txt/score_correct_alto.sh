#!/bin/bash
for f in /Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/eval_txt/doc/Cat_Courbet_1882/*.txt
do
	python3 /Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/eval_txt/score_and_correct_alto_comm_line.py $f
	echo "Processing $f"
done
