import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import os

# cek folder kerja python
print("Current Folder:", os.getcwd())

# load shapefile world map
world = gpd.read_file(r"C:\Users\usr\Documents\Damage Road\tambahan\ne_110m_admin_0_countries.shp")

# ambil negara Indonesia
indo = world[world["ADMIN"] == "Indonesia"]

# daftar kota yang disesuaikan dengan permintaan
# catatan:
# - "Bannjarmasin" diasumsikan = Banjarmasin
# - "Makasar" diasumsikan = Makassar
# - "Sumba" bukan nama kota, jadi dipakai titik representatif Waingapu (Sumba Timur)
cities = pd.DataFrame({
    "city": [
        "Banda Aceh",
        "Bandar Lampung",
        "Bandung",
        "Banjarmasin",
        "Jakarta",
        "Jambi",
        "Makassar",
        "Padang",
        "Palembang",
        "Palu",
        "Pekanbaru",
        "Pematangsiantar",
        "Pontianak",
        "Semarang",
        "Sukabumi",
        "Sumba"
    ],
    "lat": [
        5.5483,
        -5.4292,
        -6.9175,
        -3.3186,
        -6.2088,
        -1.6101,
        -5.1477,
        -0.9471,
        -2.9761,
        -0.8917,
        0.5071,
        2.9595,
        -0.0263,
        -6.9667,
        -6.9271,
        -9.6567
    ],
    "lon": [
        95.3238,
        105.2610,
        107.6191,
        114.5944,
        106.8456,
        103.6131,
        119.4327,
        100.4172,
        104.7754,
        119.8707,
        101.4478,
        99.0687,
        109.3425,
        110.4167,
        106.9287,
        120.2641
    ]
})

LABEL_SIZE = 12

# plot peta
fig, ax = plt.subplots(figsize=(12, 8))
indo.plot(ax=ax, color="lightgray", edgecolor="black")

# plot titik kota
ax.scatter(
    cities["lon"],
    cities["lat"],
    color="red",
    s=80,
    label="Dataset Location",
    zorder=3
)

# offset label biasa untuk kota lain
normal_offsets = {
    "Banda Aceh": (0.20, 0.12),
    "Bandar Lampung": (0.18, 0.10),
    "Banjarmasin": (0.15, 0.10),
    "Jambi": (0.15, 0.12),
    "Makassar": (0.12, 0.10),
    "Padang": (0.14, 0.10),
    "Palembang": (0.15, 0.10),
    "Palu": (0.15, 0.10),
    "Pekanbaru": (0.15, 0.10),
    "Pematangsiantar": (0.15, 0.10),
    "Pontianak": (0.15, 0.10),
    "Semarang": (0.15, 0.10),
    "Sumba": (0.12, 0.10),
}

for _, row in cities.iterrows():
    city = row["city"]
    x = row["lon"]
    y = row["lat"]

    # Callout khusus untuk kota yang berdekatan di Pulau Jawa
    if city == "Sukabumi":
        ax.annotate(
            "Sukabumi",
            xy=(x, y),
            xytext=(100.5, -10.7),
            fontsize=LABEL_SIZE,
            ha="center",
            va="center",
            arrowprops=dict(
                arrowstyle="->",
                color="black",
                lw=1.4,
                connectionstyle="angle3,angleA=0,angleB=90"
            ),
            zorder=5
        )
    elif city == "Bandung":
        ax.annotate(
            "Bandung",
            xy=(x, y),
            xytext=(108.8, -11.2),
            fontsize=LABEL_SIZE,
            ha="center",
            va="center",
            arrowprops=dict(
                arrowstyle="->",
                color="black",
                lw=1.4,
                connectionstyle="angle3,angleA=180,angleB=90"
            ),
            zorder=5
        )
    elif city == "Jakarta":
        ax.annotate(
            "Jakarta",
            xy=(x, y),
            xytext=(100.8, -9.6),
            fontsize=LABEL_SIZE,
            ha="center",
            va="center",
            arrowprops=dict(
                arrowstyle="->",
                color="black",
                lw=1.4,
                connectionstyle="angle3,angleA=0,angleB=90"
            ),
            zorder=5
        )
    else:
        dx, dy = normal_offsets.get(city, (0.15, 0.10))
        ax.text(
            x + dx,
            y + dy,
            city,
            fontsize=LABEL_SIZE,
            zorder=4
        )

# legend
ax.legend(loc="upper right", fontsize=12)

# judul
ax.set_title("Dataset Locations of Road Damage Images in Indonesia", fontsize=16)

# perbesar area bawah supaya callout terlihat penuh
ax.set_xlim(94, 142)
ax.set_ylim(-12.5, 7.5)

# hilangkan axis agar mirip figure paper
ax.set_axis_off()

# simpan gambar
plt.savefig("dataset_map_callout_jakarta.png", dpi=300, bbox_inches="tight")
plt.show()
