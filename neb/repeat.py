from ase import Atoms
from ase.io import read, write
import numpy as np

# Parameters
n = 1  # Number of repetitions in each direction (+/-x, +/-y)
input_file = 'Li333.xyz'  # Replace with your input file
output_file = 'Li333_repeated_3times.xyz'  # Output file after processing

# Read the initial structure
original_cell = read(input_file)
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
new_cell[0] *= (2 * n + 1)  # Scale x-direction
new_cell[1] *= (2 * n + 1)  # Scale y-direction
supercell.set_cell(new_cell, scale_atoms=False)

# Save the final structure to a file
write(output_file, supercell)

print(f"Supercell repeated {2*n+1}x{2*n+1}x1 with updated cell dimensions. Output written to {output_file}.")
