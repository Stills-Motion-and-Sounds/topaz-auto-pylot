# Topaz Auto-Pylot

This project contains a Python script `auto-pylot.py` that automates the process of using the Topaz Photo AI command line interface (CLI) to process images. The script scans through a directory or processes a single file, runs all photos through AutoPilot, and exports them as full-sized JPEGs and 70% quality JPEGs.

## Features

- Automatically processes images using Topaz Photo AI.
- Exports processed images with both 100% and 70% JPEG quality.
- Handles both individual files and directories recursively.
- Logs all commands and outputs for troubleshooting.

## Prerequisites

- Topaz Photo AI installed on your system.
- Python 3.x installed on your system.

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/Stills-Motion-and-Sounds/topaz-auto-pylot.git
    cd topaz-auto-pylot
    ```

2. Ensure Topaz Photo AI is installed and the executable path is correct in the script.

## Usage

1. Run the `auto-pylot.py` script:
    ```bash
    python3 auto-pylot.py
    ```

2. When prompted, enter the path to the file or directory you want to process. The script will:
    - Process all images in the directory recursively (if a directory is provided).
    - Process the single image (if a file is provided).
    - Export processed images with filenames ending in `- topaz @ 100` and `- topaz @ 70` for 100% and 70% quality respectively.

## Logging

- The script generates a log file in the format `topaz_auto_pylot_<timestamp>.log` in the current directory.
- The log file contains detailed information about the commands run and any errors encountered.

## Example

If you have a directory `/path/to/images` containing image files, you can run the script and process all images within that directory:

```bash
python3 auto-pylot.py
