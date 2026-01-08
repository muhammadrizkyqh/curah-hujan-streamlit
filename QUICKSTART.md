# 🚀 Quick Deploy to Streamlit Cloud

## Step 1: Push ke GitHub

```bash
# Initialize Git (jika belum)
git init

# Add all files
git add .

# Commit
git commit -m "Deploy rainfall dashboard"

# Create GitHub repo, lalu:
git remote add origin https://github.com/USERNAME/rainfall-dashboard.git
git branch -M main
git push -u origin main
```

## Step 2: Deploy ke Streamlit Cloud

1. **Buka** https://share.streamlit.io/
2. **Login** dengan GitHub account
3. **Klik** "New app"
4. **Pilih**:
   - Repository: `rainfall-dashboard`
   - Branch: `main`
   - Main file: `app.py`
5. **Klik** "Deploy"

## Step 3: Setup API Key (Optional)

Setelah app deploy:

1. Klik **Settings** (⚙️) di dashboard
2. Pilih **Secrets**
3. Paste ini:
```toml
GEMINI_API_KEY = "your_actual_gemini_api_key_here"
```
4. Klik **Save**

## Done! 🎉

Your app akan tersedia di:
```
https://USERNAME-rainfall-dashboard-xxxxx.streamlit.app
```

---

## Troubleshooting

**Error: Module not found**
- Pastikan `requirements.txt` ter-commit

**Error: File not found**
- Pastikan semua file CSV ter-commit
- Check di GitHub apakah semua file ada

**Slow loading**
- Normal untuk first load (cold start)
- Subsequent loads akan lebih cepat

**Need help?**
- Docs: https://docs.streamlit.io/streamlit-community-cloud
- Community: https://discuss.streamlit.io/
