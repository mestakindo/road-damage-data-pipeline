import os
import re

folder_path = r"C:\Users\usr\Documents\Damage Road Dataset\Dion\data\annotated"

# Ambil semua file (ubah ekstensi kalau bukan .jpg)
files = [f for f in os.listdir(folder_path) if f.endswith(".jpg")]

# Urutkan berdasarkan angka yang ada di nama file (jika sebelumnya sudah ada nomor)
files.sort(key=lambda x: int(re.search(r'\d+', x).group()))

# Rename sementara dulu supaya tidak bentrok
for i, filename in enumerate(files):
    old_path = os.path.join(folder_path, filename)
    temp_path = os.path.join(folder_path, f"temp_{i}.jpg")
    os.rename(old_path, temp_path)

# Rename final menjadi 1.jpg, 2.jpg, dst
temp_files = [f for f in os.listdir(folder_path) if f.startswith("temp_")]
temp_files.sort(key=lambda x: int(x.split("_")[1].split(".")[0]))

for i, filename in enumerate(temp_files, start=1):
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, f"{i}.jpg")
    os.rename(old_path, new_path)

print("Renaming selesai!")
