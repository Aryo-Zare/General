

    
# %% create directory

from pathlib import Path

base_path = Path(r"F:\OneDrive - Uniklinik RWTH Aachen\EMKA\data")

all_numbers = list(range(4, 39)) + list(range(60, 70))

for i in all_numbers:
    folder_name = f"ZC{i:02d}"
    (base_path / folder_name).mkdir(exist_ok=True)

# %%'

