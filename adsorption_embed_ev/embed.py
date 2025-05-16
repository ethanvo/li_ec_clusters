from ase import Atoms
from ase.io import read, write
import numpy as np

# Created by Sohang.
# This script takes a geometry of surface+adsorbate from a periodic calculation and embeds it into a superlattice by repeating
# the unperturbed surface in x and y dimensions. The code also allolws you set a zfilter to pick layers of the surface FROM THE TOP.
# For the LiEC cells: use >6 for 2L, and use >3 for 4L

# unperturbed lattice path
surface_path = "Lisurf_Garvit_6L.xyz"
surface_superlattice_path = "relaxed_superlattice.xyz"

surface_atoms = read(surface_path)
# Define lattice constants
lattice_constants = [
    [10.13811, 0.0, 0.0],  # a vector
    [0.0, 10.13811, 0.0],  # b vector
    [0.0, 0.0, 25.14250],  # c vector
]
# Apply lattice and periodic boundary conditions (PBC)
surface_atoms.set_cell(lattice_constants)
surface_atoms.set_pbc(True)  # Set PBC in all directions

n = 1  # Number of repetitions in each direction (+/-x, +/-y). Transformed lattice has 2n+1 unit cells in x and 2n+1 unit cells in y
# input_file = 'Li333.xyz'  # Replace with your input file
# output_file = 'Li333_repeated_3times.xyz'  # Output file after processing


original_cell = surface_atoms  # read(input_file)
cell = original_cell.get_cell()

# Create an empty Atoms object for the supercell
supercell = Atoms(pbc=original_cell.get_pbc())

# Repeat the cell in +x and -x, +y and -y
for ix in range(-n, n + 1):
    for iy in range(-n, n + 1):
        if ix == 0 and iy == 0:
            continue  # Skip the original cell
        # Calculate the translation vector
        translation = ix * cell[0] + iy * cell[1]

        # Copy and shift the original cell
        translated_cell = original_cell.copy()
        translated_positions = translated_cell.get_positions() + translation
        translated_cell.set_positions(translated_positions)

        # Add the translated cell to the supercell
        supercell += translated_cell

# Update the supercell's lattice dimensions
new_cell = cell.copy()
new_cell[0] *= 2 * n + 1  # Scale x-direction
new_cell[1] *= 2 * n + 1  # Scale y-direction
supercell.set_cell(new_cell, scale_atoms=False)

# Save the final structure to a file
write(surface_superlattice_path, supercell)

print(
    f"Supercell repeated {2*n+1}x{2*n+1}x1 with updated cell dimensions. Output written to {surface_superlattice_path}."
)
# Reactant
surface_adsorbate_path = "top_ads_opt.xyz"
embed_superlattice_path = "top_superlattice.xyz"

surface_adsorbate = read(surface_adsorbate_path)
embed_superlattice = surface_adsorbate + supercell
write(embed_superlattice_path, embed_superlattice)

print(f"Embedded superlattice written to {embed_superlattice_path}.")
'''
# Reactant
surface_adsorbate_path = "Rcenter_Garvit_LiEC_6L.xyz"
embed_superlattice_path = "Rcenter_embed_superlattice.xyz"

surface_adsorbate = read(surface_adsorbate_path)
embed_superlattice = surface_adsorbate + supercell
write(embed_superlattice_path, embed_superlattice)

print(f"Embedded superlattice written to {embed_superlattice_path}.")


# TS
surface_adsorbate_path = "TScenter_Garvit_LiEC_6L.xyz"
embed_superlattice_path = "TScenter_embed_superlattice.xyz"

surface_adsorbate = read(surface_adsorbate_path)
embed_superlattice = surface_adsorbate + supercell
write(embed_superlattice_path, embed_superlattice)

print(f"Embedded superlattice written to {embed_superlattice_path}.")

# Lisurf_embed
surface_adsorbate_path = "Lisurfcenter_Garvit_6L.xyz"
embed_superlattice_path = "Lisurfcenter_embed_superlattice.xyz"

surface_adsorbate = read(surface_adsorbate_path)
embed_superlattice = surface_adsorbate + supercell
write(embed_superlattice_path, embed_superlattice)

print(f"Embedded superlattice written to {embed_superlattice_path}.")
'''
