#!/bin/bash


exe="carving.py"

: '
Arguments
1. Rxyz
2. TSxyz
3. mol_idx
4. rcenter_idx
5. tscenter_idx
6. Rout_path
7. TSout_path
'
mol_idx="54,55,56,57,58,59,50,51,52,53"
center_idx="55,59"
rxyz="./superlattice/Rcenter_embed_superlattice.xyz"
tsxyz="./superlattice/TScenter_embed_superlattice.xyz"

rout_path="R/surf+mol"
mkdir -p $rout_path
tsout_path="TS/surf+mol"
mkdir -p $tsout_path

python3 $exe $rxyz $tsxyz $mol_idx $center_idx $rout_path $tsout_path 2> err > stdout

: '
prefix="surf"
mol_idx="none"
center_idx="297"
rcut="1,2,3,4,5,6,7,8,9,10"
fxyz="../superlattice/${prefix}.xyz"

out_path="$prefix"
mkdir -p $out_path

python3 $exe $fxyz $mol_idx $center_idx $rcut $out_path 2> err > stdout
'
