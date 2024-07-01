import os
import subprocess
import logging
from datetime import datetime

# Configure logging
log_filename = f"topaz_auto_pylot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to get user input for folder or file path
def get_path(prompt):
    path = input(prompt).strip()  # Remove leading/trailing whitespace
    if not os.path.exists(path):
        logging.error(f"The path '{path}' does not exist.")
        print(f"Error: The path '{path}' does not exist.")
        exit(1)
    return path

# Get user input for the path
input_path = get_path("Enter the path to the file or directory: ")

# Define Topaz Photo AI executable path
topaz_executable = "/Applications/Topaz Photo AI.app/Contents/MacOS/Topaz Photo AI"

# Function to run Topaz Photo AI CLI command
def run_topaz_cli(input_path, output_path, quality):
    command = [
        topaz_executable,
        "--cli", input_path,
        "--output", output_path,
        "--format", "jpeg",
        "--quality", str(quality)
    ]
    logging.info(f"Running command: {' '.join(command)}")
    print(f"Running command: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)
    logging.info(f"Command output: {result.stdout}")
    logging.error(f"Command error: {result.stderr}")

# Function to process a single image file
def process_file(file_path):
    # Construct new filenames
    dir_name = os.path.dirname(file_path)
    base_name, ext = os.path.splitext(os.path.basename(file_path))
    output_file_full = os.path.join(dir_name, f"{base_name} - topaz @ 100{ext}")
    output_file_70 = os.path.join(dir_name, f"{base_name} - topaz @ 70{ext}")

    # Process and save the images
    run_topaz_cli(file_path, output_file_full, 100)
    run_topaz_cli(file_path, output_file_70, 70)

# Function to process a directory recursively
def process_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tif', '.tiff', '.dng')):
                file_path = os.path.join(root, file)
                process_file(file_path)

# Determine if the input path is a file or directory and process accordingly
if os.path.isfile(input_path):
    process_file(input_path)
elif os.path.isdir(input_path):
    process_directory(input_path)
else:
    logging.error(f"The path '{input_path}' is neither a file nor a directory.")
    print(f"Error: The path '{input_path}' is neither a file nor a directory.")
    exit(1)
