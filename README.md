# Fenix to FSLabs Cabin Announcements (F2FSLCAC)

This tool converts cabin announcement files from the Fenix A320 format  
into the FSLabs A320 format, using the correct filenames and folder  
structure required by FSLabs.

---

## REQUIREMENTS

1. **Python 3.12** (DO NOT use Python 3.13 – it is not compatible!)  
   ➤ [Download Python 3.12.10](https://www.python.org/downloads/release/python-31210/)

2. **FFmpeg** – for audio conversion  
   ➤ Installation guide: [Install FFmpeg on Windows](https://www.wikihow.com/Install-FFmpeg-on-Windows)  
   ➤ IMPORTANT: Ensure you add ffmpeg to system PATH

3. **Internet connection** – the script installs any Python packages it needs.

---

## HOW TO USE

1. Extract this zip to a folder.

2. Place your Fenix announcement folder (e.g. `EWG`, `AAL`) next to the script.  
   Example folder layout:

```
├── convert_announcements.py
├── EWG/
│ ├── AfterLanding[Morning].ogg
│ └── ...
```

3. Double-click `convert_announcements.py`.

4. Select your announcement folder by typing the number shown.

5. The script will:  
✔ Match file names from Fenix packs.  
✔ Rename them to FSLabs format (case-insensitive matching)  
✔ Save them into:  
➤ `export/YourFolderName/Sounds/Cabin/`

6. Copy the resulting `Sounds` folder into your FSLabs A320 installation  
directory or wherever you need your custom cabin sounds.

---

## NOTES

- The script performs **case-insensitive** matching of tags and filenames.

- If multiple matches are found for a file, you will be prompted to select which one to use.

- The script will **only notify you of matches**, not any files that were not matched.

- If the pack has pre-safety demos for morning, afternoon, and evening, you will still be asked  
to match for a generic one — choose any you wish.

---

## TROUBLESHOOTING

- If the script opens and closes instantly:  
- Right-click > Open with > Python  
- Or run from Command Prompt for better visibility

- If FFmpeg is not found:  
- Follow the guide here:  
 ➤ [Install FFmpeg on Windows](https://www.wikihow.com/Install-FFmpeg-on-Windows)  
- Make sure you select "Add to PATH" when installing FFmpeg

- If Python says “audioop” is missing:  
- You are likely using Python 3.13 — uninstall and use 3.12 instead
