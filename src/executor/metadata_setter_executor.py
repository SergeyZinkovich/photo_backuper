from src.metadata_setter import change_taken_date_for_all as _change_taken_date_for_all
from src.file_processor import get_tree, get_paths
from datetime import datetime


def change_taken_date_for_all(path: str, taken_date: datetime, increase_date_in_sort_order: bool = False,
                              change_modification_time: bool = False, set_taken_date_to_access_time: bool = False):
    tree = get_tree(path)
    paths = get_paths(path, tree)
    _change_taken_date_for_all(paths=paths,
                               taken_date=taken_date,
                               increase_date_in_sort_order=increase_date_in_sort_order,
                               change_modification_time=change_modification_time,
                               set_taken_date_to_access_time=set_taken_date_to_access_time)


if __name__ == "__main__":
    # change_taken_date_for_all('', datetime.datetime(2022, 4, 4, 2, 2, 2))
    pass
