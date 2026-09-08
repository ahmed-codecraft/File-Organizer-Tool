import os
import shutil
import logging
from datetime import datetime

# 1. Logging setup (Activity Log File)
logging.basicConfig(
    filename='organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 2. File Categories Mapping
CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.bmp', '.webp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.csv'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi', '.flv'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.tar', '.rar', '.7z'],
    'Code': ['.py', '.html', '.css', '.js', '.cpp', '.java', '.json'],
    'Executables': ['.exe', '.msi', '.deb', '.dmg']
}

def get_category(file_extension):
    """File ki extension ke hisab se category return karta hai."""
    for category, extensions in CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category
    return 'Others'

def organize_folder(target_directory):
    """Main function jo files ko check karke folders mein shift karta hai."""
    if not os.path.exists(target_directory):
        print(f"Error: Folder '{target_directory}' nahi mila.")
        return

    print(f"Organizing folder: {target_directory}\n" + "-"*40)
    logging.info(f"Started organizing directory: {target_directory}")

    # Sirf files ki list lena (folders ko chhor kar)
    files = [f for f in os.listdir(target_directory) if os.path.isfile(os.path.join(target_directory, f))]

    for file_name in files:
        # Log file ko organize karne se skip karein
        if file_name == 'organizer.log':
            continue

        file_path = os.path.join(target_directory, file_name)
        _, ext = os.path.splitext(file_name)

        category = get_category(ext)
        category_dir = os.path.join(target_directory, category)

        # Category folder banayein agar pehle se na ho
        os.makedirs(category_dir, exist_ok=True)

        destination_path = os.path.join(category_dir, file_name)

        # Duplicate file detection and renaming
        if os.path.exists(destination_path):
            base_name, file_ext = os.path.splitext(file_name)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_file_name = f"{base_name}_duplicate_{timestamp}{file_ext}"
            destination_path = os.path.join(category_dir, new_file_name)
            
            log_msg = f"Duplicate found: '{file_name}' renamed to '{new_file_name}' and moved to '{category}'"
            print(f"[DUPLICATE] {log_msg}")
            logging.warning(log_msg)
        else:
            log_msg = f"Moved '{file_name}' to '{category}/'"
            print(f"[MOVED] {log_msg}")
            logging.info(log_msg)

        # File move karein
        shutil.move(file_path, destination_path)

    print("-" * 40)
    print("Organization complete! Details 'organizer.log' mein save ho gayi hain.")
    logging.info("Completed organization task successfully.")

if __name__ == '__main__':
    # Apne computer ke Downloads folder ka path yahan dein
    # System default Downloads path:
    downloads_path = os.path.expanduser("~/Downloads")
    
    # Run the organizer
    organize_folder(downloads_path)