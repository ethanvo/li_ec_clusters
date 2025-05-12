from ase import Atoms
from ase.io import read, write
import numpy as np

unperturbed_lattice_path = 'Lisurf_Garvit_6L.xyz'
lattice_atoms = read(unperturbed_lattice_path)
lattice_positions = lattice_atoms.get_positions()

EC_Li_path = 'EC_with_extra_Li.xyz'
EC_Li_atoms = read(EC_Li_path)
EC_Li_positions = EC_Li_atoms.get_positions()
disp_vector = EC_Li_positions[0]-lattice_positions[45]
print(disp_vector)

EC_Li_positions = [i - disp_vector for i in EC_Li_positions]
print(len(EC_Li_positions))
# for i in len(EC_Li_positions):
#      += -1.*disp_vector
EC_Li_atoms.set_positions(EC_Li_positions)

combined_atoms = lattice_atoms + EC_Li_atoms[1:]

output_path = '/Users/sohangkundu/Documents/PostDocRepo/li_ec_clusters/adsorption/top/adsorption_top.xyz'
write(output_path,combined_atoms)

# print(disp_vector)
# print(EC_Li_positions[0])
# print(lattice_positions[45])
# # displacement = EC_Li_positions[0]

