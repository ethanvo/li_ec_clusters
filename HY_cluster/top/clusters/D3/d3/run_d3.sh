#!/bin/bash


exe="/Users/hzye/local/opt/miniconda/envs/frank/bin/s-dftd3"
xcs="pbe"
geom_path0="../coord"

out_path="out"
mkdir -p $out_path

OUT_PATH="data"
mkdir -p $OUT_PATH

xc="pbe"

FOUT="$OUT_PATH/eall"
rm -f $FOUT

for n in `seq 2 2 31`
do
	rm -f tmp
	# for ptype in surf+mol surf+ghostmol ghostsurf+mol
	for ptype in surf+mol surf+nomol nosurf+mol
    do
    	geom_path="$geom_path0/$ptype"
        fcoord="$geom_path/$n.coord"
        ferr="$out_path/${n}.err"
        fout="$out_path/${n}.stdout"
        $exe --zero $xc --atm $fcoord 2> $ferr > $fout
        e=`grep -a "^Disp" $fout | awk '{print $(NF-1)}'`
		echo $e >> tmp
	done
	es=`cat tmp | tr "\n" " "`
	echo $n $es >> $FOUT
done
