# 🚀 Deployment Guide - Rainfall Clustering Dashboard

## 📋 Pilihan Platform Deployment

### 1. **Streamlit Cloud** (RECOMMENDED - FREE & MUDAH)

#### ✅ Kelebihan:
- ✨ **100% GRATIS** untuk public apps
- 🚀 Deploy langsung dari GitHub
- ⚡ Auto-deploy setiap push
- 🔒 Support secrets untuk API keys
- 💾 1 GB RAM, 1 CPU core

#### 📝 Langkah-langkah:

**A. Persiapan GitHub**
```bash
# 1. Buat repository baru di GitHub
# 2. Push code ke GitHub
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/USERNAME/rainfall-dashboard.git
git push -u origin main
```

**B. Deploy ke Streamlit Cloud**
1. Buka https://share.streamlit.io/
2. Login dengan GitHub
3. Klik "New app"
4. Pilih repository: `rainfall-dashboard`
5. Branch: `main`
6. Main file path: `app.py`
7. Klik "Deploy"

**C. Setup Secrets (API Key)**
1. Di dashboard Streamlit Cloud, klik app Anda
2. Klik "⚙️ Settings" → "Secrets"
3. Tambahkan:
```toml
GEMINI_API_KEY = "your_actual_api_key_here"
```

**D. Update app.py untuk baca secrets:**
```python
# Tambahkan di bagian API key input
import streamlit as st

# Coba baca dari secrets dulu
try:
    default_api_key = st.secrets.get("GEMINI_API_KEY", GEMINI_API_KEY_PLACEHOLDER)
except:
    default_api_key = GEMINI_API_KEY_PLACEHOLDER

api_key = st.text_input(
    "API Key",
    value=default_api_key if default_api_key != GEMINI_API_KEY_PLACEHOLDER else "",
    type="password",
    placeholder=GEMINI_API_KEY_PLACEHOLDER,
    help="Masukkan Google Gemini API Key"
)
```

---

### 2. **Railway** (FREE $5/month credit)

#### 📝 Langkah-langkah:

```bash
# 1. Install Railway CLI
npm install -g @railway/cli

# 2. Login
railway login

# 3. Initialize project
railway init

# 4. Deploy
railway up
```

**Tambahkan Procfile:**
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

---

### 3. **Heroku** (Paid - $5/month)

#### 📝 Langkah-langkah:

**A. Buat file Procfile:**
```bash
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
```

**B. Buat setup.sh:**
```bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

**C. Deploy:**
```bash
# Install Heroku CLI dari heroku.com
heroku login
heroku create rainfall-dashboard
git push heroku main
heroku config:set GEMINI_API_KEY=your_api_key
heroku open
```

---

### 4. **Docker** (Self-hosted)

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Deploy:**
```bash
# Build
docker build -t rainfall-dashboard .

# Run
docker run -p 8501:8501 rainfall-dashboard
```

---

### 5. **Vercel** (FREE)

**vercel.json:**
```json
{
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

---

## 🔧 File yang Diperlukan untuk Deployment

### 1. **requirements.txt** ✅ (Sudah ada)
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

### 2. **runtime.txt** (Optional untuk Heroku)
```txt
python-3.11.7
```

### 3. **.gitignore**
```
.venv/
__pycache__/
*.pyc
.env
.streamlit/secrets.toml
*.log
.DS_Store
```

---

## 🎯 REKOMENDASI: Streamlit Cloud

### Kenapa Streamlit Cloud?
✅ **GRATIS** untuk unlimited public apps  
✅ **Tidak perlu setup server**  
✅ **Auto SSL/HTTPS**  
✅ **Auto-deploy dari GitHub**  
✅ **Built-in untuk Streamlit apps**  
✅ **Support secrets management**  
✅ **Cocok untuk data science projects**  

### URL Setelah Deploy:
```
https://USERNAME-rainfall-dashboard-app-xxxxx.streamlit.app
```

---

## 📊 Performa & Limits

| Platform | RAM | Storage | Bandwidth | Price |
|----------|-----|---------|-----------|-------|
| Streamlit Cloud | 1 GB | 1 GB | Unlimited | FREE |
| Railway | 8 GB | 100 GB | 100 GB/month | FREE ($5 credit) |
| Heroku | 512 MB | Unlimited | Unlimited | $5/month |
| Vercel | 1 GB | 100 GB | 100 GB/month | FREE |

---

## 🔒 Security Best Practices

1. **Jangan commit API keys** ke GitHub
2. **Gunakan environment variables** atau secrets
3. **Tambahkan .gitignore** untuk file sensitive
4. **Enable authentication** jika perlu (Streamlit Auth)
5. **Regular update dependencies** untuk security patches

---

## 🐛 Troubleshooting

### Error: ModuleNotFoundError
**Solusi:** Pastikan semua packages ada di `requirements.txt`

### Error: Memory Exceeded
**Solusi:** 
- Gunakan `@st.cache_data` untuk caching
- Reduce data size atau sample data
- Upgrade plan

### Error: File Not Found
**Solusi:** 
- Pastikan semua data files ter-commit ke Git
- Check file paths (gunakan relative paths)

### Slow Loading
**Solusi:**
```python
# Tambahkan di app.py
@st.cache_data
def load_data():
    # ... loading code
    return data
```

---

## 📞 Support

- Streamlit Cloud: https://discuss.streamlit.io/
- Docs: https://docs.streamlit.io/streamlit-community-cloud
- Status: https://streamlit.statuspage.io/

---

**🎉 Happy Deploying!**
