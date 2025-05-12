from mace.calculators import mace_mp
from ase.constraints import FixAtoms, FixInternals, FixBondLengths
from ase import build
from ase import units
from ase import Atoms
from ase.cell import Cell
from ase.io import read, write
from ase.constraints import FixAtoms, FixInternals
from mace.calculators import MACECalculator
from ase.optimize import BFGS, FIRE
from ase.mep import NEB

macemp = MACECalculator(model_paths='/Users/sohangkundu/Documents/PostDocRepo/ML/periodic_data3/combdata/train2/checkpoints/MACE_run-10.model', device='cpu')
#macemp = MACECalculator(model_paths='/Users/sohangkundu/Documents/PostDocRepo/ML/periodic_data/k221/jumble/trunc/checkpoints/MACE_run-10.model', device='cpu')
#macemp = MACECalculator(model_paths='/Users/sohangkundu/Documents/PostDocRepo/ML/periodic_data/models/3300samples/fresh/jumble/checkpoints/MACE_run-10.model', device='cpu')
#macemp = MACECalculator(model_paths='/Users/sohangkundu/Documents/PostDocRepo/ML/periodic_try/checkpoints/MACE_run-10.model', device='cpu')
#macemp = MACECalculator(model_paths='/Users/sohangkundu/Documents/PostDocRepo/ML/periodic_data/k221/checkpoints/MACE_run-10.model', device='cpu')
#macemp = MACECalculator(model_paths='/Users/sohangkundu/Documents/PostDocRepo/ML/periodic_data/k221/jumble/checkpoints/MACE_run-10.model', device='cpu')
#macemp = MACECalculator(model_paths='/Users/sohangkundu/Documents/PostDocRepo/ML/periodic_data/k221/dataaug/jumble/filter/checkpoints/MACE_run-10.model', device='cpu')
#macemp = MACECalculator(model_paths='/Users/sohangkundu/Documents/PostDocRepo/ML/periodic_data/k221/checkpoints/MACE_run-10.model', device='cpu')
#macemp = MACECalculator(model_paths='/Users/sohangkundu/Documents/PostDocRepo/ML/periodic_data/k221/dataaug/checkpoints/MACE_run-10.model', device='cpu')
#macemp = MACECalculator(model_paths='/Users/sohangkundu/Documents/PostDocRepo/ML/periodic_data/models/3300samples/checkpoints/MACE_run-10.model', device='cpu')
#macemp = mace_mp(model="large",dispersion=True) # return a model with D3 dispersion correction


N1 = read('Rcenter_336_LiEC.xyz')
N1cell = Atoms(N1,cell=[[10.13811,0,0],[0,10.13811,0],[0,0,25.50125]],pbc=True)
N1cell.calc = macemp
refR = N1cell.get_potential_energy()
print("ref",refR)

N1 = read('TScenter_336_LiEC.xyz')
N1cell = Atoms(N1,cell=[[10.13811,0,0],[0,10.13811,0],[0,0,25.50125]],pbc=True)
N1cell.calc = macemp
refTS = N1cell.get_potential_energy()
print("ref",refTS)

print("diff",refTS-refR,(refTS-refR)*23.06)
