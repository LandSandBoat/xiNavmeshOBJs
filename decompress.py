# py -m ensurepip --upgrade
# py -m pip install py7zr

import sys
import time
import glob
import py7zr
import multiprocessing

def unzip_file(zip_file):
    print(zip_file)
    with py7zr.SevenZipFile(zip_file, "r") as zip_file:
        zip_file.extract()

def main():
    if len(sys.argv) == 2:
        unzip_file(sys.argv[1])
        return

    # No args, decompress all
    args_map = []
    for zip_file in sorted(glob.glob("7z/*.7z")):
        args_map.append(zip_file)

    start = time.time()

    # TODO: CTRL+C freaks out when trying to interrupt this
    with multiprocessing.Pool(10) as pool:
        pool.map(unzip_file, args_map)

    end = time.time()
    print("Time elapsed:", end - start)

if __name__ == "__main__":
    main()
