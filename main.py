import shutil
from renamer import *


def get_tree(path):
    tree = {}
    for i in os.walk(path):
        key = os.path.relpath(i[0], path)
        tree[key] = [i[1], i[2]]

    return tree


def get_files(tree):
    files = []
    for data in tree.values():
        files += data[1]

    return files


def copy_forward(sours_path, target_path, sours_tree, target_tree):
    if sours_tree == target_tree:
        print('All is up to date')
        return

    for folder_path, data in sours_tree.items():
        for file in data[1]:
            if folder_path in target_tree and file in target_tree[folder_path][1]:
                continue
            else:
                print('miss', os.path.join(sours_path, folder_path, file))
                shutil.copy(os.path.join(sours_path, folder_path, file), os.path.join(target_path, folder_path, file))


if __name__ == "__main__":
    sours_path = 'F:\\Saver\\Фото'
    target_path = 'F:\\Saver\\Фото'

    sours_tree = get_tree(sours_path)
    sours_files = get_files(sours_tree)
    target_tree = get_tree(target_path)
    target_files = get_files(target_tree)

    rename_overlapped(sours_tree, sours_files, sours_path)

    copy_forward(sours_path, sours_files, sours_tree, target_tree)

