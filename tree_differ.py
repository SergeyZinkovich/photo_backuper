import os.path


def difference_report(source_path, source_tree, target_path, target_tree, full_report=True):
    extra_folders, extra_files_in_folders, extra_files = get_tree_diff(source_tree, target_path, target_tree)
    missed_folders, missed_files_in_folders, missed_files = get_tree_diff(target_tree, source_path, source_tree)

    def print_report_part(arr, count_name):
        if full_report:
            print('#######################################')
        print(count_name, 'count', len(arr), end='\n\n')

        if full_report:
            for i in arr:
                print(i)
        print()

    print_report_part(extra_folders, 'Extra folders')
    print_report_part(extra_files_in_folders, 'Extra files in folders')
    print_report_part(extra_files, 'Extra files')

    print_report_part(missed_folders, 'Missed folders')
    print_report_part(missed_files_in_folders, 'Missed files in folders')
    print_report_part(missed_files, 'Missed files')


def get_tree_diff(source_tree, target_path, target_tree):
    folders = []
    files_in_folders = []
    files = []

    for path, data in target_tree.items():
        for folder in data[0]:
            if path not in source_tree or folder not in source_tree[path][0]:
                folders.append(os.path.join(target_path, path, folder))

        for file in data[1]:
            if path not in source_tree:
                files_in_folders.append(os.path.join(target_path, path, file))
            elif file not in source_tree[path][1]:
                files.append(os.path.join(target_path, path, file))

    return folders, files_in_folders, files
