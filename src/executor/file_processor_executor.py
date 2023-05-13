from src.file_processor import copy_forward as _copy_forward
from src.file_processor import delete_with_existence_check as _delete_with_existence_check
from src.file_processor import delete_empty_dirs as _delete_empty_dirs
from src.file_processor import get_tree, get_paths


def copy_forward(path: str, target_path: str, verbose: bool = True):
    source_tree = get_tree(path)
    target_tree = get_tree(target_path)
    _copy_forward(source_path=path,
                  target_path=target_path,
                  source_tree=source_tree,
                  target_tree=target_tree,
                  verbose=verbose)


def delete_with_existence_check(path: str, target_path: str, check_by_pixels: bool = True, verbose: bool = True,
                                dry_run: bool = False):
    source_tree = get_tree(path)
    target_tree = get_tree(target_path)
    _delete_with_existence_check(source_tree=source_tree,
                                 target_path=target_path,
                                 target_tree=target_tree,
                                 check_by_pixels=check_by_pixels,
                                 verbose=verbose,
                                 dry_run=dry_run)


def delete_empty_dirs(path: str, source_path: str = None, verbose: bool = True):
    if source_path:
        source_tree = get_tree(source_path)
        source_check = True
    else:
        source_tree = None
        source_check = False

    _delete_empty_dirs(path, source_check=source_check, source_tree=source_tree, verbose=verbose)


if __name__ == "__main__":
    # copy_forward('', '')
    # delete_with_existence_check('', '')
    # delete_empty_dirs('')
    pass
