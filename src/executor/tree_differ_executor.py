from src.tree_differ import difference_report as _difference_report
from src.file_processor import get_tree, get_paths


def difference_report(path: str, target_path: str, full_report: bool = True):
    source_tree = get_tree(path)
    target_tree = get_tree(target_path)
    _difference_report(source_path=path,
                       source_tree=source_tree,
                       target_path=target_path,
                       target_tree=target_tree,
                       full_report=full_report)


if __name__ == "__main__":
    # difference_report('', '')
    pass
