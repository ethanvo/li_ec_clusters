import sys
import numpy as np

from pyscf.lib import logger
from pyscf.data.nist import BOHR
from pyscf import gto

from zflow.pyscf_helper import LAT
from zflow.io_helper import mkdir


if __name__ == '__main__':
    try:
        fxyz = sys.argv[1]
        mol_atmidx = np.asarray(list(map(int, sys.argv[2].lstrip(',').rstrip(',').split(','))))
        fout1 = sys.argv[3]
        fout2 = sys.argv[4]
    except:
        print('Usage: fxyz, mol_atmidx, fout1, fout2')
        sys.exit(1)

    atom = '\n'.join(open(fxyz, 'r').read().lstrip('\n').rstrip('\n').split('\n')[2:])
    mol = gto.M(atom=atom, basis='cc-pvdz', spin=None)

    surf_atmidx = np.asarray([i for i in range(mol.natm) if i not in mol_atmidx])

    rs = mol.atom_coords() * BOHR
    atms = np.asarray([mol.atom_symbol(i) for i in range(mol.natm)])

    for fout,idx in zip([fout1,fout2],[mol_atmidx, surf_atmidx]):
        atom = [(atms[i],rs[i]) for i in idx]
        lat = LAT().init_from_pyscf_atom(atom)
        lat.dump_xyz(fout=fout)
