# 🌧️ Rainfall Clustering Dashboard - Jawa Timur

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Production-success.svg)

**Aplikasi Web Interaktif untuk Visualisasi dan Analisis Data Clustering Curah Hujan**

[📖 Dokumentasi](#-dokumentasi) • [🚀 Quick Start](#-quick-start) • [✨ Features](#-features) • [📊 Demo](#-demo) • [🤝 Contributing](#-contributing)

</div>

---

## 📋 Daftar Isi

- [Tentang Projek](#-tentang-projek)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Quick Start](#-quick-start)
- [Dokumentasi](#-dokumentasi)
- [Data Overview](#-data-overview)
- [Screenshots](#-screenshots)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Tentang Projek

**Rainfall Clustering Dashboard** adalah aplikasi web berbasis Streamlit yang menyediakan analisis mendalam tentang pola curah hujan di 38 Kabupaten/Kota Jawa Timur menggunakan algoritma **Fuzzy C-Medoid (FCM)**.

### 🎓 Latar Belakang

Curah hujan merupakan parameter penting untuk:
- 🌾 Perencanaan pertanian
- 💧 Manajemen sumber daya air
- 🌊 Mitigasi bencana banjir dan kekeringan
- 📊 Analisis perubahan iklim

Aplikasi ini memvisualisasikan hasil clustering 3 tahun data curah hujan (2022-2024) dari NASA POWER untuk membantu stakeholder dalam pengambilan keputusan.

### 🎯 Tujuan

1. Mengidentifikasi pola curah hujan regional di Jawa Timur
2. Mengelompokkan wilayah dengan karakteristik curah hujan serupa
3. Menyediakan insight berbasis AI untuk analisis prediktif
4. Memfasilitasi eksplorasi data interaktif dan user-friendly

---

## ✨ Features

### 🏠 Dashboard Overview
- 📊 4 KPI Cards (Wilayah, Periode, Avg Rainfall, Clusters)
- 📈 Box Plot distribusi per cluster
- 🥧 Pie Chart komposisi cluster
- 📉 Time series trend bulanan
- 💳 Statistics cards untuk 3 cluster

### 🗺️ Interactive Map
- 🌏 Peta Jawa Timur dengan 38 marker geografis
- 🎨 Color-coded berdasarkan cluster (Red, Teal, Blue)
- 📍 Circle markers proporsional dengan rata-rata curah hujan
- 💬 Tooltip hover & popup detail statistik
- 🏷️ Legend interaktif dengan shadow effect

### 🤖 AI Chatbot (Google Gemini)
- 💬 Natural language chat interface
- 🧠 Context-aware dengan 100+ data points
- 📚 Pengetahuan mendalam: statistik, trend, cluster, wilayah
- 💾 Chat history management
- 🔄 Multi-model fallback (Gemini 2.5 Flash/Pro)
- 📊 Rekomendasi berbasis data aktual

### 📈 Time Series Analysis
- 📊 Line chart curah hujan harian multi-wilayah
- 📅 Monthly average bar chart
- 🔄 Dynamic legend & hover unified
- 🎯 Filter wilayah dengan multi-select

### 🎯 Cluster Analysis
- 📊 Membership degree stacked bar chart
- 📏 Distance to medoid box plot
- 🎲 3D scatter plot (Mean × Std × Max)
- 🔄 Interactive rotation & zoom
- 📌 Cluster characterization cards

### 🌧️ Rainfall Analytics
- 🔥 Heatmap distribusi bulanan (Tahun × Bulan)
- ⚠️ Extreme events detection (>100mm) dengan table
- ☀️ Drought days analysis (<1mm) per wilayah
- 🎨 Pie chart intensity classification (6 kategori)
- 📊 Top 10 wilayah dengan hari kering terbanyak

### 📊 Statistical Dashboard
- 🎻 Violin plot per cluster dengan box overlay
- 📊 Histogram distribusi frekuensi multi-cluster
- 🚨 Outlier analysis bar chart top 15 wilayah
- 🔗 Correlation matrix antar wilayah (heatmap)
- 📈 Summary statistics table

### 🔍 Data Explorer
- 🔎 Search & filter (wilayah, rainfall range, tanggal)
- 📋 Interactive datatable dengan sorting & pagination
- 💾 Download CSV & Excel dengan 1 klik
- 📊 Real-time summary statistics
- 🔢 Record counter

### 📉 Performance Metrics
- 🎯 3 KPI metrics (c, m, Xie-Beni)
- 📊 Bar chart parameter tuning comparison
- 📈 Line chart objective function convergence
- 📋 Detailed evaluation table
- 💡 Key insights & recommendations

### 🎨 Advanced UI/UX
- 🌓 Dark/Light theme toggle
- 🎨 Modern gradient & glassmorphism effects
- ✨ Smooth CSS animations
- 📱 Fully responsive design
- 🖼️ Custom styling dengan 500+ lines CSS
- 🚀 Optimized loading dengan caching

---

## 🛠️ Tech Stack

### Frontend & Framework
- **Streamlit** `1.31+` - Main web framework
- **Plotly** `5.18+` - Interactive visualizations
- **Folium** `0.15+` - Interactive maps
- **Streamlit-Folium** `0.16+` - Folium integration

### Data Processing
- **Pandas** `2.2+` - Data manipulation
- **NumPy** `1.26+` - Numerical computing
- **Scikit-learn** `1.4+` - Machine learning utilities
- **SciPy** `1.12+` - Scientific computing

### Visualization
- **Seaborn** `0.13+` - Statistical plots
- **Matplotlib** `3.8+` - Base plotting
- **Pillow** `10.0+` - Image processing

### AI & Integration
- **Google Generative AI** `0.3+` - Gemini chatbot
- **OpenPyXL** `3.1+` - Excel export

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11 atau lebih tinggi
- pip (Python package manager)
- Git (optional)

### Installation

**1. Clone Repository**
```bash
git clone https://github.com/username/rainfall-clustering-dashboard.git
cd rainfall-clustering-dashboard
```

**2. Create Virtual Environment (Recommended)**
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Run Application**
```bash
streamlit run app.py
```

**5. Open Browser**
```
http://localhost:8501
```

### 🔑 Setup Gemini API (Optional)

1. Dapatkan API Key gratis: https://aistudio.google.com/app/apikey
2. Masukkan di sidebar aplikasi
3. Atau set di `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "your_api_key_here"
```

---

## 📖 Dokumentasi

| Dokumen | Deskripsi |
|---------|-----------|
| [📥 INSTALLATION.md](INSTALLATION.md) | Panduan instalasi lengkap step-by-step |
| [✨ FEATURES.md](FEATURES.md) | Dokumentasi detail setiap fitur |
| [📂 PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) | Struktur file & folder projek |
| [👤 USER_GUIDE.md](USER_GUIDE.md) | Panduan penggunaan untuk end-user |
| [🚀 DEPLOYMENT.md](DEPLOYMENT.md) | Panduan deployment ke berbagai platform |
| [⚡ QUICKSTART.md](QUICKSTART.md) | Quick deploy ke Streamlit Cloud |

---

## 📊 Data Overview

### 📁 Dataset
- **Sumber**: NASA POWER (Precipitation Corrected)
- **Periode**: 1 Januari 2022 - 31 Desember 2024 (1,096 hari)
- **Wilayah**: 38 Kabupaten/Kota Jawa Timur
- **Total Records**: 41,650 data points
- **Format**: CSV

### 📈 Statistik Keseluruhan
```
Rata-rata  : 5.97 mm/hari
Median     : 2.24 mm/hari
Std Dev    : 11.69 mm/hari
Minimum    : 0.00 mm/hari
Maksimum   : 318.68 mm/hari
```

### 🎯 Clustering Results
- **Algoritma**: Fuzzy C-Medoid (FCM)
- **Jumlah Cluster**: 3 (optimal)
- **Xie-Beni Index**: 0.2721 (excellent)
- **Fuzziness (m)**: 2.5 (optimal)

#### Cluster 1 (Kediri) - 18 Wilayah
- Karakteristik: Curah hujan SEDANG
- Mean: 5.72 mm/hari
- Wilayah: Pesisir utara & selatan

#### Cluster 2 (Magetan) - 8 Wilayah
- Karakteristik: Curah hujan SEDANG-TINGGI
- Mean: 6.18 mm/hari
- Wilayah: Barat Jawa Timur

#### Cluster 3 (Blitar) - 12 Wilayah
- Karakteristik: Curah hujan TINGGI
- Mean: 6.16 mm/hari
- Wilayah: Tengah & dataran tinggi

### 📁 File Structure
```
📦 Data Files
├── 📄 data_curah_hujan_clean.csv (Main dataset)
├── 📄 hasil_cluster_final.csv (Clustering results)
├── 📁 clustering_output/ (15 files)
│   ├── statistik_boxplot_per_cluster.csv
│   ├── tabel_keanggotaan_akhir_c3_m2.5.csv
│   ├── ringkasan_evaluasi_fcm.csv
│   └── ... (other analysis results)
├── 📁 data_understanding/ (7 files)
│   ├── statistik_deskriptif_overall.csv
│   ├── outlier_per_wilayah.csv
│   └── ... (data quality reports)
└── 📁 data_curah_hujan/ (38 files - raw data per region)
```

---

## 🖼️ Screenshots

### Dashboard Overview
![Dashboard](docs/screenshots/dashboard.png)
*KPI metrics, distribusi cluster, dan time series trend*

### Interactive Map
![Map](docs/screenshots/map.png)
*Peta Jawa Timur dengan marker clustering color-coded*

### AI Chatbot
![Chatbot](docs/screenshots/chatbot.png)
*Natural language chat dengan Gemini AI*

### Time Series Analysis
![Time Series](docs/screenshots/timeseries.png)
*Analisis curah hujan harian dan bulanan*

---

## 🚀 Deployment

Aplikasi ini dapat dideploy ke berbagai platform:

### 🌟 Streamlit Cloud (Recommended - FREE)
```bash
# Push to GitHub
git push origin main

# Deploy di https://share.streamlit.io/
# Pilih repo → branch → app.py → Deploy
```

### 🚂 Railway (FREE $5 Credit)
```bash
railway init
railway up
```

### 🐳 Docker
```bash
docker build -t rainfall-dashboard .
docker run -p 8501:8501 rainfall-dashboard
```

**Detail**: Lihat [DEPLOYMENT.md](DEPLOYMENT.md)

---

## 📈 Usage Examples

### Filter Data
```python
# Di sidebar
- Pilih periode: 01/01/2022 - 31/12/2024
- Pilih cluster: [1, 2, 3]
- Pilih wilayah: Kab. Malang, Kota Surabaya, ...
```

### Export Data
```python
# Di Data Explorer
1. Filter data sesuai kebutuhan
2. Klik "Download CSV" atau "Download Excel"
3. File akan otomatis terunduh
```

### Chat dengan AI
```
User: "Cluster mana yang paling rawan banjir?"
AI: "🌧️ Cluster 3 (Blitar) paling rawan banjir karena:
     - Mean rainfall tertinggi: 6.16 mm/hari
     - Variasi terbesar: Std 13.74 mm/hari
     - Extreme events: >100mm tercatat 45+ kali
     - Wilayah rawan: Kab. Malang, Kab. Blitar, Kota Batu..."
```

---

## 🔧 Configuration

### Customize Colors
Edit `config.py`:
```python
CLUSTER_COLORS = {
    1: "#FF6B6B",  # Red
    2: "#4ECDC4",  # Teal
    3: "#45B7D1",  # Blue
}
```

### Add New Coordinates
```python
COORDINATES = {
    "Kabupaten Baru": (-7.123, 112.456),
}
```

### Adjust Thresholds
```python
RAINFALL_INTENSITY = {
    "Light": (0.5, 20),
    "Moderate": (20, 50),
    # ... customize ranges
}
```

---

## 🤝 Contributing

Kontribusi sangat diterima! Ikuti langkah berikut:

1. **Fork** repository ini
2. **Create branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit** changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to branch (`git push origin feature/AmazingFeature`)
5. **Open Pull Request**

### Development Setup
```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Format code
black app.py
flake8 app.py
```

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👥 Authors

- **Developer** - [@username](https://github.com/username)
- **Data Source** - NASA POWER
- **Institution** - [Your Institution]

---

## 🙏 Acknowledgments

- **NASA POWER** - Penyedia data curah hujan
- **Streamlit** - Framework aplikasi
- **Google Gemini** - AI integration
- **OpenStreetMap** - Peta geografis
- **Komunitas Open Source** - Various libraries

---

## 📞 Support & Contact

- 📧 Email: your.email@example.com
- 💬 Discussions: [GitHub Discussions](https://github.com/username/rainfall-dashboard/discussions)
- 🐛 Issues: [GitHub Issues](https://github.com/username/rainfall-dashboard/issues)
- 📖 Docs: [Documentation](https://rainfall-dashboard.readthedocs.io)

---

## 🔗 Links

- [Live Demo](https://rainfall-dashboard.streamlit.app)
- [API Documentation](docs/API.md)
- [Changelog](CHANGELOG.md)
- [Roadmap](ROADMAP.md)

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ by Rainfall Analysis Team

[⬆ Back to Top](#-rainfall-clustering-dashboard---jawa-timur)

</div>
