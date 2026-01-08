"""
🌧️ Rainfall Clustering Dashboard - Jawa Timur
Aplikasi visualisasi data clustering curah hujan dengan AI chatbot
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import folium
from streamlit_folium import st_folium
from datetime import datetime
import google.generativeai as genai
from config import *
import io

# Page Configuration
st.set_page_config(
    page_title="Rainfall Clustering Dashboard",
    page_icon="🌧️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk styling modern
st.markdown("""
<style>
    /* Main styling */
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(120deg, #FF4B4B, #4ECDC4, #45B7D1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0;
    }
    
    .subtitle {
        text-align: center;
        color: #888;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* Card styling */
    .metric-card {
        background: linear-gradient(135deg, rgba(255,75,75,0.1), rgba(78,205,196,0.1));
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 4px solid #FF4B4B;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
    }
    
    /* Chat styling */
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        animation: fadeIn 0.5s;
    }
    
    .user-message {
        background: rgba(78,205,196,0.2);
        border-left: 3px solid #4ECDC4;
    }
    
    .bot-message {
        background: rgba(69,183,209,0.2);
        border-left: 3px solid #45B7D1;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, rgba(255,75,75,0.05), rgba(78,205,196,0.05));
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(90deg, #FF4B4B, #4ECDC4);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(255,75,75,0.4);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* DataFrame styling */
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# ===== DATA LOADING =====
@st.cache_data
def load_data():
    """Load semua data yang diperlukan"""
    data = {
        'main': pd.read_csv('data_curah_hujan_clean.csv'),
        'cluster': pd.read_csv('hasil_cluster_final.csv'),
        'stats_cluster': pd.read_csv('clustering_output/statistik_boxplot_per_cluster_20260105-170452.csv'),
        'membership': pd.read_csv('clustering_output/tabel_keanggotaan_akhir_c3_m2.5.csv'),
        'medoid_distance': pd.read_csv('clustering_output/data_boxplot_jarak_ke_medoid.csv'),
        'yearly_stats': pd.read_csv('clustering_output/rata_rata_provinsi_per_tahun_20260105-170452.csv'),
        'yearly_cluster': pd.read_csv('clustering_output/rata_rata_tahun_x_cluster_20260105-170452.csv'),
        'evaluation': pd.read_csv('clustering_output/ringkasan_evaluasi_fcm.csv'),
        'objective': pd.read_csv('clustering_output/tabel_fungsi_objektif_per_iterasi.csv'),
        'outliers': pd.read_csv('data_understanding/outlier_per_wilayah.csv'),
    }
    
    # Parse tanggal
    data['main']['tanggal'] = pd.to_datetime(data['main']['tanggal'])
    
    # Merge dengan cluster
    data['main'] = data['main'].merge(data['cluster'], on='Wilayah', how='left')
    
    return data

# Load data
try:
    data = load_data()
    df = data['main']
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

# ===== SIDEBAR =====
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/rain.png", width=80)
    st.title("⚙️ Control Panel")
    
    # Navigation
    page = st.radio(
        "📍 Navigation",
        ["🏠 Dashboard", "🗺️ Interactive Map", "🤖 AI Chatbot", 
         "📈 Time Series", "🎯 Cluster Analysis", "🌧️ Rainfall Analytics",
         "📊 Statistical View", "🔍 Data Explorer", "📉 Performance Metrics"]
    )
    
    st.divider()
    
    # Filters
    st.subheader("🔧 Filters")
    
    # Date range
    min_date = df['tanggal'].min()
    max_date = df['tanggal'].max()
    date_range = st.date_input(
        "Periode",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Cluster filter
    selected_clusters = st.multiselect(
        "Cluster",
        options=[1, 2, 3],
        default=[1, 2, 3],
        format_func=lambda x: CLUSTER_NAMES[x]
    )
    
    # Wilayah filter
    all_wilayah = sorted(df['Wilayah'].unique())
    selected_wilayah = st.multiselect(
        "Wilayah",
        options=all_wilayah,
        default=all_wilayah[:5]
    )
    
    st.divider()
    
    # API Key Input untuk Gemini
    st.subheader("🔑 Gemini API")
    
    # Try to get API key from secrets (for deployment)
    try:
        default_api_key = st.secrets.get("GEMINI_API_KEY", "")
    except:
        default_api_key = ""
    
    api_key = st.text_input(
        "API Key",
        value=default_api_key,
        type="password",
        placeholder=GEMINI_API_KEY_PLACEHOLDER,
        help="Masukkan Google Gemini API Key atau set di Streamlit Secrets"
    )
    
    if api_key and api_key != GEMINI_API_KEY_PLACEHOLDER:
        try:
            genai.configure(api_key=api_key)
            st.success("✅ API Key connected!")
        except:
            st.error("❌ Invalid API Key")
    
    st.divider()
    
    # Info
    st.caption("📅 Last Updated: Jan 7, 2026")
    st.caption("📊 Data: 2022-2024")
    st.caption("🏢 38 Wilayah Jawa Timur")

# Filter data berdasarkan selection
if len(date_range) == 2:
    df_filtered = df[
        (df['tanggal'] >= pd.to_datetime(date_range[0])) &
        (df['tanggal'] <= pd.to_datetime(date_range[1])) &
        (df['Cluster'].isin(selected_clusters))
    ]
else:
    df_filtered = df[df['Cluster'].isin(selected_clusters)]

# ===== PAGE ROUTING =====

# 🏠 DASHBOARD OVERVIEW
if page == "🏠 Dashboard":
    # Header
    st.markdown('<h1 class="main-header">🌧️ Rainfall Clustering Dashboard</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Analisis Clustering Curah Hujan Jawa Timur 2022-2024</p>', unsafe_allow_html=True)
    
    # KPI Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="📍 Total Wilayah",
            value=df['Wilayah'].nunique(),
            delta="38 Kab/Kota"
        )
    
    with col2:
        st.metric(
            label="📅 Periode",
            value="3 Tahun",
            delta="2022-2024"
        )
    
    with col3:
        avg_rainfall = df_filtered['PRECTOTCORR'].mean()
        st.metric(
            label="🌧️ Avg Rainfall",
            value=f"{avg_rainfall:.2f} mm",
            delta=f"{avg_rainfall - df['PRECTOTCORR'].mean():.2f}"
        )
    
    with col4:
        st.metric(
            label="🎯 Clusters",
            value="3",
            delta="FCM Optimized"
        )
    
    st.divider()
    
    # Main visualizations
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.subheader("📊 Rainfall Distribution by Cluster")
        
        # Box plot
        fig = px.box(
            df_filtered,
            x='Cluster',
            y='PRECTOTCORR',
            color='Cluster',
            color_discrete_map=CLUSTER_COLORS,
            labels={'PRECTOTCORR': 'Curah Hujan (mm/hari)', 'Cluster': 'Cluster'},
            title="Distribusi Curah Hujan per Cluster"
        )
        fig.update_layout(
            showlegend=False,
            height=400,
            template='plotly_dark' if theme == "Dark" else 'plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col_right:
        st.subheader("🎯 Cluster Composition")
        
        # Pie chart
        cluster_counts = df_filtered.groupby('Cluster')['Wilayah'].nunique().reset_index()
        cluster_counts['Cluster_Name'] = cluster_counts['Cluster'].map(CLUSTER_NAMES)
        
        fig = px.pie(
            cluster_counts,
            values='Wilayah',
            names='Cluster_Name',
            color='Cluster',
            color_discrete_map=CLUSTER_COLORS,
            title="Jumlah Wilayah per Cluster"
        )
        fig.update_layout(
            height=400,
            template='plotly_dark' if theme == "Dark" else 'plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Time series trend
    st.subheader("📈 Rainfall Trend Over Time")
    
    monthly_avg = df_filtered.groupby([df_filtered['tanggal'].dt.to_period('M'), 'Cluster'])['PRECTOTCORR'].mean().reset_index()
    monthly_avg['tanggal'] = monthly_avg['tanggal'].dt.to_timestamp()
    monthly_avg['Cluster_Name'] = monthly_avg['Cluster'].map(CLUSTER_NAMES)
    
    fig = px.line(
        monthly_avg,
        x='tanggal',
        y='PRECTOTCORR',
        color='Cluster_Name',
        color_discrete_map={v: CLUSTER_COLORS[k] for k, v in CLUSTER_NAMES.items()},
        labels={'PRECTOTCORR': 'Rata-rata Curah Hujan (mm/hari)', 'tanggal': 'Tanggal'},
        title="Tren Curah Hujan Bulanan per Cluster"
    )
    fig.update_layout(
        height=400,
        hovermode='x unified',
        template='plotly_dark' if theme == "Dark" else 'plotly_white'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Statistics cards
    st.subheader("📊 Cluster Statistics")
    
    cols = st.columns(3)
    for idx, cluster in enumerate([1, 2, 3]):
        with cols[idx]:
            cluster_data = df_filtered[df_filtered['Cluster'] == cluster]['PRECTOTCORR']
            
            st.markdown(f"""
            <div class="metric-card">
                <h3 style="color: {CLUSTER_COLORS[cluster]};">{CLUSTER_NAMES[cluster]}</h3>
                <p><strong>Mean:</strong> {cluster_data.mean():.2f} mm/hari</p>
                <p><strong>Median:</strong> {cluster_data.median():.2f} mm/hari</p>
                <p><strong>Std Dev:</strong> {cluster_data.std():.2f}</p>
                <p><strong>Max:</strong> {cluster_data.max():.2f} mm/hari</p>
                <p><strong>Records:</strong> {len(cluster_data):,}</p>
            </div>
            """, unsafe_allow_html=True)

# 🗺️ INTERACTIVE MAP
elif page == "🗺️ Interactive Map":
    st.header("🗺️ Interactive Clustering Map")
    st.markdown("Peta interaktif Jawa Timur dengan marker clustering berdasarkan curah hujan")
    
    # Compute stats per wilayah
    wilayah_stats = df_filtered.groupby(['Wilayah', 'Cluster']).agg({
        'PRECTOTCORR': ['mean', 'max', 'count']
    }).reset_index()
    wilayah_stats.columns = ['Wilayah', 'Cluster', 'Mean', 'Max', 'Count']
    
    # Create map
    m = folium.Map(
        location=JATIM_CENTER,
        zoom_start=JATIM_ZOOM,
        tiles='OpenStreetMap'
    )
    
    # Add markers
    for _, row in wilayah_stats.iterrows():
        wilayah = row['Wilayah']
        cluster = row['Cluster']
        
        if wilayah in COORDINATES:
            lat, lon = COORDINATES[wilayah]
            
            # Popup content
            popup_html = f"""
            <div style="font-family: Arial; width: 200px;">
                <h4 style="color: {CLUSTER_COLORS[cluster]}; margin-bottom: 5px;">{wilayah}</h4>
                <hr style="margin: 5px 0;">
                <p><strong>Cluster:</strong> {CLUSTER_NAMES[cluster]}</p>
                <p><strong>Rata-rata:</strong> {row['Mean']:.2f} mm/hari</p>
                <p><strong>Maksimum:</strong> {row['Max']:.2f} mm/hari</p>
                <p><strong>Data Points:</strong> {row['Count']:,}</p>
            </div>
            """
            
            folium.CircleMarker(
                location=[lat, lon],
                radius=10 + (row['Mean'] / 2),
                popup=folium.Popup(popup_html, max_width=300),
                tooltip=wilayah,
                color=CLUSTER_COLORS[cluster],
                fill=True,
                fillColor=CLUSTER_COLORS[cluster],
                fillOpacity=0.7,
                weight=2
            ).add_to(m)
    
    # Add legend
    legend_html = f"""
    <div style="position: fixed; 
                bottom: 50px; right: 50px; width: 220px; height: auto; 
                background-color: white; z-index:9999; font-size:14px;
                border:2px solid grey; border-radius: 10px; padding: 15px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        <p style="margin-bottom: 10px; color: #000; font-weight: bold;">Legend:</p>
        <p style="color: #000; margin: 5px 0;"><span style="color: {CLUSTER_COLORS[1]}; font-size: 20px;">●</span> {CLUSTER_NAMES[1]}</p>
        <p style="color: #000; margin: 5px 0;"><span style="color: {CLUSTER_COLORS[2]}; font-size: 20px;">●</span> {CLUSTER_NAMES[2]}</p>
        <p style="color: #000; margin: 5px 0;"><span style="color: {CLUSTER_COLORS[3]}; font-size: 20px;">●</span> {CLUSTER_NAMES[3]}</p>
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))
    
    # Display map
    st_folium(m, width=1400, height=600)
    
    st.divider()
    
    # Map statistics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("📍 Wilayah Ditampilkan", len(wilayah_stats))
    
    with col2:
        highest_rainfall = wilayah_stats.loc[wilayah_stats['Mean'].idxmax()]
        st.metric("🌧️ Tertinggi", f"{highest_rainfall['Wilayah'][:20]}...", f"{highest_rainfall['Mean']:.2f} mm")
    
    with col3:
        lowest_rainfall = wilayah_stats.loc[wilayah_stats['Mean'].idxmin()]
        st.metric("☀️ Terendah", f"{lowest_rainfall['Wilayah'][:20]}...", f"{lowest_rainfall['Mean']:.2f} mm")

# 🤖 AI CHATBOT
elif page == "🤖 AI Chatbot":
    st.header("🤖 AI Assistant - Gemini")
    st.markdown("Tanyakan apapun tentang data curah hujan Jawa Timur!")
    
    if not api_key or api_key == GEMINI_API_KEY_PLACEHOLDER:
        st.warning("⚠️ Mohon masukkan Gemini API Key di sidebar untuk menggunakan chatbot")
        st.info("💡 Dapatkan API Key gratis di: https://aistudio.google.com/app/apikey")
        
        # Demo mode
        st.subheader("🎭 Demo Mode")
        st.markdown("Contoh pertanyaan yang bisa Anda tanyakan:")
        
        demo_questions = [
            "Cluster mana yang memiliki curah hujan tertinggi?",
            "Bagaimana tren curah hujan dari 2022 ke 2024?",
            "Wilayah mana yang rawan banjir?",
            "Apa karakteristik Cluster 1?",
            "Kapan musim hujan di Jawa Timur?",
        ]
        
        for q in demo_questions:
            st.markdown(f"- ❓ {q}")
    
    else:
        # Test API connection and show available models
        try:
            genai.configure(api_key=api_key)
            
            # Try to list models
            try:
                with st.expander("ℹ️ Available Models"):
                    models = genai.list_models()
                    available_models = [m.name for m in models if 'generateContent' in m.supported_generation_methods]
                    st.write("Models yang mendukung generateContent:")
                    for model in available_models[:5]:  # Show first 5
                        st.code(model)
            except:
                pass
                
        except Exception as e:
            st.error(f"❌ API Key Error: {e}")
            st.stop()
        
        # Initialize chat history
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        
        # Prepare comprehensive data context
        # Cluster statistics
        cluster_stats = df_filtered.groupby('Cluster')['PRECTOTCORR'].agg(['mean', 'median', 'std', 'min', 'max', 'count']).round(2)
        
        # Wilayah per cluster
        cluster_wilayah = {}
        for cluster in [1, 2, 3]:
            wilayah_list = data['cluster'][data['cluster']['Cluster'] == cluster]['Wilayah'].tolist()
            cluster_wilayah[cluster] = wilayah_list
        
        # Yearly trend
        yearly_avg = df.groupby('YEAR')['PRECTOTCORR'].mean().round(2).to_dict()
        
        # Monthly pattern
        monthly_avg = df.groupby('MO')['PRECTOTCORR'].mean().round(2).to_dict()
        
        # Extreme events
        extreme_count = len(df[df['PRECTOTCORR'] > 100])
        drought_count = len(df[df['PRECTOTCORR'] < 1])
        
        # Top 5 highest and lowest rainfall regions
        wilayah_avg = df.groupby('Wilayah')['PRECTOTCORR'].mean().round(2)
        top_5 = wilayah_avg.nlargest(5).to_dict()
        bottom_5 = wilayah_avg.nsmallest(5).to_dict()
        
        # Medoid info
        medoid_info = """
        Medoid (pusat cluster):
        - Cluster 1: Kabupaten Kediri (representatif cluster curah hujan sedang)
        - Cluster 2: Kabupaten Magetan (representatif cluster curah hujan sedang-tinggi)
        - Cluster 3: Kabupaten Blitar (representatif cluster curah hujan tinggi)
        """
        
        # Evaluation metrics
        eval_metrics = f"""
        Performa Clustering (Fuzzy C-Medoid):
        - Xie-Beni Index: {data['evaluation']['XieBeni'].min():.4f} (semakin kecil semakin baik)
        - Parameter m optimal: {data['evaluation'].loc[data['evaluation']['XieBeni'].idxmin(), 'm']}
        - Konvergensi: {int(data['evaluation'].iloc[0]['Iterations'])} iterasi
        """
        
        # Build comprehensive context
        data_context = f"""
Anda adalah AI Expert untuk Analisis Data Curah Hujan Jawa Timur dengan pengetahuan mendalam tentang data clustering ini.

=== INFORMASI DATASET ===
📅 Periode: 2022-2024 (1,096 hari observasi)
📍 Wilayah: 38 Kabupaten/Kota Jawa Timur
📊 Total Records: {len(df):,} data points
🌧️ Sumber: NASA POWER (PRECTOTCORR)

=== STATISTIK UMUM ===
- Rata-rata: {df['PRECTOTCORR'].mean():.2f} mm/hari
- Median: {df['PRECTOTCORR'].median():.2f} mm/hari
- Std Dev: {df['PRECTOTCORR'].std():.2f} mm/hari
- Minimum: {df['PRECTOTCORR'].min():.2f} mm/hari
- Maksimum: {df['PRECTOTCORR'].max():.2f} mm/hari
- Extreme Events (>100mm): {extreme_count} kejadian
- Drought Days (<1mm): {drought_count} hari

=== TREND TAHUNAN ===
{chr(10).join([f"- {year}: {avg:.2f} mm/hari" for year, avg in yearly_avg.items()])}

=== POLA BULANAN (Rata-rata) ===
Bulan dengan curah hujan tertinggi dan terendah:
- Tertinggi: Bulan {max(monthly_avg, key=monthly_avg.get)} ({monthly_avg[max(monthly_avg, key=monthly_avg.get)]:.2f} mm/hari)
- Terendah: Bulan {min(monthly_avg, key=monthly_avg.get)} ({monthly_avg[min(monthly_avg, key=monthly_avg.get)]:.2f} mm/hari)

=== CLUSTERING RESULTS (FCM) ===
Algoritma: Fuzzy C-Medoid
Jumlah Cluster: 3

{medoid_info}

CLUSTER 1 - {len(cluster_wilayah[1])} wilayah:
Statistik: Mean={cluster_stats.loc[1, 'mean']:.2f}, Median={cluster_stats.loc[1, 'median']:.2f}, Std={cluster_stats.loc[1, 'std']:.2f}, Range=[{cluster_stats.loc[1, 'min']:.2f}-{cluster_stats.loc[1, 'max']:.2f}]
Wilayah: {', '.join(cluster_wilayah[1][:10])}{'...' if len(cluster_wilayah[1]) > 10 else ''}
Karakteristik: Curah hujan SEDANG, variasi cukup stabil

CLUSTER 2 - {len(cluster_wilayah[2])} wilayah:
Statistik: Mean={cluster_stats.loc[2, 'mean']:.2f}, Median={cluster_stats.loc[2, 'median']:.2f}, Std={cluster_stats.loc[2, 'std']:.2f}, Range=[{cluster_stats.loc[2, 'min']:.2f}-{cluster_stats.loc[2, 'max']:.2f}]
Wilayah: {', '.join(cluster_wilayah[2][:10])}{'...' if len(cluster_wilayah[2]) > 10 else ''}
Karakteristik: Curah hujan SEDANG-TINGGI, lebih bervariasi

CLUSTER 3 - {len(cluster_wilayah[3])} wilayah:
Statistik: Mean={cluster_stats.loc[3, 'mean']:.2f}, Median={cluster_stats.loc[3, 'median']:.2f}, Std={cluster_stats.loc[3, 'std']:.2f}, Range=[{cluster_stats.loc[3, 'min']:.2f}-{cluster_stats.loc[3, 'max']:.2f}]
Wilayah: {', '.join(cluster_wilayah[3][:10])}{'...' if len(cluster_wilayah[3]) > 10 else ''}
Karakteristik: Curah hujan TINGGI, variasi paling besar

=== WILAYAH EKSTREM ===
🌧️ Top 5 Curah Hujan Tertinggi:
{chr(10).join([f"- {wilayah}: {avg:.2f} mm/hari" for wilayah, avg in top_5.items()])}

☀️ Top 5 Curah Hujan Terendah:
{chr(10).join([f"- {wilayah}: {avg:.2f} mm/hari" for wilayah, avg in bottom_5.items()])}

{eval_metrics}

=== INSIGHT & REKOMENDASI ===
1. Tren Menurun: Curah hujan menurun dari 2022 ke 2024 (climate change?)
2. Cluster 3 paling rawan banjir (curah hujan tinggi & variasi besar)
3. Wilayah pesisir utara (Cluster 1) cenderung lebih kering
4. Musim hujan peak: Desember-Februari
5. Musim kering: Juli-September

=== CARA MENJAWAB ===
- Jawab dengan data spesifik dan angka yang akurat dari context ini
- Gunakan emoji untuk readability
- Berikan insight mendalam, bukan hanya statistik mentah
- Jika ditanya tentang wilayah spesifik, cek cluster-nya terlebih dahulu
- Jelaskan implikasi praktis (mitigasi banjir, pertanian, dll)
- Ringkas tapi informatif, max 200 kata per jawaban

        """
        
        # Display chat history
        for message in st.session_state.chat_history:
            if message['role'] == 'user':
                st.markdown(f'<div class="chat-message user-message">👤 <strong>You:</strong> {message["content"]}</div>', 
                           unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-message bot-message">🤖 <strong>AI:</strong> {message["content"]}</div>', 
                           unsafe_allow_html=True)
        
        # Chat input
        user_input = st.chat_input("Tanyakan sesuatu tentang data curah hujan...")
        
        if user_input:
            # Add user message
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            
            try:
                # Generate response - using Gemini 2.x models
                model_names = [
                    'models/gemini-2.5-flash',
                    'models/gemini-2.5-pro',
                    'models/gemini-2.0-flash-exp',
                    'models/gemini-2.0-flash',
                    'gemini-2.5-flash',
                    'gemini-2.0-flash'
                ]
                
                ai_response = None
                last_error = None
                
                for model_name in model_names:
                    try:
                        model = genai.GenerativeModel(model_name)
                        response = model.generate_content(f"{data_context}\n\nPertanyaan: {user_input}")
                        ai_response = response.text
                        break
                    except Exception as e:
                        last_error = str(e)
                        continue
                
                if ai_response is None:
                    raise Exception(f"Semua model gagal. Last error: {last_error}")
                
                # Add AI response
                st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
                
                st.rerun()
                
            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.info("💡 Cek available models di expander di atas atau verifikasi API key Anda")
                st.info("🔗 Generate new API key: https://aistudio.google.com/app/apikey")
        
        # Clear chat button
        if st.button("🗑️ Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()

# 📈 TIME SERIES ANALYSIS
elif page == "📈 Time Series":
    st.header("📈 Time Series Analysis")
    
    # Wilayah selector
    selected_regions = st.multiselect(
        "Pilih Wilayah untuk Analisis",
        options=all_wilayah,
        default=all_wilayah[:3]
    )
    
    if selected_regions:
        df_regions = df_filtered[df_filtered['Wilayah'].isin(selected_regions)]
        
        # Time series line chart
        fig = px.line(
            df_regions,
            x='tanggal',
            y='PRECTOTCORR',
            color='Wilayah',
            title="Curah Hujan Harian per Wilayah",
            labels={'PRECTOTCORR': 'Curah Hujan (mm/hari)', 'tanggal': 'Tanggal'}
        )
        fig.update_layout(
            height=500,
            hovermode='x unified',
            template='plotly_dark' if theme == "Dark" else 'plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.divider()
        
        # Monthly aggregation
        st.subheader("📊 Monthly Average")
        
        monthly = df_regions.groupby([df_regions['tanggal'].dt.to_period('M'), 'Wilayah'])['PRECTOTCORR'].mean().reset_index()
        monthly['tanggal'] = monthly['tanggal'].dt.to_timestamp()
        
        fig = go.Figure()
        for wilayah in selected_regions:
            data_w = monthly[monthly['Wilayah'] == wilayah]
            fig.add_trace(go.Bar(
                x=data_w['tanggal'],
                y=data_w['PRECTOTCORR'],
                name=wilayah
            ))
        
        fig.update_layout(
            title="Rata-rata Curah Hujan Bulanan",
            xaxis_title="Bulan",
            yaxis_title="Curah Hujan (mm/hari)",
            barmode='group',
            height=400,
            template='plotly_dark' if theme == "Dark" else 'plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    else:
        st.info("Pilih minimal 1 wilayah untuk analisis")

# 🎯 CLUSTER ANALYSIS
elif page == "🎯 Cluster Analysis":
    st.header("🎯 Cluster Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Membership Degree")
        
        # Membership visualization
        membership_display = data['membership'][['Kabupaten/Kota', 'cluster_1', 'cluster_2', 'cluster_3', 'Cluster']].head(10)
        
        fig = go.Figure()
        fig.add_trace(go.Bar(name='Cluster 1', x=membership_display['Kabupaten/Kota'], 
                            y=membership_display['cluster_1'], marker_color=CLUSTER_COLORS[1]))
        fig.add_trace(go.Bar(name='Cluster 2', x=membership_display['Kabupaten/Kota'], 
                            y=membership_display['cluster_2'], marker_color=CLUSTER_COLORS[2]))
        fig.add_trace(go.Bar(name='Cluster 3', x=membership_display['Kabupaten/Kota'], 
                            y=membership_display['cluster_3'], marker_color=CLUSTER_COLORS[3]))
        
        fig.update_layout(
            barmode='stack',
            height=400,
            xaxis_tickangle=-45,
            template='plotly_dark' if theme == "Dark" else 'plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📏 Distance to Medoid")
        
        fig = px.box(
            data['medoid_distance'],
            x='Cluster',
            y='Jarak ke Medoid',
            color='Cluster',
            color_discrete_map=CLUSTER_COLORS,
            title="Distribusi Jarak ke Medoid"
        )
        fig.update_layout(
            showlegend=False,
            height=400,
            template='plotly_dark' if theme == "Dark" else 'plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Scatter plot 3D
    st.subheader("🎲 3D Cluster Visualization")
    
    # Aggregate data untuk scatter
    scatter_data = df_filtered.groupby(['Wilayah', 'Cluster']).agg({
        'PRECTOTCORR': ['mean', 'std', 'max']
    }).reset_index()
    scatter_data.columns = ['Wilayah', 'Cluster', 'Mean', 'Std', 'Max']
    scatter_data['Cluster_Name'] = scatter_data['Cluster'].map(CLUSTER_NAMES)
    
    fig = px.scatter_3d(
        scatter_data,
        x='Mean',
        y='Std',
        z='Max',
        color='Cluster_Name',
        color_discrete_map={v: CLUSTER_COLORS[k] for k, v in CLUSTER_NAMES.items()},
        hover_name='Wilayah',
        title="3D Scatter Plot: Mean vs Std vs Max Rainfall",
        labels={'Mean': 'Mean (mm)', 'Std': 'Std Dev (mm)', 'Max': 'Max (mm)'}
    )
    fig.update_layout(
        height=600,
        template='plotly_dark' if theme == "Dark" else 'plotly_white'
    )
    st.plotly_chart(fig, use_container_width=True)

# 🌧️ RAINFALL ANALYTICS
elif page == "🌧️ Rainfall Analytics":
    st.header("🌧️ Rainfall Analytics")
    
    # Heatmap
    st.subheader("🔥 Monthly Rainfall Heatmap")
    
    heatmap_data = df_filtered.pivot_table(
        values='PRECTOTCORR',
        index=df_filtered['tanggal'].dt.month,
        columns=df_filtered['tanggal'].dt.year,
        aggfunc='mean'
    )
    
    fig = px.imshow(
        heatmap_data,
        labels=dict(x="Tahun", y="Bulan", color="Curah Hujan (mm)"),
        y=['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'],
        color_continuous_scale='Blues',
        title="Rata-rata Curah Hujan Bulanan"
    )
    fig.update_layout(
        height=400,
        template='plotly_dark' if theme == "Dark" else 'plotly_white'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Extreme events
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("⚠️ Extreme Events (>100mm)")
        
        extreme_events = df_filtered[df_filtered['PRECTOTCORR'] > 100].copy()
        extreme_events = extreme_events.sort_values('PRECTOTCORR', ascending=False)
        
        st.dataframe(
            extreme_events[['tanggal', 'Wilayah', 'PRECTOTCORR', 'Cluster']].head(20),
            use_container_width=True
        )
        
        st.metric("Total Extreme Events", len(extreme_events))
    
    with col2:
        st.subheader("☀️ Drought Days (<1mm)")
        
        drought_days = df_filtered[df_filtered['PRECTOTCORR'] < 1]
        drought_by_wilayah = drought_days.groupby('Wilayah').size().reset_index(name='Days')
        drought_by_wilayah = drought_by_wilayah.sort_values('Days', ascending=False).head(10)
        
        fig = px.bar(
            drought_by_wilayah,
            x='Days',
            y='Wilayah',
            orientation='h',
            title="Top 10 Wilayah dengan Hari Kering Terbanyak",
            color='Days',
            color_continuous_scale='Oranges'
        )
        fig.update_layout(
            height=400,
            showlegend=False,
            template='plotly_dark' if theme == "Dark" else 'plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Rainfall intensity distribution
    st.subheader("📊 Rainfall Intensity Distribution")
    
    def classify_intensity(value):
        for intensity, (min_val, max_val) in RAINFALL_INTENSITY.items():
            if min_val <= value < max_val:
                return intensity
        return "Extreme"
    
    df_filtered['Intensity'] = df_filtered['PRECTOTCORR'].apply(classify_intensity)
    
    intensity_counts = df_filtered['Intensity'].value_counts()
    
    fig = px.pie(
        values=intensity_counts.values,
        names=intensity_counts.index,
        title="Distribusi Intensitas Curah Hujan",
        color=intensity_counts.index,
        color_discrete_map=INTENSITY_COLORS
    )
    fig.update_layout(
        height=400,
        template='plotly_dark' if theme == "Dark" else 'plotly_white'
    )
    st.plotly_chart(fig, use_container_width=True)

# 📊 STATISTICAL VIEW
elif page == "📊 Statistical View":
    st.header("📊 Statistical Dashboard")
    
    # Violin plot
    st.subheader("🎻 Violin Plot per Cluster")
    
    fig = px.violin(
        df_filtered,
        x='Cluster',
        y='PRECTOTCORR',
        color='Cluster',
        color_discrete_map=CLUSTER_COLORS,
        box=True,
        title="Distribusi Curah Hujan per Cluster (Violin Plot)"
    )
    fig.update_layout(
        showlegend=False,
        height=400,
        template='plotly_dark' if theme == "Dark" else 'plotly_white'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Histogram
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Histogram")
        
        fig = px.histogram(
            df_filtered,
            x='PRECTOTCORR',
            color='Cluster',
            color_discrete_map=CLUSTER_COLORS,
            nbins=50,
            title="Distribusi Frekuensi Curah Hujan",
            labels={'PRECTOTCORR': 'Curah Hujan (mm/hari)'}
        )
        fig.update_layout(
            height=400,
            template='plotly_dark' if theme == "Dark" else 'plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📊 Outliers Analysis")
        
        fig = px.bar(
            data['outliers'].sort_values('Jumlah Outlier', ascending=False).head(15),
            x='Jumlah Outlier',
            y='Wilayah',
            orientation='h',
            title="Top 15 Wilayah dengan Outlier Terbanyak",
            color='Jumlah Outlier',
            color_continuous_scale='Reds'
        )
        fig.update_layout(
            height=400,
            showlegend=False,
            template='plotly_dark' if theme == "Dark" else 'plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Correlation heatmap
    st.subheader("🔗 Correlation Analysis")
    
    # Pivot data untuk korelasi antar wilayah
    pivot_data = df_filtered.pivot_table(
        values='PRECTOTCORR',
        index='tanggal',
        columns='Wilayah',
        aggfunc='mean'
    )
    
    if len(selected_wilayah) > 1 and len(selected_wilayah) <= 10:
        corr_matrix = pivot_data[selected_wilayah].corr()
        
        fig = px.imshow(
            corr_matrix,
            text_auto='.2f',
            color_continuous_scale='RdBu_r',
            title="Correlation Matrix - Curah Hujan antar Wilayah",
            zmin=-1, zmax=1
        )
        fig.update_layout(
            height=500,
            template='plotly_dark' if theme == "Dark" else 'plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Pilih 2-10 wilayah di sidebar untuk melihat correlation matrix")

# 🔍 DATA EXPLORER
elif page == "🔍 Data Explorer":
    st.header("🔍 Data Explorer")
    
    # Search and filter
    col1, col2, col3 = st.columns(3)
    
    with col1:
        search_wilayah = st.text_input("🔎 Search Wilayah", "")
    
    with col2:
        min_rainfall = st.number_input("Min Rainfall (mm)", 0.0, float(df['PRECTOTCORR'].max()), 0.0)
    
    with col3:
        max_rainfall = st.number_input("Max Rainfall (mm)", 0.0, float(df['PRECTOTCORR'].max()), 
                                       float(df['PRECTOTCORR'].max()))
    
    # Apply filters
    df_explorer = df_filtered[
        (df_filtered['Wilayah'].str.contains(search_wilayah, case=False)) &
        (df_filtered['PRECTOTCORR'] >= min_rainfall) &
        (df_filtered['PRECTOTCORR'] <= max_rainfall)
    ]
    
    # Display data
    st.subheader(f"📋 Data ({len(df_explorer):,} records)")
    
    st.dataframe(
        df_explorer[['tanggal', 'Wilayah', 'PRECTOTCORR', 'Cluster', 'nama_bulan']].sort_values('tanggal', ascending=False),
        use_container_width=True,
        height=400
    )
    
    # Download buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        csv = df_explorer.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name=f"rainfall_data_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    
    with col2:
        # Excel download
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df_explorer.to_excel(writer, index=False, sheet_name='Data')
        excel_data = output.getvalue()
        
        st.download_button(
            label="📥 Download Excel",
            data=excel_data,
            file_name=f"rainfall_data_{datetime.now().strftime('%Y%m%d')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    
    with col3:
        st.metric("Filtered Records", f"{len(df_explorer):,}")
    
    st.divider()
    
    # Summary statistics
    st.subheader("📊 Summary Statistics")
    
    summary_stats = df_explorer.groupby('Cluster')['PRECTOTCORR'].agg([
        ('Count', 'count'),
        ('Mean', 'mean'),
        ('Median', 'median'),
        ('Std', 'std'),
        ('Min', 'min'),
        ('Max', 'max')
    ]).reset_index()
    
    st.dataframe(summary_stats.style.format({
        'Mean': '{:.2f}',
        'Median': '{:.2f}',
        'Std': '{:.2f}',
        'Min': '{:.2f}',
        'Max': '{:.2f}'
    }), use_container_width=True)

# 📉 PERFORMANCE METRICS
elif page == "📉 Performance Metrics":
    st.header("📉 Clustering Performance Metrics")
    
    # Evaluation metrics
    col1, col2, col3 = st.columns(3)
    
    eval_data = data['evaluation'].iloc[0]
    
    with col1:
        st.metric(
            label="🎯 Optimal Clusters",
            value=int(eval_data['c']),
            delta="Best Configuration"
        )
    
    with col2:
        st.metric(
            label="📊 Fuzziness (m)",
            value=eval_data['m'],
            delta="Optimal"
        )
    
    with col3:
        st.metric(
            label="✅ Xie-Beni Index",
            value=f"{eval_data['XieBeni']:.4f}",
            delta="Lower is Better",
            delta_color="inverse"
        )
    
    st.divider()
    
    # Tuning comparison
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔧 Parameter Tuning Results")
        
        fig = px.bar(
            data['evaluation'],
            x='m',
            y='XieBeni',
            color='m',
            title="Xie-Beni Index untuk berbagai nilai m",
            labels={'m': 'Fuzziness Parameter (m)', 'XieBeni': 'Xie-Beni Index'},
            text='XieBeni'
        )
        fig.update_traces(texttemplate='%{text:.4f}', textposition='outside')
        fig.update_layout(
            showlegend=False,
            height=400,
            template='plotly_dark' if theme == "Dark" else 'plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📈 Objective Function")
        
        fig = px.line(
            data['objective'],
            x='Iterasi ke-',
            y='Nilai Fungsi Objektif',
            markers=True,
            title="Konvergensi Fungsi Objektif",
            labels={'Iterasi ke-': 'Iterasi', 'Nilai Fungsi Objektif': 'Objective Function'}
        )
        fig.update_layout(
            height=400,
            template='plotly_dark' if theme == "Dark" else 'plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Performance table
    st.subheader("📋 Detailed Evaluation")
    
    st.dataframe(
        data['evaluation'].style.format({
            'J': '{:.2f}',
            'XieBeni': '{:.4f}',
            'm': '{:.1f}'
        }),
        use_container_width=True
    )
    
    # Insights
    st.subheader("💡 Key Insights")
    
    best_config = data['evaluation'].loc[data['evaluation']['XieBeni'].idxmin()]
    
    st.markdown(f"""
    - ✅ **Best Configuration**: c={int(best_config['c'])}, m={best_config['m']}
    - 📊 **Xie-Beni Index**: {best_config['XieBeni']:.4f} (semakin kecil semakin baik)
    - 🔄 **Iterations**: {int(best_config['Iterations'])} iterasi hingga konvergen
    - ✔️ **Convergence**: {'Ya' if best_config['Converged'] else 'Tidak'}
    - 🎯 **Objective Function**: {best_config['J']:.2f}
    """)

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #888; padding: 20px;">
    <p>🌧️ <strong>Rainfall Clustering Dashboard</strong> | Developed with ❤️ using Streamlit</p>
    <p>📊 Data Source: NASA POWER | 🎯 Algorithm: Fuzzy C-Medoid</p>
    <p>© 2026 | Jawa Timur Rainfall Analysis</p>
</div>
""", unsafe_allow_html=True)
