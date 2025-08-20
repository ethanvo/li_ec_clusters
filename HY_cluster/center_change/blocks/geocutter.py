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

    with open(filename, "r") as file:
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

    with open(filename, "r") as file:
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
    Rxyz_file = "../superlattice/Rlattice_496.xyz"
    TSxyz_file = "../superlattice/TSlattice_496.xyz"
    Topxyz_file = "../superlattice/Toplattice_496.xyz"
    Rmole_file = "../superlattice/Rmolecule.xyz"
    TSmole_file = "../superlattice/TSmolecule.xyz"
    Topmole_file = "../superlattice/Topmolecule.xyz"
    Rgeometry = load_xyz_to_array(Rxyz_file)
    TSgeometry = load_xyz_to_array(TSxyz_file)
    Topgeometry = load_xyz_to_array(Topxyz_file)
    Rmole_geometry = load_xyz_to_array_watom(Rmole_file)
    TSmole_geometry = load_xyz_to_array_watom(TSmole_file)
    Topmole_geometry = load_xyz_to_array_watom(Topmole_file)

    x_min, x_max = -8.9, 20.7
    y_min, y_max = -12.3, 17.3
    z_min = -2.0

    coordinate_dicts = {
        "33": [1.2, 10.5, -2.0, 7.0, -2.0],
        "44": [1.2, 13.9, -2.0, 10.5, -2.0],
        "55": [-2.0, 13.9, -5.5, 10.5, -2.0],
        "66": [-2.0, 17.3, -5.5, 13.9, -2.0],
        "77": [-5.5, 17.3, -8.9, 13.9, -2.0],
        "88": [-5.5, 20.7, -8.9, 17.3, -2.0],
        "99": [-8.9, 20.7, -12.3, 17.3, -2.0],
    }

    top_coordinate_dicts = {
        "33": [-0.5, 8.9, -0.5, 8.9],
        "44": [-0.5, 12.3, -0.5, 12.3],
        "55": [-3.8, 12.3, -3.8, 12.3],
        "66": [-3.8, 15.7, -3.8, 15.7],
        "77": [-7.2, 15.7, -7.2, 15.7],
        "88": [-7.2, 19.1, -7.2, 19.1],
        "99": [-10.6, 19.1, -10.6, 19.1],
    }

    z_dict = {"2": 6.0, "4": 2.8, "6": -2.0}

    for xykey, xyval in coordinate_dicts.items():
        for zkey, zval in z_dict.items():
            key = xykey + zkey
            x_min, x_max, y_min, y_max = xyval[0], xyval[1], xyval[2], xyval[3]
            z_min = zval

            condition = (
                (Rgeometry[:, 0] >= x_min)
                & (Rgeometry[:, 0] <= x_max)
                & (Rgeometry[:, 1] >= y_min)
                & (Rgeometry[:, 1] <= y_max)
                & (Rgeometry[:, 2] >= z_min)
            )
            filtered_indices = np.where(condition)[0]
            filtered_Rgeometry = Rgeometry[filtered_indices]
            filtered_TSgeometry = TSgeometry[filtered_indices]
            # print("\nFiltered geometry:")
            # print(filtered_Rgeometry)
            # print(filtered_Rgeometry.shape)
            # print("\nFiltered R geometry:")
            # for i in range(len(Rmole_geometry)):
            #     print(
            #         f"{Rmole_geometry[i][0]}\t{Rmole_geometry[i][1]:14.8f}\t{Rmole_geometry[i][2]:14.8f}\t{Rmole_geometry[i][3]:14.8f}"
            #     )
            # for i in range(filtered_Rgeometry.shape[0]):
            #     print(
            #         f"Li\t{filtered_Rgeometry[i, 0]:14.8f}\t{filtered_Rgeometry[i, 1]:14.8f}\t{filtered_Rgeometry[i, 2]:14.8f}"
            #     )

            with open(f"R/Rcombined_{key}.xyz", "w") as file:
                file.write(f"{10 + filtered_Rgeometry.shape[0]}\n")
                file.write("\n")
                for i in range(len(Rmole_geometry)):
                    file.write(
                        f"{Rmole_geometry[i][0]}\t{Rmole_geometry[i][1]:14.8f}\t{Rmole_geometry[i][2]:14.8f}\t{Rmole_geometry[i][3]:14.8f}\n"
                    )
                for i in range(filtered_Rgeometry.shape[0]):
                    file.write(
                        f"Li\t{filtered_Rgeometry[i, 0]:14.8f}\t{filtered_Rgeometry[i, 1]:14.8f}\t{filtered_Rgeometry[i, 2]:14.8f}\n"
                    )

            # for i in range(len(TSmole_geometry)):
            #     print(
            #         f"{TSmole_geometry[i][0]}\t{TSmole_geometry[i][1]:14.8f}\t{TSmole_geometry[i][2]:14.8f}\t{TSmole_geometry[i][3]:14.8f}"
            #     )
            # for i in range(filtered_TSgeometry.shape[0]):
            #     print(
            #         f"Li\t{filtered_TSgeometry[i, 0]:14.8f}\t{filtered_TSgeometry[i, 1]:14.8f}\t{filtered_TSgeometry[i, 2]:14.8f}"
            #     )

            with open(f"TS/TScombined_{key}.xyz", "w") as file:
                file.write(f"{10 + filtered_TSgeometry.shape[0]}\n")
                file.write("\n")
                for i in range(len(TSmole_geometry)):
                    file.write(
                        f"{TSmole_geometry[i][0]}\t{TSmole_geometry[i][1]:14.8f}\t{TSmole_geometry[i][2]:14.8f}\t{TSmole_geometry[i][3]:14.8f}\n"
                    )
                for i in range(filtered_TSgeometry.shape[0]):
                    file.write(
                        f"Li\t{filtered_TSgeometry[i, 0]:14.8f}\t{filtered_TSgeometry[i, 1]:14.8f}\t{filtered_TSgeometry[i, 2]:14.8f}\n"
                    )

            with open(f"parallel/surf+mol/parallel_surf+mol_{key}.xyz", "w") as file:
                file.write(f"{10 + filtered_Rgeometry.shape[0]}\n")
                file.write("\n")
                for i in range(len(Rmole_geometry)):
                    file.write(
                        f"{Rmole_geometry[i][0]}\t{Rmole_geometry[i][1]:14.8f}\t{Rmole_geometry[i][2]:14.8f}\t{Rmole_geometry[i][3]:14.8f}\n"
                    )
                for i in range(filtered_Rgeometry.shape[0]):
                    file.write(
                        f"Li\t{filtered_Rgeometry[i, 0]:14.8f}\t{filtered_Rgeometry[i, 1]:14.8f}\t{filtered_Rgeometry[i, 2]:14.8f}\n"
                    )

            with open(
                f"parallel/surf+ghostmol/parallel_surf+ghostmol_{key}.xyz", "w"
            ) as file:
                file.write(f"{10 + filtered_Rgeometry.shape[0]}\n")
                file.write("\n")
                for i in range(len(Rmole_geometry)):
                    file.write(
                        f"ghost-{Rmole_geometry[i][0]}\t{Rmole_geometry[i][1]:14.8f}\t{Rmole_geometry[i][2]:14.8f}\t{Rmole_geometry[i][3]:14.8f}\n"
                    )
                for i in range(filtered_Rgeometry.shape[0]):
                    file.write(
                        f"Li\t{filtered_Rgeometry[i, 0]:14.8f}\t{filtered_Rgeometry[i, 1]:14.8f}\t{filtered_Rgeometry[i, 2]:14.8f}\n"
                    )

            with open(
                f"parallel/ghostsurf+mol/parallel_ghostsurf+mol_{key}.xyz", "w"
            ) as file:
                file.write(f"{10 + filtered_Rgeometry.shape[0]}\n")
                file.write("\n")
                for i in range(len(Rmole_geometry)):
                    file.write(
                        f"{Rmole_geometry[i][0]}\t{Rmole_geometry[i][1]:14.8f}\t{Rmole_geometry[i][2]:14.8f}\t{Rmole_geometry[i][3]:14.8f}\n"
                    )
                for i in range(filtered_Rgeometry.shape[0]):
                    file.write(
                        f"ghost-Li\t{filtered_Rgeometry[i, 0]:14.8f}\t{filtered_Rgeometry[i, 1]:14.8f}\t{filtered_Rgeometry[i, 2]:14.8f}\n"
                    )

    for xykey, xyval in top_coordinate_dicts.items():
        for zkey, zval in z_dict.items():
            key = xykey + zkey
            x_min, x_max, y_min, y_max = xyval[0], xyval[1], xyval[2], xyval[3]
            z_min = zval

            condition = (
                (Topgeometry[:, 0] >= x_min)
                & (Topgeometry[:, 0] <= x_max)
                & (Topgeometry[:, 1] >= y_min)
                & (Topgeometry[:, 1] <= y_max)
                & (Topgeometry[:, 2] >= z_min)
            )
            filtered_indices = np.where(condition)[0]
            filtered_Topgeometry = Topgeometry[filtered_indices]

            with open(f"top/surf+mol/top_surf+mol_{key}.xyz", "w") as file:
                file.write(f"{10 + filtered_Topgeometry.shape[0]}\n")
                file.write("\n")
                for i in range(len(Topmole_geometry)):
                    file.write(
                        f"{Topmole_geometry[i][0]}\t{Topmole_geometry[i][1]:14.8f}\t{Topmole_geometry[i][2]:14.8f}\t{Topmole_geometry[i][3]:14.8f}\n"
                    )
                for i in range(filtered_Topgeometry.shape[0]):
                    file.write(
                        f"Li\t{filtered_Topgeometry[i, 0]:14.8f}\t{filtered_Topgeometry[i, 1]:14.8f}\t{filtered_Topgeometry[i, 2]:14.8f}\n"
                    )

            with open(f"top/surf+ghostmol/top_surf+ghostmol_{key}.xyz", "w") as file:
                file.write(f"{10 + filtered_Topgeometry.shape[0]}\n")
                file.write("\n")
                for i in range(len(Topmole_geometry)):
                    file.write(
                        f"ghost-{Topmole_geometry[i][0]}\t{Topmole_geometry[i][1]:14.8f}\t{Topmole_geometry[i][2]:14.8f}\t{Topmole_geometry[i][3]:14.8f}\n"
                    )
                for i in range(filtered_Topgeometry.shape[0]):
                    file.write(
                        f"Li\t{filtered_Topgeometry[i, 0]:14.8f}\t{filtered_Topgeometry[i, 1]:14.8f}\t{filtered_Topgeometry[i, 2]:14.8f}\n"
                    )

            with open(f"top/ghostsurf+mol/top_ghostsurf+mol_{key}.xyz", "w") as file:
                file.write(f"{10 + filtered_Topgeometry.shape[0]}\n")
                file.write("\n")
                for i in range(len(Topmole_geometry)):
                    file.write(
                        f"{Topmole_geometry[i][0]}\t{Topmole_geometry[i][1]:14.8f}\t{Topmole_geometry[i][2]:14.8f}\t{Topmole_geometry[i][3]:14.8f}\n"
                    )
                for i in range(filtered_Topgeometry.shape[0]):
                    file.write(
                        f"ghost-Li\t{filtered_Topgeometry[i, 0]:14.8f}\t{filtered_Topgeometry[i, 1]:14.8f}\t{filtered_Topgeometry[i, 2]:14.8f}\n"
                    )
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
