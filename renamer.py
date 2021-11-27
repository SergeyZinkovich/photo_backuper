import collections
import os
import shortuuid


def get_overlapped_filenames(files):
    c = collections.Counter(files)
    overlapped = [key for key, val in c.items() if val > 1]

    return overlapped


def rename_overlapped(tree, files, base_path, dirs=None, dry_run=False, verbose=True):
    overlapped_filenames = get_overlapped_filenames(files)

    overlapped = []
    for path, data in tree.items():
        if dirs and path in dirs:
            continue

        for filename in data[1]:
            if filename in overlapped_filenames:
                overlapped.append([path, filename])
    overlapped.sort(key=lambda x: x[1])

    if verbose:
        for path, filename in overlapped:
            print(os.path.join(path, filename))
        c = collections.Counter(list(map(lambda x: x[0], overlapped)))
        print(c)

    if not dry_run:
        for path, filename in overlapped:
            os.rename(
                os.path.join(base_path, path, filename),
                os.path.join(base_path, path, shortuuid.uuid()) + os.path.splitext(filename)[1]
            )
