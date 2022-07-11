import shutil
from image_comparer import duplicate_exists
from tree_differ import difference_report
from renamer import *


def get_tree(path):
    tree = {}
    for i in os.walk(path):
        key = os.path.relpath(i[0], path)
        tree[key] = [i[1], i[2]]

    return tree


def get_paths(base_path, tree):
    paths = []

    for path, data in tree.items():
        for filename in data[1]:
            paths.append(os.path.join(base_path, path, filename))

    return paths


def get_files(tree):
    files = []

    for data in tree.values():
        files += data[1]

    return files


def copy_forward(source_path, target_path, source_tree, target_tree, verbose=True):
    if source_tree == target_tree:
        if verbose:
            print('All is up to date')
        return

    for folder_path, data in source_tree.items():
        for file in data[1]:
            if folder_path in target_tree and file in target_tree[folder_path][1]:
                continue
            else:
                if verbose:
                    print('miss', os.path.join(source_path, folder_path, file))
                shutil.copy(os.path.join(source_path, folder_path, file), os.path.join(target_path, folder_path, file))


def delete_with_existence_check(source_tree, target_path, target_tree, check_by_pixels=True, verbose=True,
                                dry_run=False):
    name_path_dict = get_name_path_dict(target_tree)

    for folder_path, data in target_tree.items():
        for file in data[1]:
            if folder_path in source_tree and file in source_tree[folder_path][1]:
                continue
            else:
                if len(name_path_dict[file]) > 1 and \
                        (not check_by_pixels or duplicate_exists(target_path, folder_path, file, name_path_dict[file])):
                    if verbose:
                        print('Deleted', os.path.join(target_path, folder_path, file))

                    if not dry_run:
                        os.remove(os.path.join(target_path, folder_path, file))
                    name_path_dict[file].remove(folder_path)
                elif verbose:
                    print('Need to delete, but there is no copy', os.path.join(target_path, folder_path, file))


if __name__ == "__main__":
    sours_path = 'F:\\Saver\\Фото'
    target_path = 'F:\\Saver\\Фото'

    sours_tree = get_tree(sours_path)
    sours_files = get_files(sours_tree)
    target_tree = get_tree(target_path)
    target_files = get_files(target_tree)

    rename_overlapped(sours_tree, sours_files, sours_path)

    copy_forward(sours_path, sours_files, sours_tree, target_tree)

