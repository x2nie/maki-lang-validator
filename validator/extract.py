import os
import zipfile

def get_extraction_path(output_folder, zip_filename):
    """
    Generate the extraction path based on the zip filename.
    Structure: /output/[first_char]/[first_two_chars]/[zip_filename_without_extension]/
    """
    first_char = zip_filename[0].lower()  # First character (lowercase)
    first_two_chars = zip_filename[:2].lower()  # First two characters (lowercase)
    zip_name_without_ext = os.path.splitext(zip_filename)[0]  # Remove '.zip' from the name
    extraction_path = os.path.join(output_folder, first_char, first_two_chars, zip_name_without_ext)
    return extraction_path

def extract_specific_files(zip_path, extract_to, extensions):
    """
    Extract specific files from a zip archive based on their extensions.
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            # Check if the file has one of the desired extensions
            if any(file_info.filename.lower().endswith(ext) for ext in extensions):
                # Extract the file while preserving the directory structure
                zip_ref.extract(file_info, extract_to)
                print(f"Extracted: {file_info.filename} to {extract_to}")

def extract_all_zips(raw_folder, output_folder, extensions):
    """
    Extract all zip files in the 'raw_folder' to 'output_folder' with the specified structure.
    Only files with the specified extensions are extracted.
    """
    # Iterate over all files in the raw folder
    for zip_filename in os.listdir(raw_folder):
        if zip_filename[-4:].lower() in ['.zip', '.wal']:
            # Construct the full path to the zip file
            zip_path = os.path.join(raw_folder, zip_filename)
            
            # Get the extraction path based on the zip filename
            extraction_folder = get_extraction_path(output_folder, zip_filename)
            if os.path.exists(extraction_folder):
                continue

            # Create the extraction folder if it doesn't exist
            os.makedirs(extraction_folder, exist_ok=True)
            
            # Extract specific files from the zip
            extract_specific_files(zip_path, extraction_folder, extensions)

# Example usage
raw_folder = 'validator/skins/raw'  # Folder containing all the zip files
output_folder = 'validator/skins/extracted'  # Base folder for extraction
extensions = ['.m', '.maki']  # File extensions to extract

# Extract all zip files
extract_all_zips(raw_folder, output_folder, extensions)