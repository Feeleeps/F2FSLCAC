import os
import sys
import shutil
import re
from pathlib import Path

def pause_exit(msg=None):
    if msg: print(msg)
    input("\nPress Enter to exit...")
    sys.exit()

# Define official FSLabs filenames and their matching Fenix tags (case-insensitive matching)
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
if not subfolders:
    pause_exit("❌ No folders found next to this script.")
print("📁 Available folders:")
for i, f in enumerate(subfolders, 1):
    print(f"{i}. {f.name}")
try:
    folder = subfolders[int(input("\nEnter number of folder to process: ")) - 1]
except:
    pause_exit("Invalid selection.")

# Create export folder
export_dir = script_dir / "export" / folder.name / "Sounds" / "Cabin"
export_dir.mkdir(parents=True, exist_ok=True)

# Index all available .ogg files
all_files = list(folder.glob("*.ogg"))

converted = 0
for fsl_name, fenix_keys in fslabs_targets.items():
    candidates = []
    for k in fenix_keys:
        k_lower = k.lower()
        # Match whole word or exact stem using regex to prevent false positives (e.g., "ArmDoors" vs "DisarmDoors")
        for f in all_files:
            stem = f.stem.lower()
            if re.search(rf"\b{k_lower}\b", stem):
                candidates.append(f)

    if not candidates:
        # No match found, silently continue
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
    shutil.copy2(chosen, export_dir / fsl_name)
    converted += 1

print(f"\n🎉 Done! {converted} files copied.")
print(f"➡ Output folder: {export_dir.resolve()}")
pause_exit()
