import os
import xml.etree.ElementTree as ET

folder_path = r"C:\Users\usr\Documents\Damage Road\Dataset\Dataset Cluster 400km\Sumba"   
jpg_files = []
xml_files = []

low = 0
medium = 0
high = 0

# scan file
for file in os.listdir(folder_path):
    if file.lower().endswith(".jpg"):
        jpg_files.append(os.path.splitext(file)[0])
    elif file.lower().endswith(".xml"):
        xml_files.append(os.path.splitext(file)[0])

# hitung anotasi dari XML
for xml_name in xml_files:
    xml_path = os.path.join(folder_path, xml_name + ".xml")

    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        for obj in root.findall("object"):
            label = obj.find("name").text.strip().lower()

            if label == "low":
                low += 1
            elif label == "medium":
                medium += 1
            elif label == "high":
                high += 1

    except Exception as e:
        print(f"Error membaca {xml_name}.xml:", e)

# cek pasangan file
jpg_set = set(jpg_files)
xml_set = set(xml_files)

jpg_without_xml = jpg_set - xml_set
xml_without_jpg = xml_set - jpg_set

# hasil
print("===== DATASET SUMMARY =====")
print("Jumlah JPG :", len(jpg_files))
print("Jumlah XML :", len(xml_files))

print("\n===== ANNOTATION COUNT =====")
print("Low    :", low)
print("Medium :", medium)
print("High   :", high)

print("\n===== FILE CHECK =====")
print("JPG tanpa XML :", len(jpg_without_xml))
print("XML tanpa JPG :", len(xml_without_jpg))

if jpg_without_xml:
    print("\nDaftar JPG tanpa XML:")
    for f in sorted(jpg_without_xml):
        print(f + ".jpg")

if xml_without_jpg:
    print("\nDaftar XML tanpa JPG:")
    for f in sorted(xml_without_jpg):
        print(f + ".xml")
