from src.image_comparer import duplicate_exists
from src.metadata_setter import get_video_taken_date
from src.type_converter import convert_all
from src.file_processor import *


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
