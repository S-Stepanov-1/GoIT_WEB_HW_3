import logging
import sys
import time
import shutil
from pathlib import Path
from threading import Thread

from categories import CATEGORIES, IGNORED_FOLDERS, ALL_EXTENSIONS

# === Logging configuration ===
logging.basicConfig(
    format='%(asctime)s  -  "%(threadName)s"  -   [%(levelname)s]  -→  %(message)s',
    level=logging.INFO,
    filename="sorter.log",
    filemode="w",
    encoding="utf-8"
)

logger = logging.getLogger()


def get_path_to_dir():
    try:
        abs_dir_path = Path(sys.argv[1])
        if abs_dir_path.is_dir():
            return abs_dir_path
        else:
            raise IsADirectoryError
    except Exception:
        print("\n  ===   Something went wrong. Please restart the program and try again.   ===\n")
        exit()


def create_folders(path_to_dir):
    parent_dir = Path(path_to_dir)
    for folder_name in IGNORED_FOLDERS:
        category_folder = parent_dir.joinpath(folder_name)
        if not category_folder.exists():
            category_folder.mkdir()


def move_file(path_to_file, category_folder):
    """If there is already the file with the same name in the destination folder, delete it; if not, move it to the destination folder"""
    is_file_in_category_folder = category_folder.joinpath(path_to_file.name)

    if is_file_in_category_folder.exists():
        path_to_file.unlink()
        logger.info(f"File \"{path_to_file.name}\" was deleted")
    else:
        shutil.move(path_to_file, category_folder)
        logger.info(f"File \"{path_to_file.name}\" was moved to \"{category_folder.name}\"")


def sort_file(path_to_file, root):
    """If file extension is in ALL_EXTENSION list, sort it to the destination folder; if not, sort it to other_formats"""
    file_extension = path_to_file.suffix[1:]

    if file_extension in ALL_EXTENSIONS:
        for category, extensions in CATEGORIES.items():
            if file_extension in extensions:
                move_file(path_to_file, root.joinpath(category))
                break
    else:
        move_file(path_to_file, root.joinpath("other_formats"))


def iterate_items(root_dir):
    """Iterate over all items in the given directory"""
    target_dir = Path(root_dir)
    stack = [target_dir]
    threads = []

    while stack:
        current_dir = stack.pop()

        for item in current_dir.iterdir():
            if item.is_dir() and item.name not in IGNORED_FOLDERS:
                logger.info(f"Folder is found: \"{item.name}\"")
                stack.append(item)

            elif item.is_file():
                thread = Thread(target=sort_file, args=(Path(item), Path(root_dir)))
                thread.start()
                threads.append(thread)

    [el.join() for el in threads]  # Waiting for all threads to end
    logger.info("End program")


def main():
    start = time.time()

    root_dir = get_path_to_dir()
    path = Path(root_dir)
    create_folders(path)  # creating folders according to category
    iterate_items(path)

    print(time.time() - start)


if __name__ == '__main__':
    main()
