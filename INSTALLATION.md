# 📥 INSTALLATION GUIDE

Panduan instalasi lengkap step-by-step untuk Rainfall Clustering Dashboard.

---

## 📋 Table of Contents

- [System Requirements](#-system-requirements)
- [Installation Methods](#-installation-methods)
- [Detailed Installation](#-detailed-installation)
- [Troubleshooting](#-troubleshooting)
- [Next Steps](#-next-steps)

---

## 💻 System Requirements

### Minimum Requirements
- **OS**: Windows 10/11, macOS 10.15+, atau Linux (Ubuntu 20.04+)
- **Python**: 3.11 atau lebih tinggi
- **RAM**: 4 GB
- **Storage**: 500 MB free space
- **Internet**: Diperlukan untuk download dependencies

### Recommended
- **RAM**: 8 GB atau lebih
- **Python**: 3.11.7
- **Browser**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

---

## 🎯 Installation Methods

### Method 1: Quick Install (Recommended)
```bash
# Clone & Install
git clone https://github.com/username/rainfall-dashboard.git
cd rainfall-dashboard
pip install -r requirements.txt
streamlit run app.py
```

### Method 2: Manual Install
Ikuti [Detailed Installation](#-detailed-installation) di bawah.

### Method 3: Docker
```bash
docker pull username/rainfall-dashboard
docker run -p 8501:8501 username/rainfall-dashboard
```

---

## 🔧 Detailed Installation

### Step 1: Install Python

#### Windows
1. Download dari [python.org](https://www.python.org/downloads/)
2. Jalankan installer
3. ✅ **Centang "Add Python to PATH"**
4. Klik "Install Now"
5. Verify:
```cmd
python --version
```

#### macOS
```bash
# Install Homebrew (jika belum)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.11

# Verify
python3 --version
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
python3.11 --version
```

### Step 2: Clone Repository

#### Option A: Using Git
```bash
# Install Git jika belum ada
# Windows: https://git-scm.com/download/win
# macOS: brew install git
# Linux: sudo apt install git

# Clone repository
git clone https://github.com/username/rainfall-dashboard.git
cd rainfall-dashboard
```

#### Option B: Download ZIP
1. Kunjungi https://github.com/username/rainfall-dashboard
2. Klik "Code" → "Download ZIP"
3. Extract ke folder pilihan
4. Buka terminal/cmd di folder tersebut

### Step 3: Create Virtual Environment (Recommended)

#### Windows (CMD)
```cmd
python -m venv .venv
.venv\Scripts\activate
```

#### Windows (PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1

# Jika error "execution policy", jalankan:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**✅ Virtual environment aktif jika prompt menampilkan `(.venv)`**

### Step 4: Install Dependencies

```bash
# Upgrade pip terlebih dahulu
python -m pip install --upgrade pip

# Install semua dependencies
pip install -r requirements.txt
```

**Tunggu 2-5 menit** hingga semua package terinstall.

### Step 5: Verify Installation

```bash
# Check installed packages
pip list

# Should see:
# streamlit      1.31.0
# pandas         2.2.0
# plotly         5.18.0
# ... (13 packages total)
```

### Step 6: Run Application

```bash
streamlit run app.py
```

**Output yang diharapkan:**
```
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

### Step 7: Open Browser

- Buka browser dan akses: **http://localhost:8501**
- Aplikasi akan loading 5-10 detik
- Dashboard akan muncul dengan sidebar di kiri

---

## 🔑 Setup Gemini API Key (Optional)

### Method 1: Via Sidebar (Development)
1. Buka aplikasi
2. Di sidebar, lihat section "🔑 Gemini API"
3. Paste API key Anda
4. Klik diluar textbox untuk save

### Method 2: Via Secrets File (Production)

**1. Create secrets file:**
```bash
mkdir -p .streamlit
```

**2. Edit `.streamlit/secrets.toml`:**
```toml
GEMINI_API_KEY = "your_actual_api_key_here"
```

**3. Restart aplikasi:**
```bash
# Stop: Ctrl+C
# Start again:
streamlit run app.py
```

### Get API Key
1. Kunjungi: https://aistudio.google.com/app/apikey
2. Login dengan Google account
3. Klik "Create API Key"
4. Copy key yang dihasilkan

---

## 🐛 Troubleshooting

### Error: `python: command not found`

**Windows:**
```cmd
# Coba dengan:
py --version
py -m pip install -r requirements.txt
```

**macOS/Linux:**
```bash
# Gunakan python3:
python3 --version
python3 -m venv .venv
```

### Error: `pip: command not found`

```bash
# Install pip
python -m ensurepip --upgrade

# Atau download get-pip.py:
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### Error: `ModuleNotFoundError: No module named 'streamlit'`

```bash
# Pastikan virtual environment aktif
# Windows:
.venv\Scripts\activate

# macOS/Linux:
source .venv/bin/activate

# Install ulang:
pip install -r requirements.txt
```

### Error: Compiler/Build Tools Not Found (Windows)

**Untuk pandas/numpy build errors:**

1. Download **Visual Studio Build Tools**:
   - https://visualstudio.microsoft.com/downloads/
   - Pilih "Build Tools for Visual Studio 2022"
   - Install dengan "Desktop development with C++"

2. Atau install pre-built wheels:
```cmd
pip install --only-binary :all: pandas numpy
```

### Error: Port 8501 Already in Use

```bash
# Stop process yang menggunakan port
# Windows:
netstat -ano | findstr :8501
taskkill /PID <process_id> /F

# macOS/Linux:
lsof -ti:8501 | xargs kill

# Atau gunakan port lain:
streamlit run app.py --server.port 8502
```

### Slow Loading / Memory Issues

**1. Reduce data size:**
```python
# Di app.py, tambahkan sampling:
df = df.sample(frac=0.5, random_state=42)  # Use 50% data
```

**2. Clear cache:**
```bash
# Hapus Streamlit cache
rm -rf ~/.streamlit/cache
# Windows: del /s /q %USERPROFILE%\.streamlit\cache
```

**3. Increase memory (Docker):**
```bash
docker run -m 4g -p 8501:8501 rainfall-dashboard
```

### Connection Timeout (Gemini API)

```python
# Error: timeout
# Solusi: Check internet connection
# Atau coba model lain di sidebar expander
```

### Data Files Not Found

```bash
# Pastikan struktur folder benar:
ls -la  # macOS/Linux
dir     # Windows

# Harus ada:
# - data_curah_hujan_clean.csv
# - hasil_cluster_final.csv
# - clustering_output/
# - data_understanding/
```

---

## ✅ Verification Checklist

Setelah instalasi, verify dengan checklist ini:

- [ ] Python 3.11+ terinstall (`python --version`)
- [ ] Virtual environment created dan active
- [ ] Semua 13 packages terinstall (`pip list`)
- [ ] Data files ada di folder yang benar
- [ ] Aplikasi berjalan tanpa error
- [ ] Browser bisa akses http://localhost:8501
- [ ] Dashboard muncul dengan 9 halaman di sidebar
- [ ] Peta muncul di halaman "Interactive Map"
- [ ] Grafik loading dengan benar
- [ ] Filter di sidebar berfungsi

---

## 📦 Package List

Berikut daftar lengkap dependencies yang akan terinstall:

| Package | Version | Size | Purpose |
|---------|---------|------|---------|
| streamlit | 1.31+ | ~50 MB | Web framework |
| pandas | 2.2+ | ~150 MB | Data manipulation |
| numpy | 1.26+ | ~30 MB | Numerical computing |
| plotly | 5.18+ | ~80 MB | Interactive charts |
| folium | 0.15+ | ~10 MB | Maps |
| streamlit-folium | 0.16+ | ~1 MB | Folium integration |
| google-generativeai | 0.3+ | ~20 MB | Gemini AI |
| openpyxl | 3.1+ | ~5 MB | Excel export |
| scikit-learn | 1.4+ | ~120 MB | ML utilities |
| scipy | 1.12+ | ~50 MB | Scientific computing |
| seaborn | 0.13+ | ~10 MB | Statistical plots |
| matplotlib | 3.8+ | ~80 MB | Base plotting |
| Pillow | 10.0+ | ~20 MB | Image processing |

**Total Download:** ~600-700 MB  
**Total Installed:** ~1-1.5 GB

---

## 🚀 Next Steps

Setelah instalasi berhasil:

1. **📖 Baca User Guide**
   - [USER_GUIDE.md](USER_GUIDE.md) untuk panduan penggunaan

2. **✨ Explore Features**
   - [FEATURES.md](FEATURES.md) untuk detail fitur

3. **🔧 Customize**
   - Edit `config.py` untuk customize colors & settings

4. **🚀 Deploy**
   - [DEPLOYMENT.md](DEPLOYMENT.md) untuk deploy online

5. **💬 Get Help**
   - Join community discussions
   - Report issues di GitHub

---

## 🔄 Update Application

### Update Code
```bash
git pull origin main
pip install -r requirements.txt --upgrade
streamlit cache clear
streamlit run app.py
```

### Update Python
```bash
# Check latest version
python --version

# Install Python 3.11.x dari python.org
# Recreate virtual environment
rm -rf .venv
python3.11 -m venv .venv
source .venv/bin/activate  # atau .venv\Scripts\activate di Windows
pip install -r requirements.txt
```

---

## 🆘 Support

Jika mengalami masalah:

1. **Check FAQ**: [FAQ.md](FAQ.md)
2. **GitHub Issues**: https://github.com/username/rainfall-dashboard/issues
3. **Community**: https://discuss.streamlit.io/
4. **Email**: support@example.com

---

## 📚 Additional Resources

- [Python Installation Guide](https://realpython.com/installing-python/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Git Tutorial](https://git-scm.com/book/en/v2)
- [Virtual Environment Guide](https://docs.python.org/3/tutorial/venv.html)

---

**✅ Installation Complete!**

Selamat! Anda berhasil install Rainfall Clustering Dashboard.  
Mulai explore dan happy analyzing! 🌧️📊
