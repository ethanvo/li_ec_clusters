from ase import Atoms
from ase.io import read, write
import numpy as np

#Created by Sohang. 
# This script takes a geometry from a periodic calculation, and filters layers by a z-coordinate threshold. 
# For the LiEC cells (6L): use >6 for 2L, use >3 for 4L, use >0 for 6L.
#Then it builds a bigger surface atom, 2 atoms in x and y, at a time. Shifts the cell to have all atoms in the 
#first quadrant and determines new lattice constants

def return_ref_coordinate(embed):
    positions = embed.positions
    min_x = np.min(positions[:, 0])
    min_y = np.min(positions[:, 1])
    min_z = np.min(positions[:, 2])
    return [min_x,min_y,min_z]


def create_layers(per_path,BCC_path,z_threshold,lattice_constants,output_hollow,output_embed,n,n_original):
    #input structure

    per_atoms = read(per_path)  
    filtered_geom = per_atoms[[atom.position[2] > z_threshold for atom in per_atoms]]
    #lattice BCC

    BCC_atoms = read(BCC_path)  
    filtered_BCC = BCC_atoms[[atom.position[2] > z_threshold for atom in BCC_atoms]]
    # Apply lattice and periodic boundary conditions (PBC)
    filtered_BCC.set_cell(lattice_constants)
    filtered_BCC.set_pbc(True)  # Set PBC in all directions
    cell = filtered_BCC.get_cell()
    supercell = Atoms(pbc=filtered_BCC.get_pbc())

    for ix in range(-n, n + 1):
        for iy in range(-n, n + 1):
            if abs(ix) <= n_original and abs(iy) <= n_original:
                continue  # Skip the original cell
            # Calculate the translation vector
            translation = ix * cell[0] + iy * cell[1]
    
            # Copy and shift the original cell
            translated_cell = filtered_BCC.copy()
            translated_positions = translated_cell.get_positions() + translation
            translated_cell.set_positions(translated_positions)
        
            # Add the translated cell to the supercell
            supercell += translated_cell
    

    #write(output_hollow, supercell)
    embed = supercell+filtered_geom
    reference= return_ref_coordinate(embed)
    embed.positions -= reference
    write(output_embed,embed)
    print(f"Embedded superlattices written to {output_hollow} and {output_embed}.")
    return embed


a = 3.37937000
vac = 17.000000

lattice_constants = [
    [a, 0.0,  0.0],  # a vector
    [0.0, a,  0.0],  # b vector
    [0.0, 0.0,8*a]   # c vector
]

#---------------------------332------------------------#

#Reactant
z_threshold = 6.0
per_path = 'Rcenter_Garvit_LiEC_6L.xyz'
BCC_path = 'BCCcenter_6L.xyz'
n = 2
n_original = 2
output_hollow = 'Lisurfcenter_332_hollow.xyz'
output_embed = 'Rcenter_332_LiEC.xyz'
embed = create_layers(per_path,BCC_path,z_threshold,lattice_constants,output_hollow,output_embed,n,n_original)

#TS
z_threshold = 6.0
per_path = 'TScenter_Garvit_LiEC_6L.xyz'
BCC_path = 'BCCcenter_6L.xyz'
n = 2
n_original = 2
output_hollow = 'Lisurfcenter_332_hollow.xyz'
output_embed = 'TScenter_332_LiEC.xyz'
embed = create_layers(per_path,BCC_path,z_threshold,lattice_constants,output_hollow,output_embed,n,n_original)

#Only surface
z_threshold = 6.0
per_path = 'Lisurfcenter_Garvit_6L.xyz'
BCC_path = 'BCCcenter_6L.xyz'
n = 1
n_original = 1
output_hollow = 'Lisurfcenter_332_hollow.xyz'
output_embed = 'LiECcenter_332.xyz'

#(super)lattice constants
embed = create_layers(per_path,BCC_path,z_threshold,lattice_constants,output_hollow,output_embed,n,n_original)
z_coords = [atom.position[2] for atom in embed]
zmax = max(z_coords)
print("DONE with 332")
print("Superlattice Vectors",(2*n+1)*a,(2*n+1)*a,zmax+vac)

#---------------------------552------------------------#

#Reactant
z_threshold = 6.0
per_path = 'Rcenter_Garvit_LiEC_6L.xyz'
BCC_path = 'BCCcenter_6L.xyz'
n = 2
n_original = 1
output_hollow = 'Lisurfcenter_552_hollow.xyz'
output_embed = 'Rcenter_552_LiEC.xyz'
embed = create_layers(per_path,BCC_path,z_threshold,lattice_constants,output_hollow,output_embed,n,n_original)
#TS
z_threshold = 6.0
per_path = 'TScenter_Garvit_LiEC_6L.xyz'
BCC_path = 'BCCcenter_6L.xyz'
n = 2
n_original = 1
output_hollow = 'Lisurfcenter_552_hollow.xyz'
output_embed = 'TScenter_552_LiEC.xyz'
embed = create_layers(per_path,BCC_path,z_threshold,lattice_constants,output_hollow,output_embed,n,n_original)
#Only surface
z_threshold = 6.0
per_path = 'Lisurfcenter_Garvit_6L.xyz'
BCC_path = 'BCCcenter_6L.xyz'
n = 2
n_original = 1
output_hollow = 'Lisurfcenter_552_hollow.xyz'
output_embed = 'LiECcenter_552.xyz'
embed = create_layers(per_path,BCC_path,z_threshold,lattice_constants,output_hollow,output_embed,n,n_original)
print("DONE with 552")
print("Superlattice Vectors",(2*n+1)*a,(2*n+1)*a,zmax+vac)

#---------------------------772------------------------#

#Reactant
z_threshold = 6.0
per_path = 'Rcenter_Garvit_LiEC_6L.xyz'
BCC_path = 'BCCcenter_6L.xyz'
n = 3
n_original = 1
output_hollow = 'Lisurfcenter_772_hollow.xyz'
output_embed = 'Rcenter_772_LiEC.xyz'
embed = create_layers(per_path,BCC_path,z_threshold,lattice_constants,output_hollow,output_embed,n,n_original)
#TS
z_threshold = 6.0
per_path = 'TScenter_Garvit_LiEC_6L.xyz'
BCC_path = 'BCCcenter_6L.xyz'
n = 3
n_original = 1
output_hollow = 'Lisurfcenter_772_hollow.xyz'
output_embed = 'TScenter_772_LiEC.xyz'
embed = create_layers(per_path,BCC_path,z_threshold,lattice_constants,output_hollow,output_embed,n,n_original)
#Only surface
z_threshold = 6.0
per_path = 'Lisurfcenter_Garvit_6L.xyz'
BCC_path = 'BCCcenter_6L.xyz'
n = 3
n_original = 1
output_hollow = 'Lisurfcenter_772_hollow.xyz'
output_embed = 'LiECcenter_772.xyz'
embed = create_layers(per_path,BCC_path,z_threshold,lattice_constants,output_hollow,output_embed,n,n_original)
print("DONE with 772")
print("Superlattice Vectors",(2*n+1)*a,(2*n+1)*a,zmax+vac)
