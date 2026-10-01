

    
# %% create directory

from pathlib import Path

base_path = Path(r"F:\OneDrive - Uniklinik RWTH Aachen\EMKA\data")

all_numbers = list(range(4, 39)) + list(range(60, 70))

for i in all_numbers:
    folder_name = f"ZC{i:02d}"
    (base_path / folder_name).mkdir(exist_ok=True)

# %% cpu

import os

# number of CPU threads
os.cpu_count()
    # Out[1]: 24

# %% number of files.

from pathlib import Path

folder_path = Path(r"F:\temp\14")
# folder = Path(r"F:\OneDrive - Uniklinik RWTH Aachen\dl\segmentation\crops")
# \manual_mask\total\geojson"

# %%% including subdirectories

# Count all files, including those in subdirectories
num_files = sum(1 
                for item in folder_path.rglob("*") 
                if item.is_file())

num_files
# print(f"Total number of files: {num_files}")

# %%% not including subdirectories

# does not count files inside subdirectories.

file_count = sum(1 
                 for item in folder_path.iterdir() 
                 if item.is_file())

print(f"Number of files: {file_count}")

# %% rename

from pathlib import Path
import re

# %%%'

# Folder containing the PNG files
folder = Path(r"F:\OneDrive - Uniklinik RWTH Aachen\dl\segmentation\crops\rename")

for file in folder.glob("*.png"):

    old_name = file.stem      # filename without extension
    ext = file.suffix

    new_name = old_name

    # ------------------------------------------------------------
    # 1. Remove '1' immediately after an opening parenthesis: (1 -> (
    # ------------------------------------------------------------
    new_name = re.sub(r"\(1", "(", new_name)

    # ------------------------------------------------------------
    # 2. Remove x=<number> or y=<number>
    #    (also removes any preceding spaces/commas)
    # ------------------------------------------------------------
    new_name = re.sub(r'[\s,]*[xy]\s*=\s*-?\d+(?:\.\d+)?', '', new_name)

    # ------------------------------------------------------------
    # 3. Replace spaces, commas, and parentheses with underscores
    # ------------------------------------------------------------
    new_name = re.sub(r'[ ,()]', '_', new_name)

    # ------------------------------------------------------------
    # 4. Reduce 3 or more consecutive underscores to exactly 2
    # ------------------------------------------------------------
    new_name = re.sub(r'_{3,}', '__', new_name)

    # Rename only if needed
    if new_name != old_name:
        new_path = file.with_name(new_name + ext)

        print(f"{file.name}  -->  {new_path.name}")
        file.rename(new_path)


# %%%'

# this renames the .geojson files from the easy & torcuous segmentations, to be similar.

from pathlib import Path

folder_path = Path(r'F:\OneDrive - Uniklinik RWTH Aachen\dl\segmentation\crops\rename\manual_mask\rest')

for file_path in folder_path.glob('*.geojson'):
    if '___' in file_path.name:      #  final_
        # Remove 'overlay' from the filename
        new_name = file_path.name.replace('___', '__')    #  ('final_', '')
        new_path = file_path.with_name(new_name)
        file_path.rename(new_path)
        # print(f"Renamed: {file_path.name} -> {new_name}")

# %%'

