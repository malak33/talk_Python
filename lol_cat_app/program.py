import os
import platform
import cat_service
import subprocess


def main():
    # print the header
    print_the_header()
    # get or create output folder
    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)

    # download cats
    download_cats(folder)
    # display cats
    display_cats(folder)


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
    print('Contacting server to download cat pics...')
    cat_count = 8
    for i in range(1, cat_count +1):
        name = 'lolcat{}'.format(i)
        print('Downloading cat pics: ' + name)
        cat_service.get_cat(folder, name)
        # print(i, end=', ')
    print('Done.')


def display_cats(folder):
    # open folder
    print('Displaying cats in OSX window.')
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't support your os" + platform.system())


if __name__ == '__main__':
    main()

