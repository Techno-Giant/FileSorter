
# File Sorting Application

The File Sorting Application is built using Python with Tkinter for the graphical user interface. Its primary function is to sort files based on extensions (audio, video, images, etc.) into organized folders.

# Features
- **File Sorting:** Files are sorted based on extensions (audio, video, images, etc.).
- **Extension Management:** Add or delete extensions using the GUI. Changes are reflected in extension files.
- **Error Handling:** Automatic checks for JSON formatting issues in extension files.

# Getting Started
# Folder Structure
- **extension_files:** Stores file extensions for each category.
- **prj_pics:** Contains icons and images used in the GUI.

# Absolute Paths (lines 6–22)
In the `extension_files` folder:
```python
path_imagefile = r"D:\MyDownload\FileSorter1\main_py_mini_prj\extension_files\image.txt"
path_audiofile = r"D:\MyDownload\FileSorter1\main_py_mini_prj\extension_files\audio.txt"
path_videofile = r"D:\MyDownload\FileSorter1\main_py_mini_prj\extension_files\video.txt"
path_docfile = r"D:\MyDownload\FileSorter1\main_py_mini_prj\extension_files\doc.txt"
```

In the `prj_pics` folder:
python
path_iconimage = r"D:\MyDownload\FileSorter1\main_py_mini_prj\prj_pics\icon.ico"
path_logo_icon = r"D:\MyDownload\FileSorter1\main_py_mini_prj\prj_pics\folder.png"
path_image_icon = r"D:\MyDownload\FileSorter1\main_py_mini_prj\prj_pics\image.png"
path_audio_icon = r"D:\MyDownload\FileSorter1\main_py_mini_prj\prj_pics\audio.png"
path_video_icon = r"D:\MyDownload\FileSorter1\main_py_mini_prj\prj_pics\video.png"
path_document_icon = r"D:\MyDownload\FileSorter1\main_py_mini_prj\prj_pics\document.png"
path_other_icon = r"D:\MyDownload\FileSorter1\main_py_mini_prj\prj_pics\audio.png"
```

# How It Works
1. **Extensions in JSON Format:** All extensions are stored in individual files in JSON format (e.g., `image.txt` for image extensions). No manual conversion is needed from string to list.
2. **Loading Extensions:** When the project starts, all functions to read extensions are called, and variables are assigned.
3. **Counting and Renaming Files:** Functions like `total_count()` and `rename_folder()` are used to count and rename files based on their extensions.
4. **Adding Extensions:** Select a radio button, enter the extension (without the dot), and the system will reflect changes in the list and the extension file.
5. **Deleting Extensions:** Click "Delete Ext", select the radio button, view the current extensions in the listbox, and delete them. Changes are reflected in the list and the extension file.
6. **Error Prevention:** The app automatically detects missing commas in extension files and alerts the user if the list becomes empty.

# Modules Used
- **os:** For interacting with the operating system, using `os.walk()` to traverse directories.
  - `root_path`: Current folder path.
  - `sub_path`: Subdirectories.
  - `files`: List of files.
- **shutil:** Used for moving files with `shutil.move()`.
- **json:** Used for reading and writing extension lists.
  - `json.loads()`: Converts JSON-formatted strings to Python objects (lists).
  - `json.dumps()`: Converts Python objects (lists) to JSON-formatted strings.

# Important Notes
- **Error Handling:** Ensure proper JSON formatting when manually editing files. Refer to `all_extension.txt` for a list of all added extensions.
  