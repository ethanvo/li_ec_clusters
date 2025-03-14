#!/bin/bash


geom_path0="../.."


# for ptype in surf+mol surf+ghostmol ghostsurf+mol
for ptype in surf+nomol nosurf+mol
do
	geom_path="$geom_path0/$ptype"
	coord_path="$ptype"
	mkdir -p $coord_path
	for mol in `ls $geom_path/*.xyz | awk -F "/" '{print $NF}' | sed "s:.xyz::g"`
	do
		fxyz="$geom_path/$mol.xyz"
		fcoord="$coord_path/$mol.coord"

		python prep_inp.py $fxyz $falat $fcoord
	done
done

