import sys
import numpy as np

from zflow.pyscf_helper import LAT
from zflow.pyscf_helper import BOHR
from zflow.io_helper import read_arg


if __name__ == '__main__':
    try:
        fxyz = read_arg(sys.argv[1], str)
        fout = read_arg(sys.argv[2], str)
    except:
        print('Usage: fxyz, fout')
        sys.exit(1)

    if fxyz.endswith('xyz'):
        lat = LAT().init_from_xyz(fxyz)
    else:
        raise RuntimeError

    atms = lat.atms
    rs = lat.rs / BOHR

    ''' format be like (note the unit is bohr)
    $coord
    0 0 0 H
    1.8897 0 0 H
    $end
    '''

    sout = ['$coord']
    for atm,r in zip(atms,rs):
        sout.append( f'{r[0]} {r[1]} {r[2]} {atm}' )
    sout.append( '$end' )
    sout = '\n'.join( sout )

    open(fout, 'w').write( sout+'\n' )
