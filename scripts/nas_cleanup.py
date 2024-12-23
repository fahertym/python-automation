import os
import shutil
import logging

# Base NAS directory
NAS_PATH = "/mnt/nas"

# Define categories and extensions
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".md"],
    "Archives": [".zip", ".rar", ".7z", ".tar.gz", ".gz"],
    "ISOs": [".iso"],
    "Large_Files": [],  # Files > 1GB will go here
    "Other": []  # Catch-all for uncategorized files
}

# Setup logging
LOG_FILE = "nas_cleanup.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Function to get file size in MB
def get_file_size(file_path):
    try:
        return os.path.getsize(file_path) / (1024 * 1024)
    except FileNotFoundError:
        logging.warning(f"File not found: {file_path}")
        print(f"Warning: File not found: {file_path}")
        return None
    except OSError as e:
        logging.warning(f"Error accessing file: {file_path} - {e}")
        print(f"Warning: Error accessing file: {file_path} - {e}")
        return None

# Organize NAS
def organize_nas():
    print(f"Starting NAS cleanup for: {NAS_PATH}")
    for root, dirs, files in os.walk(NAS_PATH):
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file)[1].lower()
            file_size_mb = get_file_size(file_path)

            if file_size_mb is None:  # Skip files with errors
                continue

            # Determine target category
            target_category = "Other"
            for category, extensions in CATEGORIES.items():
                if file_ext in extensions:
                    target_category = category
                    break

            # Move large files
            if file_size_mb > 1024:
                target_category = "Large_Files"

            # Create target folder and move file
            target_folder = os.path.join(NAS_PATH, target_category)
            os.makedirs(target_folder, exist_ok=True)
            target_path = os.path.join(target_folder, file)

            try:
                shutil.move(file_path, target_path)
                print(f"Moved: {file_path} -> {target_path}")
                logging.info(f"Moved: {file_path} -> {target_path}")
            except Exception as e:
                print(f"Failed to move {file_path}: {e}")
                logging.error(f"Failed to move {file_path}: {e}")

    print("NAS cleanup completed! Check the log for details.")
    logging.info("NAS cleanup completed!")

# Main function
if __name__ == "__main__":
    organize_nas()
