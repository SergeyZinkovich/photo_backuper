from src.type_converter import convert_all_to_jpeg as _convert_all_to_jpeg
from src.type_converter import change_all_alias_extensions_to_jpeg as _change_all_alias_extensions_to_jpeg
from src.file_processor import get_tree, get_paths


def convert_all_to_jpeg(path: str):
    tree = get_tree(path)
    paths = get_paths(path, tree)
    _convert_all_to_jpeg(paths)


def change_all_alias_extensions_to_jpeg(path: str):
    tree = get_tree(path)
    paths = get_paths(path, tree)
    _change_all_alias_extensions_to_jpeg(paths)


if __name__ == "__main__":
    # change_all_alias_extensions_to_jpeg('')
    # convert_all_to_jpeg('')
    pass
