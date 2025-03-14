#!/bin/bash


exe="../bsse.py"

out_path1="surf+ghostmol"
out_path2="ghostsurf+mol"
mkdir -p $out_path1
mkdir -p $out_path2

rm -f err stdout

for I in `seq 2 2 120`
do
	fxyz="surf+mol/$I.xyz"
	fout1="$out_path1/$I.xyz"	
	fout2="$out_path2/$I.xyz"

	natm=`head -n1 $fxyz`
	mol_idx=`seq $I 1 $natm | tr "\n" ","`

	echo $I >> stdout
	# echo $fxyz $mol_idx $fout1 $fout2
	# exit
	python3 $exe $fxyz $mol_idx $fout1 $fout2 2>> err >> stdout
done
