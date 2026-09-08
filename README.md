# File Organizer Tool 📁

An automated Python script that cleans and organizes messy directories (like your Downloads folder) based on file extensions. It automatically detects duplicates and logs every file action.

## Features ✨
- **Category-based Sorting**: Groups files into `Images`, `Documents`, `Videos`, `Audio`, `Archives`, `Code`, `Executables`, and `Others`.
- **Duplicate Detection**: Renames duplicate files safely using timestamping to prevent overwriting existing files.
- **Activity Logging**: Records all operations in `organizer.log` for audit and tracking.

## Technologies Used 🛠️
- Python 3
- Built-in modules: `os`, `shutil`, `logging`, `datetime`

## How to Run 🚀

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ahmed-codecraft/file-organizer-tool.git
   cd file-organizer-tool
