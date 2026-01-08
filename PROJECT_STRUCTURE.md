# 📂 PROJECT STRUCTURE

Dokumentasi lengkap struktur folder dan file dalam projek Rainfall Clustering Dashboard.

---

## 📁 Directory Tree

```
clusteringcmedoid/
├── 📄 app.py                          # Main application file (1,200 lines)
├── 📄 config.py                       # Configuration & constants
├── 📄 requirements.txt                # Python dependencies
├── 📄 runtime.txt                     # Python version for deployment
├── 📄 .gitignore                      # Git ignore rules
│
├── 📁 .streamlit/                     # Streamlit configuration
│   ├── config.toml                    # Theme & server settings
│   └── secrets.toml                   # API keys (not in Git)
│
├── 📁 data_curah_hujan/               # Raw data files (38 files)
│   ├── kab bangkalan.csv             # Per-region NASA POWER data
│   ├── kab banyuwangi.csv
│   ├── ... (36 more files)
│   └── kota surabaya.csv
│
├── 📁 clustering_output/              # Clustering results (15 files)
│   ├── hasil_cluster_final.csv        # Final cluster assignment
│   ├── statistik_boxplot_per_cluster_*.csv
│   ├── rata_rata_provinsi_per_tahun_*.csv
│   ├── rata_rata_tahun_x_cluster_*.csv
│   ├── ringkasan_evaluasi_fcm.csv     # Evaluation metrics
│   ├── ringkasan_tuning_m_c3.csv
│   ├── tabel_fungsi_objektif_per_iterasi.csv
│   ├── tabel_keanggotaan_akhir_c3_m*.csv  # Membership degrees
│   ├── tabel_keanggotaan_awal_c3_m*.csv
│   ├── tabel_pusat_cluster_c3_m*.csv  # Medoid information
│   └── data_boxplot_jarak_ke_medoid.csv
│
├── 📁 data_understanding/             # Data quality reports (7 files)
│   ├── deskripsi_variabel.csv         # Variable descriptions
│   ├── kelengkapan_data_per_wilayah.csv
│   ├── missing_value_per_kolom.csv
│   ├── outlier_ekstrem.csv
│   ├── outlier_per_wilayah.csv
│   ├── statistik_deskriptif_overall.csv
│   └── statistik_deskriptif_per_wilayah.csv
│
├── 📁 dtw_output/                     # DTW analysis results (3 files)
│   ├── data_pivot_daily.csv
│   ├── dtw_matrix.csv                 # Distance matrix
│   └── hasil_tuning_fcm_dtw.csv
│
├── 📁 docs/                           # Documentation files
│   ├── 📄 README.md                   # Main documentation
│   ├── 📄 INSTALLATION.md             # Installation guide
│   ├── 📄 FEATURES.md                 # Features documentation
│   ├── 📄 PROJECT_STRUCTURE.md        # This file
│   ├── 📄 USER_GUIDE.md               # User manual
│   ├── 📄 DEPLOYMENT.md               # Deployment guide
│   ├── 📄 QUICKSTART.md               # Quick deploy guide
│   └── 📁 screenshots/                # Application screenshots
│       ├── dashboard.png
│       ├── map.png
│       ├── chatbot.png
│       └── timeseries.png
│
├── 📄 data_curah_hujan_clean.csv      # Main cleaned dataset (41,650 rows)
├── 📄 hasil_cluster_final.csv         # Cluster assignments
├── 📄 ringkasan_evaluasi_fcm.csv      # Evaluation summary
│
└── 📁 .venv/                          # Virtual environment (not in Git)
    └── ... (Python packages)
```

---

## 📄 Core Files

### app.py
**Purpose**: Main Streamlit application  
**Size**: ~1,200 lines  
**Structure**:
```python
# Imports (50 lines)
import streamlit as st
import pandas as pd
import plotly.express as px
# ... more imports

# Page Config (30 lines)
st.set_page_config(...)
st.markdown("""<style>...</style>""")  # Custom CSS

# Data Loading (50 lines)
@st.cache_data
def load_data():
    # Load 10+ CSV files
    # Merge & process
    return data

# Sidebar (100 lines)
with st.sidebar:
    # Navigation
    # Filters
    # API key input
    # Theme toggle

# Page Routing (950+ lines)
if page == "Dashboard":
    # 150 lines
elif page == "Interactive Map":
    # 120 lines
elif page == "AI Chatbot":
    # 180 lines
# ... 6 more pages

# Footer (20 lines)
```

