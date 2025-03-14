import sys
import numpy as np

from pyscf.lib import logger
from pyscf.data.nist import BOHR
from pyscf import gto

log = logger.Logger(sys.stdout, 6)


if __name__ == '__main__':
    try:
        Rxyz = sys.argv[1]
        TSxyz = sys.argv[2]
        mol_atmidx = np.asarray(list(map(int, sys.argv[3].split(',')))) if sys.argv[3].lower() != "none" else np.asarray([])
        center_atmidx = np.asarray(list(map(int, sys.argv[4].split(','))))
        Rout_path = sys.argv[5]
        TSout_path = sys.argv[6]
    except:
        log.warn('Usage: Rxyz, TS_xyz, mol_atmidx, center_atmidx, Rout_prefix, TSout_prefix')
        sys.exit(1)

    ratom = '\n'.join(open(rxyz, 'r').read().lstrip('\n').rstrip('\n').split('\n')[2:])
    rmol = gto.M(atom=ratom, basis='cc-pvdz', spin=None)

    tsatom = '\n'.join(open(tsxyz, 'r').read().lstrip('\n').rstrip('\n').split('\n')[2:])
    tsmol = gto.M(atom=tsatom, basis='cc-pvdz', spin=None)

    surf_atmidx = np.asarray([i for i in range(mol.natm) if i not in mol_atmidx])

    rs = mol.atom_coords() * BOHR
    atms = np.asarray([mol.atom_symbol(i) for i in range(mol.natm)])

    surf_rs = rs[surf_atmidx].reshape(-1,3)
    center_rs = rs[center_atmidx].reshape(-1,3).mean(axis=0)
    print(center_rs)
    dist = np.linalg.norm(surf_rs - center_rs, axis=-1)
    order = np.argsort(dist)
    print(order)
    for nsurf in np.arange(2,121,2):
        keep_atmidx = surf_atmidx[order[:nsurf]].copy()
        keep_atmidx = keep_atmidx[np.argsort(rs[keep_atmidx,2])]
        keep_atmidx = np.concatenate((keep_atmidx, mol_atmidx)).astype(int)

        # keep_atmidx = surf_atmidx[np.where(np.prod(dist <= rcut, axis=0))[0]].copy()
        # nsurf = keep_atmidx.size
        # keep_atmidx = keep_atmidx[np.argsort(rs[keep_atmidx,2])]
        # keep_atmidx = np.concatenate((keep_atmidx, mol_atmidx)).astype(int)

        keep_atom = [(atms[i],rs[i]) for i in keep_atmidx]

        # fout = f'{out_prefix}_{rcut:.1f}.xyz'
        fout = f'{out_path}/{nsurf}.xyz'
        with open(fout, 'w') as f:
            f.write(f'{len(keep_atom)}\n')
            f.write('\n')
            for atm, r in keep_atom:
                f.write(f'{atm} {r[0]} {r[1]} {r[2]}\n')
