# Fenix to FSLabs Cabin Announcements Converter (F2FSLCAC)

This tool converts cabin announcement files from the Fenix A320 format into the FSLabs A320 format, using the correct filenames and folder structure required by FSLabs.

## REQUIREMENTS

1. **Python** (Currently tested with 3.12.10, should work fine with 3.13.x.)  
   ➤ [Download Python 3.12.10](https://www.python.org/downloads/release/python-31210/)

2. **Internet connection** – the script installs any Python packages it needs.

## HOW TO USE

1. Extract this zip to a folder.

2. Place your Fenix announcement folder (e.g. `EWG`) next to the script.  
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
✔ Copy them into:  
➤ `export/YourFolderName/Sounds/Cabin/`

6. You are then simply required to copy the resulting airline folder (e.g. `EWG`) into:

`%AppData%\Microsoft Flight Simulator 2024\Packages\Community\fsl-a32x-airline-packs\`

## NOTES

- The script performs **case-insensitive** matching of tags and filenames.

- If multiple matches are found for a file, you will be prompted to select which one to use.

- The script will **only notify you of matches**, not any files that were not matched.

- If the pack has pre-safety demos for morning, afternoon, and evening, you will still be asked  
to match for a generic one — choose any you wish.

- For full disclosure, this script is mainly AI generated, I have tested it in many cases with no issues. Use at your own will.

## TROUBLESHOOTING

- If the script opens and closes instantly:  
  - Right-click > Open with > Python  
  - Or run from Command Prompt for better visibility

## License

This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0).

You are free to:

- Share — copy and redistribute the material in any medium or format  
- Adapt — remix, transform, and build upon the material

Under the following terms:

- Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made.  
- NonCommercial — You may not use the material for commercial purposes.
- ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

For more details, see the [full license text](https://creativecommons.org/licenses/by-nc-sa/4.0/).
