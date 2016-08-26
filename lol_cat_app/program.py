import os

import cat_service


def main():
    # print the header
    print_the_header()
    # get or create output folder
    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)

    # download cats
    download_cats(folder)
    # display cats


def print_the_header():
    print('----------------------------------')
    print('         LOL CAT APP   ')
    print('----------------------------------')
    print()


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat pictures'
    full_path = os.path.join(base_folder, folder)
    # print(base_folder)
    # print(full_path)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    cat_count = 8
    for i in range(1, cat_count +1):
        name = 'lolcat{}'.format(i)
        cat_service.get_cat(folder, name)
        # print(i, end=', ')

if __name__ == '__main__':
    main()

