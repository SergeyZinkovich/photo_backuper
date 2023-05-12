from src.renamer import rename_all as _rename_all
from src.renamer import rename_overlapped as _rename_overlapped
from src.file_processor import get_tree, get_paths


def rename_all(path: str):
    tree = get_tree(path)
    _rename_all(path, tree)


def rename_overlapped(path: str, dry_run: bool = False, verbose: bool = True):
    tree = get_tree(path)
    _rename_overlapped(tree, path, dry_run=dry_run, verbose=verbose)


if __name__ == "__main__":
    # rename_overlapped('')
    # rename_all('')
    pass
