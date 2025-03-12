from ase import Atoms
from ase.io import read, write
import numpy as np

#Created by Sohang. 
#This script is pretty random. It moves atoms around to make the adsorbate position symmetric in the unit cell

def move_atoms_around(input_path,output_path,x_threshold,x_window,y_threshold,y_window,x_shift,y_shift):
    '''
    This function moves atoms around inside the unit cell
    Reads:
        original geometry read from input_path
    Parameters: for x and y directions
        threshold: the neigborhood of atoms to be moved
        window: the tolerance around the neigborhood
        shift: with sign, the direction to be moved in. 
    Returns:
        updated geometry is written at output_path
    '''

    geometry = read(input_path)
    positions = geometry.get_positions()
    for i, pos in enumerate(positions):
        if x_threshold - x_window <= pos[0] <= x_threshold + x_window:
            positions[i, 0] += x_shift
        if y_threshold - y_window <= pos[1] <= y_threshold + y_window:
            positions[i, 1] += y_shift
    geometry.set_positions(positions)
    write(output_path,geometry)

#Parameters
x_threshold = 0. #the neighborhood of atoms to be moved along x
x_window = 0.5 #to check whether an atoms lies within the +/- window of threshold along x
y_threshold = 8.4 #the neighborhood of atoms to be moved along y
y_window = 0.5 #to check whether an atoms lies within the +/- window of threshold along x
x_shift = 10.13811 #the lattice parameter (BUT with sign) needed to repeat the atom on the other end of the unit cell.
y_shift = -10.13811 #the lattice parameter (BUT with sign) needed to repeat the atom on the other end of the unit cell.

#Reactant Geometry
input_path= 'R_Garvit_LiEC_6L.xyz' #path
output_path = 'Rcenter_Garvit_LiEC_6L.xyz' #path
move_atoms_around(input_path,output_path,x_threshold,x_window,y_threshold,y_window,x_shift,y_shift)
print(f"Moved atoms around in {input_path} to center EC. Output written to {output_path}.")

#TS Geometry
input_path= 'TS_Garvit_LiEC_6L.xyz' #path
output_path = 'TScenter_Garvit_LiEC_6L.xyz' #path
move_atoms_around(input_path,output_path,x_threshold,x_window,y_threshold,y_window,x_shift,y_shift)
print(f"Moved atoms around in {input_path} to center EC. Output written to {output_path}.")

#Isolated Li surface
input_path= 'Lisurf_Garvit_6L.xyz' #path
output_path = 'Lisurfcenter_Garvit_6L.xyz' #path
move_atoms_around(input_path,output_path,x_threshold,x_window,y_threshold,y_window,x_shift,y_shift)
print(f"Moved atoms around in {input_path} to center EC. Output written to {output_path}.")