**Key Functions**:
- `load_data()` - Load & cache all datasets
- No other functions (all inline code)

### config.py
**Purpose**: Configuration & constants  
**Size**: ~150 lines  
**Contents**:
```python
# API Configuration
GEMINI_API_KEY_PLACEHOLDER = "..."

# Color Schemes
CLUSTER_COLORS = {1: "#FF6B6B", ...}
CLUSTER_NAMES = {1: "Cluster 1 (Kediri)", ...}

# Rainfall Classification
RAINFALL_INTENSITY = {...}
INTENSITY_COLORS = {...}

# Geographic Coordinates (38 locations)
COORDINATES = {
    "Kabupaten Bangkalan": (-7.0458, 112.7394),
    ...
}

# Map Settings
JATIM_CENTER = [-7.5, 112.0]
JATIM_ZOOM = 8

# Theme Configuration
THEME_CONFIG = {...}
```

### requirements.txt
**Purpose**: Python dependencies  
**Contents**:
```txt
streamlit>=1.31.0
pandas>=2.2.0
numpy>=1.26.0
plotly>=5.18.0
folium>=0.15.0
streamlit-folium>=0.16.0
google-generativeai>=0.3.0
openpyxl>=3.1.0
scikit-learn>=1.4.0
scipy>=1.12.0
seaborn>=0.13.0
matplotlib>=3.8.0
Pillow>=10.0.0
```

---

## 📊 Data Files

### Main Dataset

#### data_curah_hujan_clean.csv
**Description**: Main cleaned dataset  
**Rows**: 41,650  
**Columns**: 7
```
YEAR         : 2022-2024
MO           : 1-12 (month)
DY           : 1-31 (day)
PRECTOTCORR  : Rainfall (mm/day)
Wilayah      : Region name
tanggal      : Date (YYYY-MM-DD)
nama_bulan   : Month name (Indonesian)
```

**Sample**:
```csv
YEAR,MO,DY,PRECTOTCORR,Wilayah,tanggal,nama_bulan
2022,1,1,10.05,Kabupaten Bangkalan,2022-01-01,January
2022,1,2,7.62,Kabupaten Bangkalan,2022-01-02,January
```

**Size**: ~3.5 MB

### Raw Data (38 files)

#### data_curah_hujan/*.csv
**Format**: NASA POWER format  
**Structure**:
```csv
-BEGIN HEADER-
NASA/POWER Source...
Dates: 01/01/2022 through 12/31/2024
Location: latitude X longitude Y
...
-END HEADER-
YEAR,MO,DY,PRECTOTCORR
2022,1,1,10.05
```

**Files**: 38 (one per region)  
**Total Size**: ~5 MB

---

## 🎯 Clustering Output Files

### Cluster Assignment

#### hasil_cluster_final.csv
**Rows**: 38 (one per region)  
**Columns**: 2
```csv
Wilayah,Cluster
Kabupaten Bangkalan,1
Kabupaten Banyuwangi,1
...
```

### Membership Degrees

#### tabel_keanggotaan_akhir_c3_m2.5.csv
**Description**: Fuzzy membership values  
**Rows**: 38  
**Columns**: 5
```csv
Kabupaten/Kota,cluster_1,cluster_2,cluster_3,Cluster
Kabupaten Bangkalan,0.4076,0.3422,0.2501,1
```

**Note**: Membership values sum to 1.0

### Statistics

#### statistik_boxplot_per_cluster_*.csv
**Description**: Statistical summary per cluster  
**Rows**: 3 (one per cluster)  
**Columns**: 9
```csv
Cluster,count,mean,median,std,min,max,Q1,Q3
1,18632,5.72,2.35,9.78,0.0,173.92,0.15,7.86
```

### Evaluation

