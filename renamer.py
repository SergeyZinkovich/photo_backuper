import collections
import os
import shortuuid


def get_overlapped_filenames(files):
    c = collections.Counter(files)
    overlapped = [key for key, val in c.items() if val > 1]

    return overlapped


def get_name_path_dict(tree):
    name_path_dict = {}

    for path, data in tree.items():
        for filename in data[1]:
            if filename in name_path_dict:
                name_path_dict[filename].add(path)
            else:
                name_path_dict[filename] = {path}

    return name_path_dict


def rename_overlapped(tree, base_path, dry_run=False, verbose=True):
    overlapped = get_name_path_dict(tree)
    overlapped = {filename: paths for filename, paths in overlapped if len(paths) > 1}

    for filename, paths in overlapped:
        if len(paths) < 2:
            continue

        if verbose:
            print(f'{filename} appears {len(paths)} times:')

        for path in paths:
            if verbose:
                print(os.path.join(base_path, path, filename))

            if not dry_run:
                os.rename(
                    os.path.join(base_path, path, filename),
                    os.path.join(base_path, path, shortuuid.uuid()) + os.path.splitext(filename)[1]
                )


def rename_all(base_path, tree):
    for path, data in tree.items():
        for filename in data[1]:
            os.rename(
                os.path.join(base_path, path, filename),
                os.path.join(base_path, path, shortuuid.uuid()) + os.path.splitext(filename)[1]
            )
