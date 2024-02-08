import os
from shutil import move
from pathlib import Path

desktop_path = Path('/Users/Francesco/Desktop')


def organizza_scrivania(desktop_path):
    if not desktop_path.exists():
        print("Il percorso della scrivania non esiste.")
        return

    file_paths = [p for p in desktop_path.iterdir() if p.is_file()]

    for file_path in file_paths:
        ext = file_path.suffix.lower()[1:]
        if ext == "":
            ext = "SenzaEstensione"

        folder_path = desktop_path / ext

        folder_path.mkdir(exist_ok=True)

        dest_path = folder_path / file_path.name
        move(str(file_path), str(dest_path))
        print(f"Spostato: {file_path} -> {dest_path}")


organizza_scrivania(desktop_path)
