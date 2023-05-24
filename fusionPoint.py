# -*- coding: UTF-8 -*-

import numpy as np
import os
import struct
from PyQt5.QtCore import QThread, pyqtSignal


# dx/dy/dz是position wx/wy/wx是orientation，x/y/z是点云坐标，m是尺度因子
def molodensky_transform(x, y, z, dx, dy, dz, wx, wy, wz, m):
    """
    Performs a Molodensky transformation on the input coordinates using the given transformation parameters.

    Args:
    x (float): The x coordinate.
    y (float): The y coordinate.
    z (float): The z coordinate.
    dx (float): The delta x transformation parameter.
    dy (float): The delta y transformation parameter.
    dz (float): The delta z transformation parameter.
    wx (float): The x rotation parameter in arc seconds.
    wy (float): The y rotation parameter in arc seconds.
    wz (float): The z rotation parameter in arc seconds.
    m (float): The scale factor in parts per million.

    Returns:
    tuple: A tuple containing the transformed x, y, and z coordinates.
    """
    # # Convert rotation parameters to arc seconds
    # wx = np.deg2rad(wx / 3600)
    # wy = np.deg2rad(wy / 3600)
    # wz = np.deg2rad(wz / 3600)

    # Convert scale factor to parts per million
    # m = (m * 10 ** -6) + 1

    # Apply the transformation
    x2 = dx + ((m) * ((1 * x) + (wz * y) + (-wy * z)))
    y2 = dy + ((m) * ((-wz * x) + (1 * y) + (wx * z)))
    z2 = dz + ((m) * ((wy * x) + (-wx * y) + (1 * z)))

    return x2, y2, z2


def molodensky_transform2(x, y, z, dx, dy, dz, wx, wy, wz, m):
    rwx = np.array(
        [[1, 0, 0], [0, np.cos(wx), np.sin(wx)], [
            0, -np.sin(wx), np.cos(wx)]]
    )
    rwy = np.array(
        [[np.cos(wy), 0, -np.sin(wy)], [0, 1, 0],
            [np.sin(wy), 0, np.cos(wy)]]
    )
    rwz = np.array(
        [[np.cos(wz), np.sin(wz), 0],
            [-np.sin(wz), np.cos(wz), 0], [0, 0, 1]]
    )

    rw = np.dot(rwz, np.dot(rwy, rwx))
    r = m * np.dot(rw, np.array([x, y, z]))
    x2 = dx + r[0]
    y2 = dy + r[1]
    z2 = dz + r[2]

    return x2, y2, z2


class FusionPoint(QThread):
    __pointPath = ""
    __positionPath = ""
    __method = 1
    msg_signal = pyqtSignal(str)

    def __init__(self, pointPath, positionPath, method, parent=None):
        """
        Initializes the FusionPoint object.

        :param pointPath: A string representing the path to the point file.
        :param positionPath: A string representing the path to the position file.
        :param method: A string representing the method.
        :param parent: An optional parent object. Defaults to None.
        """
        super().__init__()
        super(FusionPoint, self).__init__(parent)
        self.__pointPath = pointPath
        self.__positionPath = positionPath
        self.__method = method

    def read_odom_file(file_path):
        """
        Reads an odometry file from the specified path and returns the positional and rotational changes.

        :param file_path: A string representing the file path to read from.
        :return: A tuple containing the positional and rotational changes as floats in the following order: dx, dy, dz, wx, wy, wz, m.
        """
        with open(file_path, "r") as f:
            position = f.readline().split()
            dx = float(f.readline().split()[1])
            dy = float(f.readline().split()[1])
            dz = float(f.readline().split()[1])
            orientation = f.readline().split()
            wx = float(f.readline().split()[1])
            wy = float(f.readline().split()[1])
            wz = float(f.readline().split()[1])
            m = float(f.readline().split()[1])

        return dx, dy, dz, wx, wy, wz, m

    @staticmethod
    def write_ply_file(file_path, dx, dy, dz, wx, wy, wz, m, method=1):
        """
        Writes a new PLY (Polygon File Format) file with updated header and transformed vertices.

        :param file_path: str, the path to the input PLY file.
        :param dx: float, the X shift of the transformation.
        :param dy: float, the Y shift of the transformation.
        :param dz: float, the Z shift of the transformation.
        :param wx: float, the X rotation of the transformation.
        :param wy: float, the Y rotation of the transformation.
        :param wz: float, the Z rotation of the transformation.
        :param m: float, the scale factor of the transformation.
        :return: None
        """
        with open(file_path, "rb") as f:
            header = ""
            while True:
                line = f.readline().decode("ascii")
                header += line
                if line.strip() == "end_header":
                    break
                    # Modify the header
            header = header.replace(
                "format binary_little_endian 1.0", "format ascii 1.0")
            vertex_data = f.read()
            vertex_size = struct.calcsize("ffff")
            vertex_count = len(vertex_data) // vertex_size
            vertices = []
            for i in range(vertex_count):
                vertex = struct.unpack(
                    "ffff", vertex_data[i * vertex_size: (i + 1) * vertex_size]
                )
                vertices.append(vertex)
            bak_file_path = file_path[:-4] + "_bak.ply"
            vertex_number = 0
            with open(bak_file_path, "w") as f:
                f.write(header)
                for vertex in vertices:
                    if (method == 1):
                        x2, y2, z2 = molodensky_transform(
                            vertex[0], vertex[1], vertex[2], dx, dy, dz, wx, wy, wz, m
                        )
                    else:
                        x2, y2, z2 = molodensky_transform2(
                            vertex[0], vertex[1], vertex[2], dx, dy, dz, wx, wy, wz, m
                        )
                    if not (np.isnan(x2) or np.isnan(y2) or np.isnan(z2)):
                        f.write(f"{x2} {y2} {z2} {vertex[3]}\n")
                        vertex_number += 1
                    # else:
                    #     print(f'{x2} {y2} {z2} {vertex[3]}\n')
            flist = []
            # 修改数量
            with open(bak_file_path, "r") as f2:
                flist = f2.readlines()
                flist[2] = f"element vertex {vertex_number}\n"
            with open(bak_file_path, "w") as file:
                file.writelines(flist)

    def run(self):
        """
        Runs the function to read odometry files and write point cloud files.

        Returns:
        None.
        """
        txt_files = []
        ply_files = []
        self.msg_signal.emit(str("开始计算！"))
        self.msg_signal.emit(str("选择使用第"+self.__method+"方法！"))
        for file_name in os.listdir(self.__positionPath):
            if file_name.endswith(".txt"):
                txt_files.append(file_name)
        for file_name in os.listdir(self.__pointPath):
            if file_name.endswith(".ply"):
                ply_files.append(file_name)
        for txt_file in txt_files:
            time_stamp = txt_file.split("_")[0]
            dx, dy, dz, wx, wy, wz, m = self.read_odom_file(
                os.path.join(self.__positionPath, txt_file))
            for ply_file in ply_files:
                if ply_file.startswith(time_stamp):
                    self.msg_signal.emit(str(time_stamp)+"计算中！")
                    self.write_ply_file(
                        os.path.join(self.__pointPath, ply_file), dx, dy, dz, wx, wy, wz, m, self.__method)
                    break
        self.msg_signal.emit(str('计算完成！'))
