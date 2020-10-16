#!/bin/env python3

import os
import shutil
from os.path import expanduser

import click

img_exts = [
    "png",
    "gif",
    "jpg",
    "jpeg",
    "webp",
    "svg",
    "tif",
    "tiff",
    "bmp",
    "psd",
    "xcf",
    "ico",
]

vid_exts = [
    "mkv",
    "mp4",
    "webm",
    "m4v",
    "mov",
    "hevc",
    "wmv",
    "vob",
    "flv",
    "avi",
    "3gp",
    "ogg",
]

# curr_folder = os.path.dirname(os.path.realpath(__file__))
home_folder = expanduser("~")

docs_src_folder = os.path.join(home_folder, "Documents")
chrome_download_src_folder = os.path.join(docs_src_folder, "chrome_download")

imgs_dst_folder = os.path.join(docs_src_folder, "_IMAGES")
vids_dst_folder = os.path.join(docs_src_folder, "_VIDEOS")


def create_folder_if_not_exists(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)


def list_files(folder, exts):
    files = []
    num_of_files_ext = {}

    for ext in exts:
        # files += [file for file in os.listdir(folder) if file.endswith(ext)]
        for file in os.listdir(folder):
            if file.endswith(ext):
                files.append(file)
                num_of_files_ext[ext] = num_of_files_ext.get(ext, 0) + 1

    if files:
        for ext, num_of_files in num_of_files_ext.items():
            print(f"Number of {ext.upper()} files: {num_of_files}")

    return files


def move_files(files, src_folder, dst_folder):
    for file in files:
        try:
            shutil.move(os.path.join(src_folder, file), dst_folder)

        # if file already exists or other error
        except shutil.Error as e:
            print(e)
            print(os.path.join(src_folder, file))
            # print("Removing the existing file")
            # os.remove(os.path.join(src_folder, file))


def order_files(*src_folders):
    for src_folder in src_folders:
        try:
            imgs = []
            vids = []

            print(f"Locating files in {src_folder} folder:")

            imgs += list_files(src_folder, img_exts)
            vids += list_files(src_folder, vid_exts)

            if not imgs and not vids:
                print("No files to move in the folder")
                continue

            files = {imgs_dst_folder: imgs, vids_dst_folder: vids}

            if click.confirm("Move files from the folder?", default=True):
                for folder in files:
                    create_folder_if_not_exists(folder)

                    move_files(
                        files[folder],
                        src_folder,
                        folder,
                    )

        # if there is no source folder
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    order_files(docs_src_folder, chrome_download_src_folder)
