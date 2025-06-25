import os
import sys
import subprocess
import re
from pathlib import Path

def pause_exit(msg=None):
    if msg: print(msg)
    input("\nPress Enter to exit...")
    sys.exit()

# Ensure pydub is installed
try:
    from pydub import AudioSegment
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pydub"])
    from pydub import AudioSegment

# Check ffmpeg
if subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
    pause_exit("❌ FFmpeg not found. Install it and add to PATH. https://www.wikihow.com/Install-FFmpeg-on-Windows")

# Define official FSLabs filenames
fslabs_targets = {
    "FSL_A320X_CABIN_PA_BOARDING.ogg": ["BoardingWelcome"],
    "FSL_A320X_CABIN_PA_BOARDING_MUSIC.ogg": ["BoardingMusic"],
    "FSL_A320X_CABIN_PA_BOARDING_FUEL.ogg": ["BoardingWelcome[Refueling]"],
    "FSL_A320X_CABIN_PA_BOARDING_COMPLETE.ogg": ["BoardingComplete"],
    "FSL_A320X_CABIN_PA_DOORS_AUTO.ogg": ["ArmDoors"],
    "FSL_A320X_CABIN_PA_DOORS_MANUAL.ogg": ["DisarmDoors"],
    "FSL_A320X_CABIN_PA_DISEMBARK.ogg": ["DisembarkStarted"],
    "FSL_A320X_CABIN_PA_BRIEFING.ogg": ["PreSafetyBriefing"],
    "FSL_A320X_CABIN_PA_BRIEFING_MORNING.ogg": ["PreSafetyBriefing[Morning]"],
    "FSL_A320X_CABIN_PA_BRIEFING_AFTERNOON.ogg": ["PreSafetyBriefing[Afternoon]"],
    "FSL_A320X_CABIN_PA_BRIEFING_EVENING.ogg": ["PreSafetyBriefing[Evening]"],
    "FSL_A320X_CABIN_PA_SAFETY_BRIEFING.ogg": ["SafetyBriefing"],
    "FSL_A320X_CABIN_PA_LIGHTS_DIM.ogg": ["CabinDimTakeoff"],
    "FSL_A320X_CABIN_PA_SECURE_FOR_TAKEOFF.ogg": ["CrewSeatsTakeoff"],
    "FSL_A320X_CABIN_PA_READY_TAKEOFF.ogg": ["CallCabinSecureTakeoff"],
    "FSL_A320X_CABIN_PA_AFTER_TAKEOFF.ogg": ["AfterTakeoff"],
    "FSL_A320X_CABIN_PA_TURB.ogg": ["FastenSeatbelt"],
    "FSL_A320X_CABIN_PA_SECURE_FOR_LANDING.ogg": ["CrewSeatsLanding"],
    "FSL_A320X_CABIN_PA_READY_LANDING.ogg": ["CallCabinSecureLanding"],
    "FSL_A320X_CABIN_PA_AFTER_LANDING.ogg": ["AfterLanding"],
    "FSL_A320X_CABIN_PA_SEATBELTS.ogg": ["DescentSeatbelts"],
}

# Select folder
script_dir = Path(__file__).parent
subfolders = [f for f in script_dir.iterdir() if f.is_dir() and f.name.lower() not in ["export", "__pycache__"]]
if not subfolders: pause_exit("❌ No folders found next to this script.")
print("📁 Available folders:")
for i, f in enumerate(subfolders, 1): print(f"{i}. {f.name}")
try:
    folder = subfolders[int(input("\nEnter number of folder to process: ")) - 1]
except: pause_exit("Invalid selection.")

# Create export folder
export_dir = script_dir / "export" / folder.name / "Sounds" / "Cabin"
export_dir.mkdir(parents=True, exist_ok=True)

# Index all available .ogg files
all_files = list(folder.glob("*.ogg"))
# Create a dict with lowercase stems for case-insensitive lookup
file_map = {f.stem.lower(): f for f in all_files}

# Helper to find possible matches case-insensitively
def find_possible_matches(key):
    # Remove tags inside brackets (case-insensitive)
    simplified = re.sub(r"\[.*?\]", "", key, flags=re.IGNORECASE).lower()
    return [f for f in all_files if simplified in f.stem.lower()]

# Convert files
converted = 0
for fsl_name, fenix_keys in fslabs_targets.items():
    candidates = []
    for k in fenix_keys:
        k_lower = k.lower()
        if k_lower in file_map:
            candidates = [file_map[k_lower]]
            break
        else:
            # Match if k (case-insensitive) is contained in file stem (also case-insensitive)
            candidates += [f for f in all_files if k_lower in f.stem.lower()]

    if not candidates:
        # Suppressed warning about no match as requested
        continue

    chosen = candidates[0]
    if len(candidates) > 1:
        print(f"\nMultiple options found for {fsl_name}:")
        for i, f in enumerate(candidates, 1):
            print(f" {i}. {f.name}")
        try:
            idx = int(input(f"Select file (1-{len(candidates)}) or press Enter to skip: "))
            chosen = candidates[idx - 1]
        except:
            print("❌ Skipped.")
            continue

    print(f"✅ {chosen.name} → {fsl_name}")
    AudioSegment.from_ogg(chosen).export(export_dir / fsl_name, format="ogg")
    converted += 1

print(f"\n🎉 Done! {converted} files converted.")
print(f"➡ Output folder: {export_dir.resolve()}")
pause_exit()
