import shutil
import os
from . import renamer
from . import image_comparer


def get_tree(path: str):
    tree = {}
    for root, dirs, files in os.walk(path):
        root = os.path.relpath(root, path)
        tree[root] = [dirs, files]

    return tree


def get_paths(base_path: str, tree: dict):
    paths = []

    for path, data in tree.items():
        for filename in data[1]:
            paths.append(os.path.normpath(os.path.join(base_path, path, filename)))

    return paths


def copy_forward(source_path: str, target_path: str, source_tree: dict, target_tree: dict, verbose: bool = True):
    if source_tree == target_tree:
        if verbose:
            print('All is up to date')
        return

    for folder_path, data in source_tree.items():
        if len(data[1]):
            os.makedirs(os.path.join(target_path, folder_path), exist_ok=True)

        for file in data[1]:
            if folder_path in target_tree and file in target_tree[folder_path][1]:
                continue
            else:
                shutil.copy(os.path.join(source_path, folder_path, file), os.path.join(target_path, folder_path, file))
                if verbose:
                    print('Copied', os.path.normpath(os.path.join(source_path, folder_path, file)))


def delete_with_existence_check(source_tree: dict, target_path: str, target_tree: dict, check_by_pixels: bool = True,
                                verbose: bool = True, dry_run: bool = False):
    name_path_dict = renamer.get_name_path_dict(target_tree)

    for folder_path, data in target_tree.items():
        for file in data[1]:
            if folder_path in source_tree and file in source_tree[folder_path][1]:
                continue
            else:
                if len(name_path_dict[file]) > 1 and \
                        (not check_by_pixels or image_comparer.duplicate_exists(target_path, folder_path, file, name_path_dict[file])):
                    if verbose:
                        print('Deleted', os.path.normpath(os.path.join(target_path, folder_path, file)))

                    if not dry_run:
                        os.remove(os.path.join(target_path, folder_path, file))
                    name_path_dict[file].remove(folder_path)
                elif verbose:
                    print('Need to delete, but there is no copy',
                          os.path.normpath(os.path.join(target_path, folder_path, file)))


def delete_empty_dirs(base_path: str, source_check: bool = False, source_tree: dict = None, verbose: bool = True):
    for root, dirs, files in os.walk(base_path, topdown=False):
        root = os.path.relpath(root, base_path)
        if not os.listdir(os.path.join(base_path, root)) and (not source_check or root not in source_tree):
            os.rmdir(os.path.join(base_path, root))
            if verbose:
                print('Deleted', os.path.normpath(os.path.join(base_path, root)))

        elif verbose and not os.listdir(os.path.join(base_path, root)):
            print('Empty directory in source', os.path.normpath(os.path.join(base_path, root)))
