#!/bin/bash


exe="../carving.py"

prefix="surf+mol"
mol_idx="54,55,56,57,58,59,60,61,62,63"
center_idx="45"
rcut="1,2,3,4,5,6,7,8,9,10"
fxyz="../superlattice/${prefix}.xyz"

out_path="$prefix"
mkdir -p $out_path

python3 $exe $fxyz $mol_idx $center_idx $rcut $out_path 2> err > stdout


prefix="surf"
mol_idx="none"
center_idx="297"
rcut="1,2,3,4,5,6,7,8,9,10"
fxyz="../superlattice/${prefix}.xyz"

out_path="$prefix"
mkdir -p $out_path

python3 $exe $fxyz $mol_idx $center_idx $rcut $out_path 2> err > stdout
