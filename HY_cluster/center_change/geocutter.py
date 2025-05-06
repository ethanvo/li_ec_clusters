#!/usr/env python3
import numpy as np

def load_xyz_to_array(filename):
    """
    Load an XYZ file and convert the geometry to an n x 3 NumPy array.

    Parameters:
        filename (str): Path to the XYZ file.

    Returns:
        np.ndarray: An n x 3 array of atomic coordinates.
    """
    coordinates = []

    with open(filename, 'r') as file:
        lines = file.readlines()
        
        # Skip the first two lines (number of atoms and comment)
        for line in lines[2:]:
            parts = line.split()
            
            # Ensure the line contains valid data (element + 3 coordinates)
            if len(parts) >= 4:
                x, y, z = map(float, parts[1:4])
                coordinates.append([x, y, z])
    
    return np.array(coordinates)

def load_xyz_to_array_watom(filename):
    """
    Load an XYZ file and convert the geometry to an n x 4 NumPy array.

    Parameters:
        filename (str): Path to the XYZ file.

    Returns:
        list
    """
    coordinates = []

    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines[2:]:
            parts = line.split()
            if len(parts) >= 4:
                atom, (x, y, z) = parts[0], map(float, parts[1:4])
                coordinates.append((atom, x, y, z))

    return coordinates

# Example usage
if __name__ == "__main__":
    # Replace 'example.xyz' with your XYZ file path
    Rxyz_file = 'Rlattice_496.xyz'
    TSxyz_file = 'TSlattice_496.xyz'
    Rmole_file = 'Rmolecule.xyz'
    TSmole_file = 'TSmolecule.xyz'
    Rgeometry = load_xyz_to_array(Rxyz_file)
    TSgeometry = load_xyz_to_array(TSxyz_file)
    Rmole_geometry = load_xyz_to_array_watom(Rmole_file)
    TSmole_geometry = load_xyz_to_array_watom(TSmole_file)

    x_min, x_max = 1.4, 17.1
    y_min, y_max = -7.0, 8.7
    z_min = 3.0

    condition = (
            (Rgeometry[:, 0] >= x_min) & (Rgeometry[:, 0] <= x_max) &
            (Rgeometry[:, 1] >= y_min) & (Rgeometry[:, 1] <= y_max) &
            (Rgeometry[:, 2] >= z_min)
    )
    filtered_indices = np.where(condition)[0]
    filtered_Rgeometry = Rgeometry[filtered_indices]
    print("\nFiltered geometry:")
    print(filtered_Rgeometry)
    print(filtered_Rgeometry.shape)
    print("\nFiltered R geometry:")
    for i in range(len(Rmole_geometry)):
        print(f"{Rmole_geometry[i][0]}\t{Rmole_geometry[i][1]:14.8f}\t{Rmole_geometry[i][2]:14.8f}\t{Rmole_geometry[i][3]:14.8f}")
    for i in range(filtered_Rgeometry.shape[0]):
        print(f"Li\t{filtered_Rgeometry[i, 0]:14.8f}\t{filtered_Rgeometry[i, 1]:14.8f}\t{filtered_Rgeometry[i, 2]:14.8f}")

    with open('Rcombined_554.xyz', 'w') as file:
        file.write(f"{10 + filtered_Rgeometry.shape[0]}\n")
        file.write("\n")
        for i in range(len(Rmole_geometry)):
            file.write(f"{Rmole_geometry[i][0]}\t{Rmole_geometry[i][1]:14.8f}\t{Rmole_geometry[i][2]:14.8f}\t{Rmole_geometry[i][3]:14.8f}\n")
        for i in range(filtered_Rgeometry.shape[0]):
            file.write(f"Li\t{filtered_Rgeometry[i, 0]:14.8f}\t{filtered_Rgeometry[i, 1]:14.8f}\t{filtered_Rgeometry[i, 2]:14.8f}\n")

    print("\nFiltered TS geometry:")
    filtered_TSgeometry = TSgeometry[filtered_indices]
    for i in range(len(TSmole_geometry)):
        print(f"{TSmole_geometry[i][0]}\t{TSmole_geometry[i][1]:14.8f}\t{TSmole_geometry[i][2]:14.8f}\t{TSmole_geometry[i][3]:14.8f}")
    for i in range(filtered_TSgeometry.shape[0]):
        print(f"Li\t{filtered_TSgeometry[i, 0]:14.8f}\t{filtered_TSgeometry[i, 1]:14.8f}\t{filtered_TSgeometry[i, 2]:14.8f}")

    with open('TScombined_554.xyz', 'w') as file:
        file.write(f"{10 + filtered_TSgeometry.shape[0]}\n")
        file.write("\n")
        for i in range(len(TSmole_geometry)):
            file.write(f"{TSmole_geometry[i][0]}\t{TSmole_geometry[i][1]:14.8f}\t{TSmole_geometry[i][2]:14.8f}\t{TSmole_geometry[i][3]:14.8f}\n")
        for i in range(filtered_TSgeometry.shape[0]):
            file.write(f"Li\t{filtered_TSgeometry[i, 0]:14.8f}\t{filtered_TSgeometry[i, 1]:14.8f}\t{filtered_TSgeometry[i, 2]:14.8f}\n")
    """
    geometries = []
    for z in range(3, 8):
        for x in range(3, 8):
            for y in range(3, 8):
                test = x * y * z
                if test % 2 == 0 and test > 50 and test < 100:
                    geometries.append((x, y, z, test))
    geometries.sort(key=lambda x: x[3])
    print(geometries)
    """
