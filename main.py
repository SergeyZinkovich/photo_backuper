import shutil
from src.image_comparer import duplicate_exists
from src.renamer import *
from src.metadata_setter import get_video_taken_date


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
            paths.append(os.path.normpath(os.path.join(base_path, path, filename)))

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
                    print('Copied', os.path.normpath(os.path.join(source_path, folder_path, file)))
                os.makedirs(os.path.join(target_path, folder_path), exist_ok=True)
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
                        print('Deleted', os.path.normpath(os.path.join(target_path, folder_path, file)))

                    if not dry_run:
                        os.remove(os.path.join(target_path, folder_path, file))
                    name_path_dict[file].remove(folder_path)
                elif verbose:
                    print('Need to delete, but there is no copy',
                          os.path.normpath(os.path.join(target_path, folder_path, file)))


def delete_empty_dirs(base_path, source_check=False, source_tree=None, verbose=True):
    for root, dirs, files in os.walk(base_path, topdown=False):
        root = os.path.relpath(root, base_path)
        if not source_check or root not in source_tree:
            try:
                os.rmdir(os.path.join(base_path, root))
            except OSError:
                pass
            else:
                if verbose:
                    print('Deleted', os.path.normpath(os.path.join(base_path, root)))

        elif verbose and not os.listdir(os.path.join(base_path, root)):
            print('Empty directory in source', os.path.normpath(os.path.join(base_path, root)))


if __name__ == "__main__":
    source_path = 'F:\\test'
    target_path = 'E:\\test'

    source_tree = get_tree(source_path)
    source_files = get_files(source_tree)
    target_tree = get_tree(target_path)
    target_files = get_files(target_tree)

    get_video_taken_date('F:\\Saver\\Фото\\просто фотки\\шкалка\\олимпиец.mp4')

    # delete_empty_dirs('E:\\test', source_check=True, source_tree=source_tree)

    # difference_report(source_path, source_tree, target_path, target_tree)

    # delete_with_existence_check(source_tree, target_path, target_tree, dry_run=True)

    # change_taken_date('C:\\Users\\Saver\\Downloads\\video.mp4', datetime.datetime(2022, 4, 4, 2, 2, 2))
    # change_taken_date_for_all(get_paths(source_path, source_tree), datetime.datetime(2022, 5, 29, 15, 2, 2), increase_date_in_sort_order=True)

    # rename_all(source_path, source_tree)

    # rename_overlapped(source_tree, source_files, source_path)
    #
    # copy_forward(source_path, target_path, source_tree, target_tree)
