# 📖 USER GUIDE

Panduan lengkap penggunaan Rainfall Clustering Dashboard untuk analisis data curah hujan Jawa Timur.

---

## 📋 Table of Contents

1. [Getting Started](#-getting-started)
2. [Navigation](#-navigation)
3. [Dashboard Overview](#-dashboard-overview)
4. [Interactive Map](#-interactive-map)
5. [AI Chatbot](#-ai-chatbot)
6. [Time Series Analysis](#-time-series-analysis)
7. [Cluster Analysis](#-cluster-analysis)
8. [Rainfall Analytics](#-rainfall-analytics)
9. [Statistical Dashboard](#-statistical-dashboard)
10. [Data Explorer](#-data-explorer)
11. [Performance Metrics](#-performance-metrics)
12. [Filtering Data](#-filtering-data)
13. [Exporting Data](#-exporting-data)
14. [Tips & Best Practices](#-tips--best-practices)
15. [Troubleshooting](#-troubleshooting)

---

## 🚀 Getting Started

### First Launch

1. **Start the application:**
   ```bash
   streamlit run app.py
   ```

2. **Access the dashboard:**
   - Open browser to: `http://localhost:8501`
   - Or use Network URL for remote access

3. **Check data loading:**
   - Wait for "Loading data..." to complete
   - Verify no error messages appear
   - Sidebar should show navigation menu

### Interface Overview

```
┌─────────────────────────────────────────────────────────┐
│  [Logo]  Rainfall Clustering Dashboard                  │
├──────────────┬──────────────────────────────────────────┤
│              │                                           │
│  SIDEBAR     │         MAIN CONTENT AREA                 │
│              │                                           │
│ Navigation   │  • Charts & visualizations               │
│ Filters      │  • Data tables                           │
│ Settings     │  • Interactive elements                  │
│              │                                           │
├──────────────┴──────────────────────────────────────────┤
│  Footer: Made with ❤️ by your team                      │
└─────────────────────────────────────────────────────────┘
```

---

## 🧭 Navigation

### Sidebar Menu

**9 Pages Available:**

| Icon | Page Name | Purpose |
|------|-----------|---------|
| 🏠 | Dashboard | Overview & summary |
| 🗺️ | Interactive Map | Geographic visualization |
| 🤖 | AI Chatbot | Ask questions about data |
| 📊 | Time Series | Trend analysis |
| 🎯 | Cluster Analysis | Clustering details |
| 🌧️ | Rainfall Analytics | Extreme events & patterns |
| 📈 | Statistical Dashboard | Advanced statistics |
| 🔍 | Data Explorer | Search & filter data |
| 📐 | Performance Metrics | Model evaluation |

**How to Navigate:**
1. Click page name in sidebar
2. Current page highlighted in color
3. Content area updates instantly

---

## 🏠 Dashboard Overview

### What You See

**4 KPI Cards (Top):**
- Total data points
- Average rainfall
- Max rainfall
- Number of regions

**Main Visualizations:**
1. **Box Plot**: Distribution per cluster
2. **Pie Chart**: Region distribution
3. **Time Series**: Monthly trends
4. **Statistics Cards**: Mean, median, std dev

### How to Use

**Analyzing Clusters:**
```
Step 1: Look at box plot
  → Compare median (line inside box)
  → Check spread (box height)
  → Identify outliers (dots outside)

Step 2: Check pie chart
  → See cluster sizes
  → Note percentages

Step 3: Review time series
  → Observe seasonal patterns
  → Identify peaks (wet season)
```

**Example Workflow:**
> **Question**: "Which cluster has highest rainfall?"  
> **Steps**:
> 1. Look at box plot → Find tallest box
> 2. Check median line → Red cluster (Cluster 1)
> 3. Verify in statistics cards → Mean: 6.21 mm/day

---

## 🗺️ Interactive Map

### Map Features

**Markers:**
- Color-coded by cluster
- Size proportional to rainfall
- Click for details popup

**Legend (Bottom-right):**
- 🔴 Cluster 1 (Kediri) - 18 regions
- 🔵 Cluster 2 (Magetan) - 8 regions  
- 🟢 Cluster 3 (Blitar) - 12 regions

**Statistics Panel:**
- Most affected region
- Average rainfall
- Highest recorded

### How to Use

**Exploring the Map:**
```
🖱️ Mouse Controls:
  Scroll      → Zoom in/out
  Click+Drag  → Pan map
  Click marker→ View popup

📱 Touch Controls:
  Pinch       → Zoom
  Swipe       → Pan
  Tap marker  → View popup
```

**Finding Specific Region:**
1. Use sidebar "Pilih Wilayah" filter
2. Or scan map for color (cluster)
3. Or use Data Explorer page

**Example Workflow:**
> **Task**: "Find all high-rainfall regions"  
> **Steps**:
> 1. Look for large red markers
> 2. Click each to see exact values
> 3. Note down region names
> 4. Compare with cluster analysis

---

## 🤖 AI Chatbot

### Prerequisites

**Setup API Key:**
- Method 1: Enter in sidebar textbox
- Method 2: Add to `.streamlit/secrets.toml`

### How to Chat

**Starting Conversation:**
```
1. Select "🤖 AI Chatbot" page
2. Enter API key (if not saved)
3. Type question in chat box
4. Press Enter or click Submit
```

**Question Examples:**

**Basic Questions:**
- "Apa cluster dengan curah hujan tertinggi?"
- "Berapa rata-rata curah hujan di Surabaya?"
- "Kapan musim hujan paling tinggi?"

**Advanced Questions:**
- "Bandingkan pola curah hujan antar cluster"
- "Apa penyebab Cluster 1 memiliki curah hujan tinggi?"
- "Prediksi trend curah hujan tahun depan"

**Data-Specific:**
- "Berapa banyak hari kering di Kabupaten Kediri?"
- "Wilayah mana yang sering banjir?"
- "Apa perbedaan Cluster 1 dan Cluster 2?"

### Understanding Responses

**AI Provides:**
- Statistical facts from data
- Comparisons between clusters
- Insights and patterns
- Recommendations

**Example Interaction:**
```
User: "Apa karakteristik Cluster 1?"

AI: "Cluster 1 (Pusat: Kediri) memiliki karakteristik:
     • Rata-rata curah hujan: 6.21 mm/hari (TERTINGGI)
     • Jumlah wilayah: 18 (47.4%)
     • Curah hujan maksimum: 318.68 mm/hari
     • Pola: Curah hujan tinggi & konsisten
     • Wilayah: Kediri, Blitar, Tulungagung, dll.
     
     Ini menunjukkan zona dengan intensitas hujan
     sangat tinggi, memerlukan perhatian untuk
     manajemen banjir."

User: "Bagaimana dibanding Cluster 2?"

AI: "Cluster 2 (Pusat: Magetan) berbeda signifikan:
     • Rata-rata: 5.72 mm/hari (lebih rendah 8%)
     • Curah hujan lebih stabil (std: 9.78)
     • Wilayah: Magetan, Madiun, Ngawi, Pacitan
     • Pola: Curah hujan sedang-tinggi
     
     Cluster 2 lebih moderat, cocok untuk
     pertanian dengan irigasi terencana."
```

### Tips for Better Responses

**✅ Good Questions:**
- Specific and clear
- Use data terminology
- One question at a time
- Follow-up based on previous answer

**❌ Avoid:**
- Multiple questions in one message
- Vague terms ("bagus", "jelek")
- Questions outside dataset scope
- Personal opinions

---

## 📊 Time Series Analysis

### Available Charts

**1. Daily Rainfall Chart**
- Line chart with all dates
- X-axis: Date (2022-2024)
- Y-axis: Rainfall (mm/day)
- Tooltip: Exact values

**2. Monthly Average Chart**
- Bar chart by month
- X-axis: Months (Jan-Dec)
- Y-axis: Average rainfall
- Color: Gradient blue

### How to Use

**Analyzing Trends:**
```
Step 1: Select region from dropdown
  → Sidebar "Pilih Wilayah"
  → Or keep "Semua Wilayah" for overall

Step 2: Observe daily chart
  → Identify peaks (wet season)
  → Note valleys (dry season)
  → Look for patterns

Step 3: Check monthly chart
  → Compare month-to-month
  → Find highest/lowest months
  → Seasonal patterns
```

**Example Workflow:**
> **Question**: "When is wet season in Surabaya?"  
> **Steps**:
> 1. Select "Kota Surabaya" in sidebar
> 2. Look at monthly chart
> 3. Find highest bars → Nov, Dec, Jan (>10 mm/day)
> 4. Conclusion: Wet season Nov-Jan

### Interpreting Patterns

**Seasonal Patterns:**
- **Wet Season** (Nov-Mar): High rainfall
- **Dry Season** (Apr-Oct): Low rainfall
- **Transition** (Mar-Apr, Oct-Nov): Variable

**Anomalies:**
- Sudden spikes → Extreme events
- Extended low periods → Drought
- Irregular patterns → Climate variability

---

## 🎯 Cluster Analysis

### Three Visualizations

**1. Membership Degrees (Stacked Bar)**
- Shows fuzzy membership per region
- 100% stacked (sums to 1.0)
- Color by cluster

**2. Distance to Medoid (Box Plot)**
- Statistical spread per cluster
- Lower = more homogeneous
- Outliers visible

**3. 3D Scatter Plot**
- X: Mean rainfall
- Y: Standard deviation
- Z: Maximum rainfall
- Color: Cluster assignment

### How to Use

**Understanding Membership:**
```
Example: Kabupaten Bangkalan
  Cluster 1: 40.8% ← Primary cluster
  Cluster 2: 34.2%
  Cluster 3: 25.0%

Interpretation:
→ Belongs to Cluster 1, but shows
  characteristics of other clusters too
→ "Fuzzy" membership reflects gradual
  transitions between clusters
```

**Comparing Clusters:**
```
Step 1: Check distance box plot
  → Lower median = tighter cluster
  → Fewer outliers = better quality

Step 2: View 3D scatter
  → Rotate for different angles
  → Observe separation
  → Identify overlap regions

Step 3: Cross-reference with map
  → Geographic patterns?
  → Adjacent regions similar?
```

**Example Workflow:**
> **Task**: "Is Cluster 1 well-separated?"  
> **Steps**:
> 1. Look at 3D scatter → Red points form distinct group
> 2. Check distance box plot → Median ~15, few outliers
> 3. View membership → Most >80% primary cluster
> 4. Conclusion: Yes, well-defined cluster

---

## 🌧️ Rainfall Analytics

### Four Analysis Tools

**1. Monthly Heatmap**
- Rows: Months (Jan-Dec)
- Columns: Years (2022-2024)
- Color intensity: Rainfall amount
- Tooltip: Exact values

**2. Extreme Events Table**
- Lists all days >100 mm/day
- Columns: Date, Region, Rainfall
- Sortable by any column

**3. Drought Analysis**
- Days with <1 mm/day
- Percentage of total days
- Distribution by region

**4. Intensity Classification**
- Pie chart by category:
  - No rain (0 mm)
  - Light (0-5 mm)
  - Moderate (5-20 mm)
  - Heavy (20-50 mm)
  - Very heavy (50-100 mm)
  - Extreme (>100 mm)

### How to Use

**Finding Extreme Events:**
```
Step 1: Scroll to Extreme Events table
  → Click column headers to sort
  → Click "Rainfall" twice for descending

Step 2: Note date and region
  → Highest: 318.68 mm/day
  → Date: [date]
  → Region: [region]

Step 3: Cross-check with map
  → Find region on map
  → Verify cluster assignment
```

**Analyzing Drought:**
```
Step 1: View drought statistics
  → Total drought days
  → Percentage of dataset

Step 2: Check distribution chart
  → Which regions most affected?
  → Seasonal patterns?

Step 3: Compare with intensity pie
  → How much "no rain" vs "light rain"?
```

**Example Workflow:**
> **Question**: "Which regions prone to flooding?"  
> **Steps**:
> 1. Sort extreme events by frequency
> 2. Count occurrences per region
> 3. Check monthly heatmap for patterns
> 4. Find regions: Kediri, Blitar, Tulungagung (Cluster 1)

---

## 📈 Statistical Dashboard

### Four Statistical Views

**1. Violin Plot**
- Shows distribution shape
- Width = density
- Inner box = quartiles
- Compare across clusters

**2. Distribution Histogram**
- Bins: 50 intervals
- Overlay: Normal curve (orange)
- Shows skewness

**3. Outlier Analysis**
- Method: IQR (Interquartile Range)
- Table lists all outliers
- Statistics: Count, min, max

**4. Correlation Matrix**
- Variables: Mean, Std, Min, Max
- Color: Red (positive), Blue (negative)
- Values: -1 to +1

### How to Use

**Comparing Distributions:**
```
Violin Plot Analysis:
  Wide section → Many data points
  Narrow section → Few data points
  Center line → Median
  Box inside → Q1-Q3 range

Example:
  Cluster 1: Wide at 0-10 mm (most days low)
            Narrow at 15-20 mm (few days)
            Tail to 40+ mm (extreme events)
```

**Understanding Outliers:**
```
Outlier Definition:
  Q1 = 25th percentile
  Q3 = 75th percentile
  IQR = Q3 - Q1
  
  Lower Bound = Q1 - 1.5×IQR
  Upper Bound = Q3 + 1.5×IQR
  
  Outlier if: value < Lower OR value > Upper
```

**Correlation Insights:**
```
Matrix Reading:
  1.0  → Perfect positive correlation
  0.5  → Moderate positive
  0.0  → No correlation
  -0.5 → Moderate negative
  -1.0 → Perfect negative

Example:
  Mean ↔ Max: 0.85 (high correlation)
  → Regions with high average also have
    high maximum rainfall
```

---

## 🔍 Data Explorer

### Search & Filter Panel

**Three Filters Available:**
1. **Wilayah** (Region)
   - Dropdown with all 38 regions
   - Default: "Semua Wilayah"

2. **Cluster**
   - Options: 1, 2, 3, or "Semua"
   - Default: "Semua"

3. **Date Range**
   - Start date picker
   - End date picker
   - Default: Full range (2022-2024)

### How to Use

**Searching for Specific Data:**
```
Example: Find all high-rainfall days in Surabaya

Step 1: Set filters
  Wilayah: "Kota Surabaya"
  Cluster: "Semua"
  Date: 2022-01-01 to 2024-12-31

Step 2: View results table
  → Data updates automatically
  → Sortable by clicking columns

Step 3: Sort by rainfall
  → Click "PRECTOTCORR" column
  → Click again for descending
  → Top rows = highest rainfall
```

**Exporting Results:**
```
Step 1: Apply desired filters

Step 2: Click export button
  Options:
  • 📥 Download CSV
  • 📥 Download Excel

Step 3: Save file
  → Opens browser download
  → Default name: rainfall_data_[date].csv
  → Open in Excel, Python, R, etc.
```

**Example Workflow:**
> **Task**: "Compare rainfall in Cluster 1 vs Cluster 3 in 2023"  
> **Steps**:
> 1. Filter: Cluster 1, Date 2023-01-01 to 2023-12-31
> 2. Export CSV → cluster1_2023.csv
> 3. Repeat for Cluster 3 → cluster3_2023.csv
> 4. Analyze in external tool (Excel, Python)

### Summary Statistics

**Below Table:**
- Total records shown
- Date range
- Statistics: Mean, Median, Std, Min, Max

**Use Cases:**
- Quick verification of filter results
- Sanity check before export
- Preliminary analysis

---

## 📐 Performance Metrics

### Evaluation Dashboard

**Four Components:**

**1. KPI Cards (Top)**
- Objective Function (J)
- Xie-Beni Index
- Convergence Status
- Iterations Used

**2. Parameter Tuning Chart**
- X-axis: m values (1.5, 2.0, 2.5)
- Y-axis: Xie-Beni Index
- Lower = better
- Optimal: m = 2.5

**3. Convergence Plot**
- X-axis: Iteration number
- Y-axis: Objective function J
- Shows algorithm convergence
- Stops when change < tolerance

**4. Detailed Metrics Table**
- All parameters tested
- Evaluation scores
- Convergence info

### How to Use

**Understanding Clustering Quality:**
```
Xie-Beni Index Interpretation:
  < 0.3  → Excellent clustering ✅
  0.3-0.5 → Good clustering
  0.5-0.7 → Fair clustering
  > 0.7  → Poor clustering

Your Results: 0.2721 → EXCELLENT
```

**Convergence Analysis:**
```
Step 1: Look at convergence plot
  → Sharp initial drop → Fast convergence
  → Flat plateau → Stable solution

Step 2: Check iterations
  → 2 iterations (very fast!)
  → Tolerance: 1e-05 (strict)
  → Converged: True ✅

Interpretation:
  Fast convergence + low Xie-Beni
  = High-quality, distinct clusters
```

**Parameter Selection:**
```
m (fuzziness parameter) effects:
  m = 1.5 → Crisp clusters (less fuzzy)
  m = 2.0 → Balanced
  m = 2.5 → Fuzzy clusters ← OPTIMAL

Why m=2.5 best?
  → Lowest Xie-Beni (0.2721)
  → Reflects gradual transitions
  → More realistic for geographic data
```

---

## 🔧 Filtering Data

### Sidebar Filters

**Filter Locations:**
- Top of sidebar (always visible)
- Persist across page navigation
- Apply to ALL visualizations

**Available Filters:**

**1. Date Range Slider**
```
[2022-01-01] ←========== ●●●●●●●● =========→ [2024-12-31]
                         Move these sliders
```
**Effect**: Show only data within selected dates

**2. Cluster Selector**
```
( ) Semua Cluster
(•) Cluster 1 - Kediri (18 wilayah)
( ) Cluster 2 - Magetan (8 wilayah)
( ) Cluster 3 - Blitar (12 wilayah)
```
**Effect**: Filter by cluster assignment

**3. Wilayah Dropdown**
```
[Semua Wilayah              ▼]
 Kabupaten Bangkalan
 Kabupaten Banyuwangi
 ...
 Kota Surabaya
```
**Effect**: Focus on specific region

### Filter Combinations

**Example 1: Cluster Analysis**
```
Filters:
  Date: Full range
  Cluster: Cluster 1
  Wilayah: Semua

Result: View all Cluster 1 regions across all time
```

**Example 2: Regional Deep Dive**
```
Filters:
  Date: 2023 only
  Cluster: Semua
  Wilayah: Kota Surabaya

Result: All 2023 data for Surabaya, all clusters
```

**Example 3: Seasonal Comparison**
```
Filters:
  Date: Jan-Mar 2023 (wet season)
  Cluster: Semua
  Wilayah: Semua

Result: Wet season patterns across all regions
```

### Resetting Filters

**Quick Reset:**
1. Select "Semua Cluster"
2. Select "Semua Wilayah"
3. Drag date sliders to full range

**Why Reset?**
- Return to overview
- Compare filtered vs unfiltered
- Troubleshoot unexpected results

---

## 💾 Exporting Data

### Export Options

**Available Formats:**

**1. CSV (Comma-Separated Values)**
- Universal format
- Opens in Excel, Google Sheets
- Best for: Data analysis, sharing

**2. Excel (.xlsx)**
- Formatted spreadsheet
- Multiple sheets possible
- Best for: Reports, presentations

### How to Export

**From Data Explorer Page:**
```
Step 1: Navigate to "🔍 Data Explorer"

Step 2: Apply filters (optional)
  → Export will include only filtered data

Step 3: Click export button
  [📥 Download CSV] or [📥 Download Excel]

Step 4: Save file
  → Browser downloads file
  → Default location: Downloads folder
```

**From Other Pages:**
- Not all pages have export
- Use Data Explorer for comprehensive exports
- Some charts have built-in Plotly export

### Using Exported Data

**In Excel:**
```
1. Open downloaded file
2. Data is ready for analysis
3. Create pivot tables
4. Make custom charts
```

**In Python:**
```python
import pandas as pd

# Read exported CSV
df = pd.read_csv('rainfall_data_20260105.csv')

# Analyze
print(df.describe())
print(df.groupby('Cluster')['PRECTOTCORR'].mean())
```

**In R:**
```r
# Read exported CSV
df <- read.csv('rainfall_data_20260105.csv')

# Analyze
summary(df)
aggregate(PRECTOTCORR ~ Cluster, df, mean)
```

---

## 💡 Tips & Best Practices

### Performance Tips

**1. Data Loading**
- Initial load may take 5-10 seconds
- Data is cached after first load
- Refresh page if data seems stale

**2. Large Visualizations**
- 3D scatter may be slow with all points
- Use cluster filter to reduce points
- Zoom/pan gradually for smoothness

**3. AI Chatbot**
- First response may be slower
- Subsequent responses faster (model loaded)
- Complex questions take longer

### Analysis Workflow

**Recommended Order:**

**For New Users:**
```
1. Dashboard → Overview
2. Interactive Map → Geographic context
3. Time Series → Temporal patterns
4. Cluster Analysis → Understanding groupings
5. Other pages as needed
```

**For Data Analysts:**
```
1. Data Explorer → Get familiar with raw data
2. Statistical Dashboard → Understand distributions
3. Cluster Analysis → Validate clustering
4. Performance Metrics → Check quality
5. Specific analyses (Rainfall Analytics, etc.)
```

**For Presentations:**
```
1. Dashboard → Summary slide
2. Interactive Map → Regional overview
3. Cluster Analysis → 3D visualization
4. Time Series → Trend highlights
5. Performance Metrics → Methodology validation
```

### Common Mistakes

**❌ Mistake 1**: Not setting filters before export
- **Problem**: Export too large or not relevant
- **Solution**: Always filter first, then export

**❌ Mistake 2**: Comparing across filters
- **Problem**: Inconsistent results
- **Solution**: Reset filters, start fresh

**❌ Mistake 3**: Ignoring outliers
- **Problem**: Misleading averages
- **Solution**: Check Statistical Dashboard outliers

**❌ Mistake 4**: Asking AI opinion questions
- **Problem**: AI gives generic answers
- **Solution**: Ask data-specific questions

---

## 🔧 Troubleshooting

### Common Issues

**Issue 1: Data Not Loading**
```
Symptoms:
  • "Loading data..." message persists
  • Error message appears
  • Blank page

Solutions:
  1. Check file paths
     → data_curah_hujan_clean.csv exists?
     → Correct working directory?
  
  2. Verify file format
     → CSV properly formatted?
     → No special characters?
  
  3. Restart app
     → Ctrl+C in terminal
     → streamlit run app.py
```

**Issue 2: Charts Not Displaying**
```
Symptoms:
  • White space where chart should be
  • "Error rendering chart" message

Solutions:
  1. Check filters
     → Are filters too restrictive?
     → Any data passing filters?
  
  2. Refresh page
     → Press F5 or Ctrl+R
  
  3. Clear cache
     → Press 'C' in app (if enabled)
     → Or restart app
```

**Issue 3: AI Chatbot Not Working**
```
Symptoms:
  • "Please enter API key" message
  • Error after sending message
  • No response from AI

Solutions:
  1. Verify API key
     → Check Gemini API Console
     → Key active and not expired?
  
  2. Check internet connection
     → API requires internet
  
  3. Try different model
     → App tries 6 models automatically
     → Wait for fallback
  
  4. Check quota
     → Free tier: 60 requests/minute
     → Wait if limit reached
```

**Issue 4: Slow Performance**
```
Symptoms:
  • App laggy or unresponsive
  • Long loading times
  • Browser freezing

Solutions:
  1. Close unused pages/tabs
  
  2. Use filters to reduce data
     → Select specific cluster
     → Narrow date range
  
  3. Restart app
     → Clear cache
     → Fresh start
  
  4. Check system resources
     → Close other programs
     → More RAM needed?
```

**Issue 5: Export Not Working**
```
Symptoms:
  • Click export, nothing happens
  • File download fails
  • Corrupted file

Solutions:
  1. Check browser permissions
     → Allow downloads from localhost
  
  2. Try different format
     → CSV instead of Excel
  
  3. Reduce data size
     → Apply filters first
     → Export smaller chunks
  
  4. Check disk space
     → Sufficient storage?
```

### Getting Help

**Resources:**

1. **Documentation**
   - [README.md](README.md)
   - [INSTALLATION.md](INSTALLATION.md)
   - [FEATURES.md](FEATURES.md)

2. **GitHub Issues**
   - Report bugs
   - Request features
   - Search existing issues

3. **Contact Support**
   - Email: [your-email]
   - GitHub: [@yourusername]

4. **Community**
   - Streamlit forums
   - Stack Overflow
   - Discord server

---

## 🎯 Use Case Examples

### Use Case 1: Disaster Management

**Scenario**: Identify flood-prone regions

**Workflow:**
```
1. Go to "🌧️ Rainfall Analytics"
2. View extreme events table
3. Sort by frequency (region)
4. Go to "🗺️ Interactive Map"
5. Filter by high-risk cluster
6. Export region list for action plan
```

**Expected Output**: List of regions needing flood mitigation

### Use Case 2: Agricultural Planning

**Scenario**: Recommend crops by rainfall pattern

**Workflow:**
```
1. Go to "🎯 Cluster Analysis"
2. Understand cluster characteristics
3. Go to "📊 Time Series"
4. Analyze seasonal patterns
5. Use "🤖 AI Chatbot"
   Ask: "Rekomendasi tanaman untuk Cluster 2?"
6. Combine AI insights with data
```

**Expected Output**: Crop recommendations per cluster

### Use Case 3: Climate Research

**Scenario**: Study rainfall trends 2022-2024

**Workflow:**
```
1. Go to "📊 Time Series"
2. Select "Semua Wilayah"
3. Observe monthly chart for trends
4. Go to "🌧️ Rainfall Analytics"
5. Check intensity distribution
6. Go to "🔍 Data Explorer"
7. Export all data for statistical analysis
```

**Expected Output**: Dataset for research paper

### Use Case 4: Infrastructure Planning

**Scenario**: Drainage system sizing

**Workflow:**
```
1. Go to "📈 Statistical Dashboard"
2. View distribution histogram
3. Note 95th percentile value
4. Go to "🌧️ Rainfall Analytics"
5. Count extreme events
6. Calculate return periods
7. Use values for drainage design
```

**Expected Output**: Design rainfall values

---

**Need more help?**  
Join our community or open an issue on GitHub!
