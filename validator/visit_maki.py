import os

def find_files_with_extension(directory, extension='.maki'):
    """
    Find all files with a specific extension in a directory (recursively).

    :param directory: The directory to search in.
    :param extension: The file extension to look for (e.g., '.maki').
    :return: A list of full paths to the files with the specified extension.
    """
    matched_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                full_path = os.path.join(root, file)
                matched_files.append(full_path)
    return matched_files

# Example usage
output_folder = 'validator/skins/extracted'  # Folder where the extracted files are located
extension = '.maki'  # File extension to search for


if __name__ == '__main__':
    # Find all .maki files in the output folder
    maki_files = find_files_with_extension(output_folder, extension)

    # Print the results
    for file_path in maki_files:
        print(file_path)