#### ringkasan_evaluasi_fcm.csv
**Description**: Model evaluation metrics  
**Rows**: 3 (different m values)  
**Columns**: 9
```csv
c,m,J,XieBeni,Iterations,Converged,n_init,max_iter,tol
3,2.5,893.67,0.2721,2,True,15,300,1e-05
```

---

## 📁 Folder Purposes

### .streamlit/
**Purpose**: Streamlit configuration  
**Files**:
- `config.toml` - Theme colors, server settings
- `secrets.toml` - API keys (user-created, not in Git)

**Example config.toml**:
```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#0E1117"
secondaryBackgroundColor = "#262730"
textColor = "#FAFAFA"
font = "sans serif"

[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = true
```

### clustering_output/
**Purpose**: Results from FCM algorithm  
**Generated By**: Clustering analysis script (not included)  
**Used By**: app.py for visualizations  
**Contents**:
- Cluster assignments
- Membership degrees (fuzzy values)
- Medoid locations
- Distance matrices
- Evaluation metrics
- Statistical summaries

### data_understanding/
**Purpose**: Data quality & exploration reports  
**Generated By**: Data preprocessing script  
**Used By**: App for outlier analysis, stats display  
**Contents**:
- Variable descriptions
- Missing value analysis
- Outlier detection results
- Descriptive statistics

### dtw_output/
**Purpose**: Dynamic Time Warping analysis  
**Note**: Optional, untuk advanced time series analysis  
**Contents**:
- DTW distance matrix
- Tuning results untuk DTW-based clustering

---

## 🔄 Data Flow

```
┌─────────────────────────────────────────────┐
│  Raw Data (NASA POWER)                      │
│  data_curah_hujan/*.csv                     │
│  38 files × 1,096 rows = 41,648 records     │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  Data Preprocessing   │
        │  - Cleaning           │
        │  - Validation         │
        │  - Feature extraction │
        └──────────┬────────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  Cleaned Dataset      │
        │  data_curah_hujan_    │
        │  clean.csv            │
        └──────────┬────────────┘
                   │
        ┌──────────┴─────────────┐
        │                        │
        ▼                        ▼
┌───────────────┐      ┌────────────────────┐
│ Data Quality  │      │ Clustering (FCM)   │
│ Analysis      │      │ - Fuzzy C-Medoid   │
│               │      │ - m tuning         │
│ Output:       │      │ - Evaluation       │
│ data_under    │      │                    │
│ standing/     │      │ Output:            │
└───────────────┘      │ clustering_output/ │
                       └─────────┬──────────┘
                                 │
                       ┌─────────┴──────────┐
                       │                    │
                       ▼                    ▼
              ┌────────────────┐  ┌────────────────┐
              │ Cluster Results│  │ Evaluation     │
              │ hasil_cluster_ │  │ Metrics        │
              │ final.csv      │  │ ringkasan_     │
              └────────┬───────┘  │ evaluasi.csv   │
                       │          └────────────────┘
                       │
                       ▼
              ┌────────────────────────┐
              │   Streamlit App        │
              │   app.py               │
              │                        │
              │   Features:            │
              │   - Visualizations     │
              │   - AI Chatbot         │
              │   - Interactive Map    │
              │   - Data Explorer      │
              └────────────────────────┘
```

---

## 🎨 Code Organization

### app.py Structure

