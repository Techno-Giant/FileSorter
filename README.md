# File Sorting Application 📂✨

A Python app with a Tkinter GUI that helps you organize files by their extensions (audio, video, images, and more). No more clutter! 🎉

## How It Works:
1. **Extensions in JSON**: Each type of file (like images, audio) has its own file where extensions are stored in JSON format.
2. **Sorting**: Browse a folder, and the app counts files and renames them by extension (all lowercase).
3. **Add/Delete Extensions**: Easily add or remove extensions through the GUI—no `.dot` needed, it’s auto-handled! 💡
4. **Error Checks**: Pop-up alerts if JSON formatting (like missing commas) is off. Stay error-free!

## Setup 🛠
- **extension_files** folder: Holds `.txt` files for each file type.
- **prj_pics** folder: Icons and images used in the app’s UI.


## Modules Used 💻
- `os`: For walking through directories and managing files.
- `shutil`: For moving files.
- `json`: To handle extension files stored in JSON format.

Enjoy a clutter-free folder life! 🎯
