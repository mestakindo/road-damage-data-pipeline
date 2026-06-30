# road-damage-data-pipeline
A project dedicated to consolidating, cleaning, and analyzing a multi-contributor image dataset consisting of 15,000+ images and XML annotation files for Computer Vision tasks.

> **Disclaimer:** File data mentah (raw images & XML) dan data hasil perbaikan tidak disertakan dalam repositori ini karena alasan privasi dan ukuran data yang terlalu besar. Repositori ini difokuskan untuk memamerkan alur otomatisasi program (*data pipeline scripts*), metodologi perapian data, serta visualisasi analitis.

## 📌 Project Overview
Dalam proyek kolaboratif berskala besar, pengumpulan data anotasi sering kali menghasilkan data yang tidak konsisten dan berantakan karena perbedaan standar input antar-anggota tim. Proyek ini berfokus pada **Data Preprocessing & Exploratory Data Analysis (EDA)** menggunakan pemrograman Python untuk merapikan, memvalidasi, dan menganalisis sebaran data dari 15.000+ gambar yang telah dianotasi menggunakan tools `LabelImg` (Format Pascal VOC XML).

Tantangan utama dalam proyek ini adalah menyatukan output dari banyak kontributor, mengotomatisasi perbaikan ribuan nama file yang bentrok, mendeteksi file yang hilang, serta menyajikan laporan analisis sebaran data spasial yang mudah dibaca oleh dosen dan peneliti.

## 🛠️ Tech Stack & Tools
- **Language:** Python
- **Libraries:** Pandas, NumPy, Geopandas, Matplotlib, Seaborn, ElementTree (XML Parser), OS, Re
- **Annotation Tool:** LabelImg (Pascal VOC format)

## 🗂️ Repository Structure
Repositori diatur dengan struktur standar profesional sebagai berikut:
```text
├── scripts/
│   ├── rename_automation.py  # Script otomatisasi penamaan file gambar (bulk rename)
│   ├── missing_name.py       # Script melacak nomor file yang hilang/rusak
│   ├── total_summary.py      # Script parsing XML, hitung label, & validasi sinkronisasi
│   └── map_v2.py             # Script analitik spasial & peta penyebaran data
├── presentation/
│   ├── Presentation.pdf        # File presentasi siap baca langsung di browser
├── output/
│   └── Map_v2.png               # Hasil akhir visualisasi peta penyebaran data spasial
└── README.md
```
## 🚀 Workflows & Automation Scripts
A. **Data Cleaning & File Management** 
Proses perapian data dilakukan secara terprogram untuk menghindari kesalahan manusia (human error) pada 15.000 file data:

Bulk Renaming (01_rename_automation.py): Menggunakan library os dan regex (re) untuk mengurutkan nama ribuan file secara otomatis menjadi format berurutan (1.jpg, 2.jpg, dst) menggunakan teknik temporary rename agar nama file tidak saling bentrok.

Audit File Hilang (02_missing_name.py): Script khusus untuk memindai seluruh direktori dan mendeteksi secara instan jika ada nomor urutan file gambar yang terlewat atau hilang dalam dataset.

B. **XML Parsing & Synchronization Validation**
Metadata Extraction (03_total_summary.py): Memanfaatkan library xml.etree.ElementTree untuk mengekstrak isi tag objek di dalam file XML, mengubah huruf kapital yang tidak konsisten (misal: low, LOW, atau typo diseragamkan menjadi low), serta menghitung total kemunculan label.

Sinkronisasi Pasangan Data: Script secara otomatis melakukan operasi himpunan (set operations) di Python untuk mencari file .jpg yang tidak memiliki pasangan .xml, atau sebaliknya, demi memastikan dataset 100% sinkron sebelum masuk ke tahap training model AI.

C. **Exploratory Data Analysis & Spatial Mapping**
Geospatial Analysis (04_map_v2.py): Menggunakan library tingkat lanjut geopandas untuk memetakan koordinat titik pengambilan data gambar berdasarkan shapefile wilayah administratif Indonesia, lalu memberikan visualisasi serta anotasi label nama kota secara dinamis.

## 📊 Key Results & Insights
A. **Kategorisasi Anotasi Dataset**
Seluruh objek dalam dataset 15.000 gambar berhasil divalidasi dan dikelompokkan secara konsisten ke dalam 3 kelas intensitas:

- Low: Menunjukkan tingkat kepadatan/objek rendah.
- Medium: Menunjukkan tingkat kepadatan/objek sedang.
- High: Menunjukkan tingkat kepadatan/objek tinggi.

B. **Analisis Sebaran Spasial (Peta Wilayah)**
Berdasarkan eksekusi script 04_map_v2.py yang menghasilkan output peta Map_v2.png, diperoleh temuan penting:

Distribusi data gambar tidak berpusat pada satu lokasi saja, melainkan tersebar secara klaster di berbagai kota besar di Indonesia (seperti Banda Aceh, Jakarta, Bandung, Banjarmasin, Makassar, Sumba, dll).

Tingkat kepadatan label (High/Medium/Low) sangat berkorelasi dengan faktor lingkungan geografis daerah setempat. Area perkotaan padat didominasi kelas High, sedangkan wilayah luar kota didominasi kelas Low.

## 💡 Key Deliverables & Impact
Model-Ready Dataset Pipeline: Menghasilkan alur kode otomatisasi yang mampu menyaring ribuan data berantakan menjadi dataset bersih yang siap dimasukkan ke algoritma Object Detection (seperti YOLO atau Faster R-CNN).

Data Presentation & Reporting: Menyediakan dokumen laporan profesional (presentation/) yang menerjemahkan angka-angka coding mentah menjadi bentuk insight visual grafis yang mudah dipahami oleh dosen, peneliti, maupun penguji proyek.
