from config import get_downloads_path


def downloadsList(path):
    if path == None:
        return

    for file in path.iterdir():
        if file.is_file(): #and file.suffix == ".pdf":
            print(f"Archívo: {file.stem} | Típo: {file.suffix}")


if __name__ == "__main__":
    path = get_downloads_path()
    downloadsList(path)