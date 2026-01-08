# ✨ FEATURES DOCUMENTATION

Dokumentasi lengkap semua fitur dalam Rainfall Clustering Dashboard.

---

## 📋 Table of Contents

1. [Dashboard Overview](#1--dashboard-overview)
2. [Interactive Map](#2--interactive-map)
3. [AI Chatbot](#3--ai-chatbot)
4. [Time Series Analysis](#4--time-series-analysis)
5. [Cluster Analysis](#5--cluster-analysis)
6. [Rainfall Analytics](#6--rainfall-analytics)
7. [Statistical Dashboard](#7--statistical-dashboard)
8. [Data Explorer](#8--data-explorer)
9. [Performance Metrics](#9--performance-metrics)

---

## 1. 🏠 Dashboard Overview

**Halaman utama** yang menampilkan ringkasan keseluruhan data dan insight utama.

### Features

#### 📊 KPI Metrics Cards (4 Cards)
- **Total Wilayah**: Jumlah kabupaten/kota (38)
- **Periode**: Rentang waktu data (2022-2024)
- **Average Rainfall**: Rata-rata curah hujan keseluruhan
- **Clusters**: Jumlah cluster optimal (3)

**Teknologi**: Streamlit `st.metric()` dengan delta indicators

#### 📈 Box Plot Distribution
- **Purpose**: Menampilkan distribusi curah hujan per cluster
- **Interactive**: Hover untuk detail statistik
- **Visualization**: Plotly box plot
- **Data**: Filtered berdasarkan selection di sidebar
- **Colors**: Red (Cluster 1), Teal (Cluster 2), Blue (Cluster 3)

**Features:**
- Median line (garis tengah)
- Quartile boxes (Q1-Q3)
- Whiskers (min-max excluding outliers)
- Outlier points (dots)

#### 🥧 Pie Chart Cluster Composition
- **Purpose**: Komposisi jumlah wilayah per cluster
- **Interactive**: Click legend untuk hide/show
- **Percentage**: Auto-calculated
- **Colors**: Consistent dengan cluster colors

#### 📉 Time Series Trend
- **Type**: Line chart bulanan
- **Period**: 2022-2024 (36 bulan)
- **Lines**: Satu line per cluster
- **X-axis**: Tanggal (monthly aggregated)
- **Y-axis**: Rata-rata curah hujan (mm/hari)
- **Interaction**: 
  - Hover unified (vertical line)
  - Zoom & pan
  - Download plot

#### 💳 Cluster Statistics Cards (3 Cards)
**Per cluster menampilkan:**
- Mean (rata-rata)
- Median (nilai tengah)
- Std Dev (standar deviasi)
- Max (nilai maksimum)
- Records (jumlah data points)

**Design**: Gradient glassmorphism card dengan border-left colored

---

## 2. 🗺️ Interactive Map

**Peta geografis interaktif** Jawa Timur dengan marker clustering.

### Features

#### 🌏 Base Map
- **Library**: Folium
- **Tileset**: CartoDB Positron (clean & modern)
- **Center**: -7.5°S, 112.0°E (center of Jawa Timur)
- **Initial Zoom**: 8
- **Size**: 1400×600 pixels

#### 📍 Circle Markers (38 Wilayah)
**Marker Properties:**
- **Location**: Lat/Lon coordinates dari config.py
- **Radius**: Dynamic = `10 + (mean_rainfall / 2)`
  - Semakin tinggi curah hujan, semakin besar marker
- **Color**: Border sesuai cluster
- **Fill Color**: Same as border (60% opacity)
- **Weight**: 2px border

**Example:**
```python
# Kab. Malang - Cluster 3 (Blue)
Location: (-8.1663, 112.7075)
Radius: ~13 pixels (mean 6.16 mm/hari)
Color: #45B7D1
```

#### 💬 Interactive Elements

**Tooltip (Hover):**
- Tampil saat mouse hover
- Content: Nama wilayah
- Style: Default Folium tooltip

**Popup (Click):**
- Tampil saat marker di-click
- Content HTML dengan styling:
  - Nama wilayah (colored by cluster)
  - Horizontal divider
  - Cluster name
  - Rata-rata curah hujan
  - Maksimum curah hujan
  - Total data points
- Width: 200px
- Font: Arial

#### 🏷️ Legend Box
**Properties:**
- Position: Fixed bottom-right
- Size: 220×auto pixels
- Background: White with shadow
- Border: 2px grey, 10px radius
- Z-index: 9999 (always on top)

**Content:**
- Title: "Legend:" (bold, black)
- 3 items:
  - Colored bullet (20px) + Cluster name
  - Text color: Black (#000)
  - Margin: 5px between items

#### 📊 Statistics Section
**3 Metrics di bawah peta:**
1. **Wilayah Ditampilkan**: Total markers
2. **Tertinggi**: Wilayah dengan mean tertinggi + value
3. **Terendah**: Wilayah dengan mean terendah + value

---

## 3. 🤖 AI Chatbot

**Conversational AI** powered by Google Gemini untuk analisis data natural language.

### Features

#### 💬 Chat Interface
- **Layout**: Chat-style bubbles
- **User messages**: Light teal background, left-aligned
- **AI messages**: Light blue background, left-aligned
- **Emoji**: 👤 for user, 🤖 for AI
- **Animation**: Fade-in effect on new messages

#### 🧠 AI Context (Comprehensive)
**AI memiliki pengetahuan tentang:**

1. **Dataset Overview**
   - Periode: 2022-2024 (1,096 hari)
   - 38 wilayah Jawa Timur
   - 41,650 data points
   - Sumber: NASA POWER

2. **Statistik Lengkap**
   - Mean, median, std, min, max overall
   - Stats per cluster (3 clusters)
   - Extreme events (>100mm): jumlah
   - Drought days (<1mm): jumlah

3. **Trend & Pattern**
   - Yearly averages (2022, 2023, 2024)
   - Monthly patterns (12 bulan)
   - Seasonal insights

4. **Cluster Details**
   - Medoid: Kediri (C1), Magetan (C2), Blitar (C3)
   - Daftar wilayah per cluster
   - Karakteristik tiap cluster
   - Statistik lengkap per cluster

5. **Wilayah Ranking**
   - Top 5 tertinggi
   - Top 5 terendah
   - Outlier information

6. **Evaluation Metrics**
   - Xie-Beni Index: 0.2721
   - Optimal m: 2.5
   - Convergence: 2 iterasi

7. **Insights & Recommendations**
   - Tren menurun 2022→2024
   - Wilayah rawan banjir (Cluster 3)
   - Musim hujan/kering
   - Implikasi untuk pertanian

#### 🔄 Model Fallback System
**6 model dicoba secara sequential:**
1. `models/gemini-2.5-flash` (fastest, recommended)
2. `models/gemini-2.5-pro` (most capable)
3. `models/gemini-2.0-flash-exp` (experimental)
4. `models/gemini-2.0-flash`
5. `gemini-2.5-flash` (without prefix)
6. `gemini-2.0-flash` (without prefix)

**Logic**: Jika model gagal, langsung try next model

#### ℹ️ Available Models Expander
- **Purpose**: Show available models dari API
- **Expandable**: Click to expand/collapse
- **Content**: List models dengan `generateContent` support
- **Limit**: Tampil 5 model pertama
- **Format**: Code block

#### 💾 Chat History Management
- **Storage**: `st.session_state.chat_history`
- **Persistence**: Per session (hilang jika refresh)
- **Format**: List of dicts `[{role, content}, ...]`
- **Display**: Scroll ke bawah otomatis

#### 🗑️ Clear Chat Button
- **Function**: Reset chat history
- **Action**: Clear `st.session_state.chat_history`
- **Rerun**: Immediate UI update

#### 🎭 Demo Mode (No API Key)
**Features:**
- Warning message untuk input API key
- Link ke API key generator
- 5 contoh pertanyaan:
  - Cluster tertinggi
  - Tren 2022-2024
  - Wilayah rawan banjir
  - Karakteristik cluster
  - Musim hujan

### Usage Examples

**Q: "Cluster mana yang curah hujannya paling tinggi?"**
```
A: 🌧️ Berdasarkan data, **Cluster 3** memiliki curah hujan 
tertinggi dengan rata-rata 6.16 mm/hari. Cluster ini mencakup 12 wilayah
termasuk Kab. Malang, Kab. Blitar, Kota Batu yang merupakan dataran tinggi
dengan variasi curah hujan paling besar (std 13.74 mm/hari).
```

**Q: "Bagaimana tren curah hujan dari 2022 ke 2024?"**
```
A: 📉 Tren menurun signifikan:
- 2022: 6.77 mm/hari
- 2023: 5.74 mm/hari (↓ 15%)
- 2024: 5.40 mm/hari (↓ 6%)

Total penurunan 20% dalam 3 tahun, kemungkinan indikasi climate change.
Penurunan terjadi di semua cluster.
```

---

## 4. 📈 Time Series Analysis

**Analisis temporal** curah hujan harian dan bulanan.

### Features

#### 🎯 Region Selector
- **Type**: Multiselect dropdown
- **Options**: All 38 wilayah
- **Default**: 3 wilayah pertama
- **Limit**: Recommended max 5 untuk readability

#### 📊 Daily Rainfall Line Chart
**Properties:**
- **Type**: Plotly line chart
- **X-axis**: Tanggal (daily)
- **Y-axis**: Curah hujan (mm/hari)
- **Lines**: Satu line per wilayah selected
- **Colors**: Auto-assigned by Plotly
- **Height**: 500px

**Interactive Features:**
- Hover unified (vertical line across all lines)
- Zoom: Click & drag
- Pan: Click & move
- Reset: Double click
- Download: Camera icon (PNG)
- Legend: Click to hide/show lines

#### 📅 Monthly Average Bar Chart
**Properties:**
- **Type**: Plotly grouped bar chart
- **X-axis**: Bulan (monthly)
- **Y-axis**: Rata-rata curah hujan
- **Groups**: Per wilayah
- **Colors**: Different per wilayah
- **Height**: 400px

**Aggregation:**
```python
# Groupby month & wilayah
monthly = df.groupby([
    df['tanggal'].dt.to_period('M'), 
    'Wilayah'
])['PRECTOTCORR'].mean()
```

---

## 5. 🎯 Cluster Analysis

**Analisis mendalam** tentang clustering results dan karakteristik.

### Features

#### 📊 Membership Degree Visualization
**Type**: Stacked bar chart (100% stacked)

**Data**: `tabel_keanggotaan_akhir_c3_m2.5.csv`
- **Columns**: cluster_1, cluster_2, cluster_3 (fuzzy membership 0-1)
- **Display**: 10 wilayah pertama
- **Colors**: Red, Teal, Blue (per cluster)

**Interpretation:**
- Tinggi bar = strong membership (mendekati 1.0)
- Rendah bar = weak membership (mendekati 0.0)
- Perfect membership = 0.999...

**Example:**
```
Kab. Kediri:
- Cluster 1: 0.9999 ✅ (dominant)
- Cluster 2: 0.0001
- Cluster 3: 0.0000
```

#### 📏 Distance to Medoid Box Plot
**Purpose**: Show variability jarak wilayah ke medoid cluster-nya

**Data**: `data_boxplot_jarak_ke_medoid.csv`
- **X-axis**: Cluster (1, 2, 3)
- **Y-axis**: Jarak ke medoid (distance metric)
- **Box**: Q1, median, Q3
- **Whiskers**: Min-max
- **Outliers**: Dots beyond whiskers

**Interpretation:**
- Median rendah = cluster compact
- IQR kecil = cluster homogen
- Outliers = wilayah atypical

#### 🎲 3D Scatter Plot
**Axes:**
- **X**: Mean rainfall
- **Y**: Standard deviation
- **Z**: Maximum rainfall
- **Color**: Cluster (3 colors)
- **Hover**: Nama wilayah

**Interactive:**
- Rotate: Click & drag
- Zoom: Scroll
- Pan: Right-click & drag
- Reset: Home icon

**Height**: 600px untuk full 3D experience

**Purpose**: Visualize cluster separation dalam 3D space

---

## 6. 🌧️ Rainfall Analytics

**Analisis pola** curah hujan, extreme events, dan drought.

### Features

#### 🔥 Monthly Rainfall Heatmap
**Type**: Plotly imshow (heatmap)

**Axes:**
- **X**: Tahun (2022, 2023, 2024)
- **Y**: Bulan (Jan-Des)
- **Color**: Curah hujan (mm/hari)
- **Scale**: Blues (light to dark)

**Data Processing:**
```python
heatmap_data = df.pivot_table(
    values='PRECTOTCORR',
    index=df['tanggal'].dt.month,
    columns=df['tanggal'].dt.year,
    aggfunc='mean'
)
```

**Interpretation:**
- Dark blue = High rainfall (musim hujan)
- Light blue = Low rainfall (musim kering)
- Pattern: Biasanya tinggi di Des-Feb, rendah di Jul-Sep

#### ⚠️ Extreme Events Detection
**Criteria**: `PRECTOTCORR > 100 mm/hari`

**Display:**
- **Table**: Top 20 extreme events
- **Columns**: Tanggal, Wilayah, Curah Hujan, Cluster
- **Sorting**: Descending by rainfall
- **Metric**: Total count

**Use Case:**
- Identifikasi potensi banjir
- Disaster preparedness
- Infrastructure planning

#### ☀️ Drought Days Analysis
**Criteria**: `PRECTOTCORR < 1 mm/hari`

**Visualization**: Horizontal bar chart
- **Top 10 wilayah** dengan hari kering terbanyak
- **X-axis**: Number of days
- **Y-axis**: Wilayah
- **Color**: Orange gradient (intensity by count)

**Use Case:**
- Water resource management
- Agricultural planning
- Drought mitigation

#### 🎨 Rainfall Intensity Classification
**6 Kategori:**
1. **No Rain**: 0 - 0.5 mm (Grey)
2. **Light**: 0.5 - 20 mm (Light green)
3. **Moderate**: 20 - 50 mm (Yellow)
4. **Heavy**: 50 - 100 mm (Orange)
5. **Very Heavy**: 100 - 150 mm (Red)
6. **Extreme**: > 150 mm (Dark red)

**Visualization**: Pie chart dengan percentages

**Processing:**
```python
def classify_intensity(value):
    for intensity, (min_val, max_val) in RAINFALL_INTENSITY.items():
        if min_val <= value < max_val:
            return intensity
```

---

## 7. 📊 Statistical Dashboard

**Visualisasi statistik** lanjutan untuk analisis mendalam.

### Features

#### 🎻 Violin Plot
**Type**: Plotly violin plot dengan box overlay

**Components:**
- **Violin**: Density distribution (kde)
- **Box**: Q1, median, Q3 overlay
- **Points**: Individual data points (optional)
- **Width**: Proportional to density

**Per Cluster:**
- Cluster 1
- Cluster 2
- Cluster 3

**Interpretation:
- Wide area = Many data points at that value
- Narrow area = Few data points
- Multiple peaks = Multimodal distribution

#### 📊 Histogram Distribution
**Type**: Plotly histogram with overlay

**Settings:**
- **Bins**: 50 bins
- **Opacity**: 0.7 (untuk overlay)
- **Colors**: Per cluster
- **Barmode**: Overlay
- **X-axis**: Curah hujan (mm/hari)
- **Y-axis**: Frequency (count)

**Purpose**: Show frequency distribution overlap antar cluster

#### 🚨 Outlier Analysis
**Data**: `outlier_per_wilayah.csv`

**Visualization**: Horizontal bar chart
- **Top 15 wilayah** dengan outlier terbanyak
- **X-axis**: Jumlah outlier
- **Y-axis**: Wilayah
- **Color**: Red gradient (darker = more outliers)

**Outlier Detection Method**: IQR method
```
Q1 = 25th percentile
Q3 = 75th percentile
IQR = Q3 - Q1
Lower bound = Q1 - 1.5 * IQR
Upper bound = Q3 + 1.5 * IQR
Outliers = values < Lower OR > Upper
```

#### 🔗 Correlation Matrix
**Type**: Plotly heatmap dengan annotations

**Conditions:**
- Minimum 2 wilayah selected
- Maximum 10 wilayah (untuk readability)
- Data: Pivot curah hujan per tanggal × wilayah

**Calculation:**
```python
corr_matrix = pivot_data[selected_wilayah].corr()
```

**Visualization:**
- **Color scale**: RdBu_r (red-white-blue reversed)
- **Range**: -1 to +1
- **Annotations**: Correlation values (2 decimal places)
- **Size**: 500×500 px

**Interpretation:**
- +1 (Dark blue) = Perfect positive correlation
- 0 (White) = No correlation
- -1 (Dark red) = Perfect negative correlation

---

## 8. 🔍 Data Explorer

**Interactive table** untuk eksplorasi dan export data.

### Features

#### 🔎 Search & Filter Panel
**3 Filters:**

1. **Search Wilayah**
   - Type: Text input
   - Function: Case-insensitive substring search
   - Example: "malang" → finds "Kab. Malang", "Kota Malang"

2. **Min Rainfall**
   - Type: Number input
   - Range: 0 to max
   - Default: 0.0
   - Step: 0.1

3. **Max Rainfall**
   - Type: Number input
   - Range: 0 to max
   - Default: Maximum in dataset
   - Step: 0.1

**Filter Logic**: AND condition (all must match)

#### 📋 Interactive Data Table
**Properties:**
- **Library**: Streamlit native dataframe
- **Height**: 400px (scrollable)
- **Sorting**: Click column header
- **Columns Displayed**:
  - tanggal
  - Wilayah
  - PRECTOTCORR (curah hujan)
  - Cluster
  - nama_bulan

**Default Sort**: tanggal descending (newest first)

**Row Counter**: Shows `X records` filtered

#### 💾 Download Buttons
**2 Format:**

1. **CSV Export**
   - Encoding: UTF-8
   - Separator: Comma
   - Include index: No
   - Filename: `rainfall_data_YYYYMMDD.csv`

2. **Excel Export**
   - Engine: OpenPyXL
   - Sheet name: "Data"
   - Include index: No
   - Filename: `rainfall_data_YYYYMMDD.xlsx`

**Processing:**
```python
# CSV
csv = df_explorer.to_csv(index=False).encode('utf-8')

# Excel
output = io.BytesIO()
with pd.ExcelWriter(output, engine='openpyxl') as writer:
    df_explorer.to_excel(writer, index=False, sheet_name='Data')
excel_data = output.getvalue()
```

#### 📊 Summary Statistics Table
**Grouped by Cluster:**

**Metrics Calculated:**
- Count (jumlah records)
- Mean (rata-rata)
- Median (nilai tengah)
- Std (standar deviasi)
- Min (nilai minimum)
- Max (nilai maksimum)

**Format**: 2 decimal places

---

## 9. 📉 Performance Metrics

**Evaluasi kualitas** clustering dan optimization results.

### Features

#### 🎯 Evaluation KPI Cards (3 Cards)
1. **Optimal Clusters**
   - Value: 3
   - Delta: "Best Configuration"
   - Source: Silhouette, Xie-Beni comparison

2. **Fuzziness (m)**
   - Value: 2.5
   - Delta: "Optimal"
   - Range tested: 1.5, 2.0, 2.5
   - Winner: 2.5 (lowest Xie-Beni)

3. **Xie-Beni Index**
   - Value: 0.2721
   - Delta: "Lower is Better" (inverse color)
   - Formula: Compactness / Separation
   - Interpretation: <0.5 = Excellent

#### 📊 Parameter Tuning Bar Chart
**Data**: `ringkasan_evaluasi_fcm.csv`

**Comparison**: Xie-Beni for m = 1.5, 2.0, 2.5
- **X-axis**: Fuzziness parameter (m)
- **Y-axis**: Xie-Beni Index
- **Colors**: Different per m value
- **Annotations**: Values on top of bars

**Winner**: m = 2.5 (lowest Xie-Beni = 0.2721)

#### 📈 Objective Function Convergence
**Data**: `tabel_fungsi_objektif_per_iterasi.csv`

**Type**: Plotly line chart with markers
- **X-axis**: Iteration (1, 2, ...)
- **Y-axis**: Objective function value (J)
- **Points**: Circle markers
- **Line**: Solid

**Convergence Criteria**: 
- Tolerance: 1e-5
- Converged: Yes (after 2 iterations)

**Interpretation:**
- Flat line = Converged
- Decreasing = Improving
- Oscillating = Not converged

#### 📋 Detailed Evaluation Table
**Data**: Full evaluation results (3 rows)

**Columns:**
- c (number of clusters)
- m (fuzziness parameter)
- J (objective function)
- XieBeni (index)
- Iterations (count)
- Converged (boolean)
- n_init (15 runs)
- max_iter (300 max)
- tol (1e-5)

**Format**: 
- J: 2 decimals
- XieBeni: 4 decimals
- m: 1 decimal

#### 💡 Key Insights Section
**Auto-Generated Summary:**
- Best configuration (c=3, m=2.5)
- Xie-Beni value interpretation
- Iterations to convergence
- Convergence status
- Objective function final value

---

## 🎨 Common Features (All Pages)

### Sidebar Filters
**Always Available:**
- **Periode**: Date range picker (start-end)
- **Cluster**: Multiselect [1, 2, 3]
- **Wilayah**: Multiselect (all 38 wilayah)
- **Theme**: Radio Dark/Light
- **API Key**: Password input untuk Gemini

**Filter Behavior**:
- Applied globally ke semua visualizations
- Real-time update saat selection berubah
- Persistent within session

### Export Features
**Available on Charts:**
- **Camera icon** → Download PNG
- **Pan tool** → Move view
- **Zoom tool** → Scroll or click-drag
- **Reset** → Double-click
- **Autoscale** → Reset axes

### Performance Optimizations
- **Caching**: `@st.cache_data` untuk load_data()
- **Lazy loading**: Data loaded once per session
- **Filtered views**: Only render selected data
- **Optimized queries**: Pandas groupby & merge

---

**📚 More Information:**
- [USER_GUIDE.md](USER_GUIDE.md) - How to use each feature
- [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) - Code organization
- [README.md](README.md) - Project overview

**🆘 Need Help?**
- GitHub Issues: Report bugs or request features
- Discussions: Ask questions & share ideas
