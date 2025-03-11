# WELCOME TO File_Sorter!
# This script will sort all the files in the catalogue you choose into several categories.

"""
Below, in the dictionary named `fileTypesDict`, you can check what categories are predefined and what file extensions
are assigned to each category. Feel free to add your own categories or file extensions or move file extensions to other categories.
`fileTypesDict.keys()` are for the category names, and `fileTypesDict.values()` are for file extensions assigned to this category.
"""

# !!!ATTENTION!!!
# If there is a directory named by the category (e.g., if you used this script before) and there is a file with the same name
# in the category (destination) directory, it will be overwritten!!!

# This will be upgraded in the future to choose what to do in such conflicts, but for now, this script is just for training.
# It will also be upgraded with a log file containing data and history of usage.
# ... someday :)

# Bon appétit! | 2024 | R32NOR | ZOLCBYTERS

import os
import shutil


def get_directory_path():
    """Gets the directory path from user input."""
    return input('Enter the directory path you want to sort: ')


def get_file_list(directory):
    """
    Returns a list of all filenames in the chosen directory.

    :param directory: Directory path where files need to be sorted.
    :return: List of files in the chosen directory (excluding folders).
    """
    return [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]


def get_file_extension(file_name):
    """
    Returns the file extension without the dot.

    :param file_name: Name of the file.
    :return: File extension.
    """
    return os.path.splitext(file_name)[1][1:].lower()


def get_file_category(file_extension):
    """
    Returns the category of the file based on its extension.

    :param file_extension: File extension without the dot.
    :return: Category of the file defined in `fileTypesDict`.
    """
    file_types_dict = {
        'Images': ['png', 'jpg', 'bmp', 'gif'],
        'PDF': ['pdf'],
        'Docs': ['doc', 'docx', 'xls', 'xlsx', 'txt', 'ppt', 'pptx', 'odt'],
        'Music': ['mp3', 'wav'],
        'Video': ['mp4'],
        'Archive': ['rar', 'zip', '7z']
    }

    for category, extensions in file_types_dict.items():
        if file_extension in extensions:
            return category
    return 'Other'


def create_category_directory(directory, category):
    """
    Creates a category directory if it does not exist.

    :param directory: Directory path where files need to be sorted.
    :param category: Category of the file.
    """
    category_dir = os.path.join(directory, category)
    if not os.path.exists(category_dir):
        os.makedirs(category_dir)


def move_file_to_category(directory, file_name, category):
    """
    Moves a file to its appropriate category directory.

    :param directory: Directory path where files need to be sorted.
    :param file_name: Name of the file.
    :param category: Category of the file.
    """
    source_file_path = os.path.join(directory, file_name)
    destination_dir_path = os.path.join(directory, category, file_name)
    shutil.move(source_file_path, destination_dir_path)


def sort_files(directory):
    """
    Sorts files in the chosen directory into their respective categories.

    :param directory: Directory path where files need to be sorted.
    """
    file_list = get_file_list(directory)

    for file in file_list:
        file_extension = get_file_extension(file)
        file_category = get_file_category(file_extension)
        create_category_directory(directory, file_category)
        move_file_to_category(directory, file, file_category)


if __name__ == "__main__":
    directory_path = get_directory_path()
    sort_files(directory_path)