```python
# ===== IMPORTS =====
# Standard library
from datetime import datetime
import io

# Data science
import pandas as pd
import numpy as np

# Visualization
import plotly.express as px
import plotly.graph_objects as go
import folium
import seaborn as sns

# Streamlit
import streamlit as st
from streamlit_folium import st_folium

# AI
import google.generativeai as genai

# Config
from config import *


# ===== PAGE CONFIGURATION =====
st.set_page_config(...)


# ===== CUSTOM CSS =====
st.markdown("""<style>...</style>""")


# ===== DATA LOADING FUNCTION =====
@st.cache_data
def load_data():
    """Load all CSV files and prepare data"""
    data = {}
    # Load 10+ CSV files
    # Process & merge
    return data


# ===== LOAD DATA =====
try:
    data = load_data()
    df = data['main']
except Exception as e:
    st.error(f"Error: {e}")
    st.stop()


# ===== SIDEBAR =====
with st.sidebar:
    # Logo & title
    # Navigation radio button
    # Filters (date, cluster, wilayah)
    # Theme toggle
    # API key input
    # Info section


# ===== DATA FILTERING =====
df_filtered = df[
    (conditions) &
    (more conditions)
]


# ===== PAGE ROUTING =====

# Dashboard
if page == "🏠 Dashboard":
    # Header
    # KPI metrics
    # Visualizations
    # Statistics cards

# Interactive Map
elif page == "🗺️ Interactive Map":
    # Map creation
    # Marker loops
    # Legend
    # Statistics

# AI Chatbot
elif page == "🤖 AI Chatbot":
    # API check
    # Chat interface
    # Message handling
    # AI generation

# ... (6 more pages)


# ===== FOOTER =====
st.divider()
st.markdown("""...""")
```

### Style Categories

#### CSS Classes Used
```css
.main-header         /* Page titles */
.subtitle            /* Subtitles */
.metric-card         /* KPI cards */
.chat-message        /* Chat bubbles */
.user-message        /* User messages */
.bot-message         /* AI messages */
.sidebar-content     /* Sidebar styling */
```

---

## 📦 Dependencies Graph

```
app.py
├── streamlit (core framework)
├── pandas (data manipulation)
│   └── numpy (numerical ops)
├── plotly (interactive charts)
│   └── plotly.graph_objects
│   └── plotly.express
├── folium (maps)
│   └── streamlit-folium (integration)
├── google.generativeai (AI chatbot)
├── openpyxl (Excel export)
├── scikit-learn (ML utilities)
├── scipy (scientific computing)
├── seaborn (statistical plots)
│   └── matplotlib (base plotting)
├── Pillow (image processing)
└── config (local config file)
```

---

## 🔐 Security & Sensitive Files

### Files NOT in Git (.gitignore)
```gitignore
.venv/                    # Virtual environment
__pycache__/              # Python cache
*.pyc                     # Compiled Python
.env                      # Environment variables
.streamlit/secrets.toml   # API keys ⚠️
*.log                     # Log files
.DS_Store                 # macOS files
```

### Sensitive Data
- **API Keys**: Store in `secrets.toml` or environment variables
- **Credentials**: Never commit to Git
- **Personal Info**: Remove from data files

---

## 📊 File Sizes

| Category | Count | Total Size |
|----------|-------|------------|
| Python Code | 2 | ~100 KB |
| Data Files (raw) | 38 | ~5 MB |
| Data Files (processed) | 1 | ~3.5 MB |
| Clustering Output | 15 | ~500 KB |
| Data Understanding | 7 | ~200 KB |
| Documentation | 7 | ~300 KB |
| **Total** | **70** | **~9.5 MB** |

---

## 🔧 Maintenance

### Adding New Features

**1. Add new page:**
```python
# In sidebar navigation
page = st.radio("Navigation", [
    ...,
    "🆕 New Feature"
])

# In page routing
elif page == "🆕 New Feature":
    st.header("New Feature")
    # Your code here
```

**2. Add new data file:**
```python
# In load_data() function
data['new_file'] = pd.read_csv('path/to/new_file.csv')
```

**3. Add new configuration:**
```python
# In config.py
NEW_SETTING = {
    "option1": "value1",
    "option2": "value2"
}
```

### Code Standards

- **Indentation**: 4 spaces
- **Line length**: Max 100 characters
- **Comments**: Docstrings for functions
- **Naming**: snake_case for variables/functions
- **Constants**: UPPER_CASE in config.py

---

## 📚 Related Documentation

- [README.md](README.md) - Project overview
- [INSTALLATION.md](INSTALLATION.md) - Setup guide
- [FEATURES.md](FEATURES.md) - Feature details
- [USER_GUIDE.md](USER_GUIDE.md) - Usage instructions
- [DEPLOYMENT.md](DEPLOYMENT.md) - Deploy guide

---

**Need to understand the code structure?**  
Start with `app.py` and follow the data flow from loading → filtering → visualization.
