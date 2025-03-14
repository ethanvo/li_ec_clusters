import sys
import numpy as np

from pyscf.lib import logger
from pyscf.data.nist import BOHR
from pyscf import gto


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
        atom = []
        for i in range(mol.natm):
            if i in idx:
                atm = "ghost-" + atms[i]
            else:
                atm = atms[i]
            atom.append((atm,rs[i]))
        with open(fout, 'w') as f:
            f.write('%d\n' % mol.natm)
            f.write('\n')
            for atm, r in atom:
                f.write(f'{atm} {r[0]} {r[1]} {r[2]}\n')
