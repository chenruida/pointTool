import os
import numpy as np
import struct


def read_odom_file(file_path):
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


def write_ply_file(file_path):
    with open(file_path, "rb") as f:
        header = ""
        while True:
            line = f.readline().decode("ascii")
            header += line
            if line.strip() == "end_header":
                break
                # Modify the header
        header = header.replace("format binary_little_endian 1.0", "format ascii 1.0")
        vertex_data = f.read()
        vertex_size = struct.calcsize("ffff")
        vertex_count = len(vertex_data) // vertex_size
        vertices = []
        for i in range(vertex_count):
            vertex = struct.unpack(
                "ffff", vertex_data[i * vertex_size : (i + 1) * vertex_size]
            )
            vertices.append(vertex)
        bak_file_path = file_path[:-4] + "_select.ply"
        vertex_number = 0
        with open(bak_file_path, "w") as f:
            f.write(header)
            for vertex in vertices:
                x2, y2, z2 = vertex[0], vertex[1], vertex[2]
                if not (np.isnan(x2) or np.isnan(y2) or np.isnan(z2)):
                    f.write(f"{x2} {y2} {z2} {vertex[3]}\n")
                    vertex_number += 1
        flist = []
        # 修改数量
        with open(bak_file_path, "r") as f2:
            flist = f2.readlines()
            flist[2] = f"element vertex {vertex_number}\n"
        with open(bak_file_path, "w") as file:
            file.writelines(flist)
            # f.write(flist)
            # for i in range(vertex_number):
            #     f.write(vertices_transform[i])


# 定义主函数
if __name__ == "__main__":
    txt_files = []
    ply_files = []
    pcd_list = []
    distance = -3.41056112722
    odom_dir = "./0426/odom1/"
    point_cloud_dir = "./0426/ply/"
    for file_name in os.listdir(odom_dir):
        if file_name.endswith(".txt"):
            txt_files.append(file_name)
    for file_name in os.listdir(point_cloud_dir):
        if file_name.endswith(".ply"):
            ply_files.append(file_name)
    for txt_file in txt_files:
        time_stamp = txt_file.split("_")[0]
        dx, dy, dz, wx, wy, wz, m = read_odom_file(os.path.join(odom_dir, txt_file))
        if abs(dx - distance) > 0.4 and abs(dx - distance) < 0.6:
            distance = dx
            for ply_file in ply_files:
                if ply_file.startswith(time_stamp):
                    write_ply_file(os.path.join(point_cloud_dir, ply_file))
                    break
