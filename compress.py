# py -m ensurepip --upgrade
# py -m pip install py7zr

import sys
import time
import glob
import py7zr
import multiprocessing

def zip_file(obj_file, zip_file_name):
    print(obj_file, "->", zip_file_name)
    with py7zr.SevenZipFile(zip_file_name, "w") as zip_file:
        zip_file.write(obj_file)

def main():
    if len(sys.argv) == 2:
        obj_file = sys.argv[1]
        zip_file_name = obj_file.replace(".obj", ".7z").replace("obj\\", "7z\\")
        zip_file(obj_file, zip_file_name)
        return

    args_map = []
    for obj_file in sorted(glob.glob("obj/*.obj")):
        zip_file_name = obj_file.replace(".obj", ".7z").replace("obj\\", "7z\\")
        args_map.append((obj_file, zip_file_name))

    start = time.time()

    # TODO: CTRL+C freaks out when trying to interrupt this
    with multiprocessing.Pool(10) as pool:
        pool.starmap(zip_file, args_map)

    end = time.time()
    print("Time elapsed:", end - start)

if __name__ == "__main__":
    main()
