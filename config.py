"""
Konfigurasi aplikasi Rainfall Clustering Dashboard
"""

# API Configuration
GEMINI_API_KEY_PLACEHOLDER = "YOUR_GEMINI_API_KEY_HERE"

# Color Schemes
CLUSTER_COLORS = {
    1: "#FF6B6B",  # Red - Cluster 1
    2: "#4ECDC4",  # Teal - Cluster 2
    3: "#45B7D1",  # Blue - Cluster 3
}

CLUSTER_NAMES = {
    1: "Cluster 1",
    2: "Cluster 2",
    3: "Cluster 3",
}

# Rainfall Intensity Classification (mm/hari)
RAINFALL_INTENSITY = {
    "No Rain": (0, 0.5),
    "Light": (0.5, 20),
    "Moderate": (20, 50),
    "Heavy": (50, 100),
    "Very Heavy": (100, 150),
    "Extreme": (150, float('inf')),
}

INTENSITY_COLORS = {
    "No Rain": "#E8E8E8",
    "Light": "#A8E6CF",
    "Moderate": "#FFD93D",
    "Heavy": "#FF6B6B",
    "Very Heavy": "#C44569",
    "Extreme": "#8B0000",
}

# Map Configuration
JATIM_CENTER = [-7.5, 112.0]
JATIM_ZOOM = 8

# Koordinat untuk setiap wilayah (lat, lon)
COORDINATES = {
    "Kabupaten Bangkalan": (-7.0458, 112.7394),
    "Kabupaten Banyuwangi": (-8.2193, 114.3691),
    "Kabupaten Blitar": (-8.0983, 112.1681),
    "Kabupaten Bojonegoro": (-7.1502, 111.8817),
    "Kabupaten Bondowoso": (-7.9138, 113.8206),
    "Kabupaten Gresik": (-7.1554, 112.6540),
    "Kabupaten Jember": (-8.1720, 113.6984),
    "Kabupaten Jombang": (-7.5460, 112.2330),
    "Kabupaten Kediri": (-7.8484, 112.0184),
    "Kabupaten Lamongan": (-7.1170, 112.4170),
    "Kabupaten Lumajang": (-8.1335, 113.2246),
    "Kabupaten Madiun": (-7.6298, 111.6701),
    "Kabupaten Magetan": (-7.6407, 111.3404),
    "Kabupaten Malang": (-8.1663, 112.7075),
    "Kabupaten Mojokerto": (-7.4664, 112.4338),
    "Kabupaten Nganjuk": (-7.6050, 111.9046),
    "Kabupaten Ngawi": (-7.4040, 111.4460),
    "Kabupaten Pacitan": (-8.2050, 111.0920),
    "Kabupaten Pamekasan": (-7.1568, 113.4746),
    "Kabupaten Pasuruan": (-7.6453, 112.9075),
    "Kabupaten Ponorogo": (-7.8660, 111.4610),
    "Kabupaten Probolinggo": (-7.7543, 113.2159),
    "Kabupaten Sampang": (-7.1847, 113.2391),
    "Kabupaten Sidoarjo": (-7.4478, 112.7183),
    "Kabupaten Situbondo": (-7.7063, 114.0096),
    "Kabupaten Sumenep": (-7.0166, 113.8559),
    "Kabupaten Trenggalek": (-8.0501, 111.7097),
    "Kabupaten Tuban": (-6.8978, 111.9560),
    "Kabupaten Tulungagung": (-8.0658, 111.9028),
    "Kota Batu": (-7.8698, 112.5276),
    "Kota Blitar": (-8.0983, 112.1681),
    "Kota Kediri": (-7.8167, 112.0167),
    "Kota Madiun": (-7.6298, 111.5239),
    "Kota Malang": (-7.9797, 112.6304),
    "Kota Mojokerto": (-7.4725, 112.4338),
    "Kota Pasuruan": (-7.6453, 112.9075),
    "Kota Probolinggo": (-7.7543, 113.2159),
    "Kota Surabaya": (-7.2393, 112.7362),
}

# Theme Configuration
THEME_CONFIG = {
    "light": {
        "backgroundColor": "#FFFFFF",
        "secondaryBackgroundColor": "#F0F2F6",
        "textColor": "#262730",
        "primaryColor": "#FF4B4B",
    },
    "dark": {
        "backgroundColor": "#0E1117",
        "secondaryBackgroundColor": "#262730",
        "textColor": "#FAFAFA",
        "primaryColor": "#FF4B4B",
    }
}
