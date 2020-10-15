#!/bin/env python3

import os
import shutil

curr_folder = os.path.dirname(os.path.realpath(__file__))

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


def list_media(exts):
    media_files = []

    for ext in exts:
        media_files += [file for file in os.listdir(curr_folder) if file.endswith(ext)]

    return media_files


imgs = list_media(img_exts)
vids = list_media(vid_exts)

imgs_folder = os.path.join(curr_folder, "IMAGES")
vids_folder = os.path.join(curr_folder, "VIDEOS")


def create_folder_if_not_exists(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)


def move_files(files, files_folder):
    for file in files:
        print(file)
        shutil.move(os.path.join(curr_folder, file), files_folder)


for folder in (imgs_folder, vids_folder):
    create_folder_if_not_exists(folder)

move_files(imgs, imgs_folder)
move_files(vids, vids_folder)
