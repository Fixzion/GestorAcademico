from uuid import main

from config import get_downloads_path
import pathlib
import os


def reader(path):
    print (f"La ruta a leer es {path}")


path = get_downloads_path()
reader(path)