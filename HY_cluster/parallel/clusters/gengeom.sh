#!/bin/bash


exe="../carving.py"

prefix="surf+mol"
mol_idx="505,506,507,508,509,510,511,512,513,514"
center_idx="227,281"
rcut="1,2,3,4,5,6,7,8,9,10"
fxyz="../superlattice/${prefix}.xyz"

out_path="$prefix"
mkdir -p $out_path

python $exe $fxyz $mol_idx $center_idx $rcut $out_path 2> err > stdout

exit


prefix="surf"
mol_idx="none"
center_idx="227,281"
rcut="1,2,3,4,5,6,7,8,9,10"
fxyz="../superlattice/${prefix}.xyz"

out_path="$prefix"
mkdir -p $out_path

python $exe $fxyz $mol_idx $center_idx $rcut $out_path 2> err > stdout
