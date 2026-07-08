import streamlit as st
import pandas as pd
import numpy as np
import time

# ── 1. CONFIG & SETUP HALAMAN ────────────────────────────────────────────────
st.set_page_config(
    page_title="RAGeni — AI Data Science Assistant",
    page_icon="🤖",
    layout="wide"
)

# Inisialisasi session state untuk chat history jika belum ada
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Halo! Saya RAGeni. Unggah dataset Anda di sidebar atau tanyakan teori data science kepada saya!"}
    ]

# ── 2. SIDEBAR CONTROL CENTER (Edukasi & Parameter) ──────────────────────────
with st.sidebar:
    st.title("RAGeni Control Center ⚙️")
    st.write("Modul asisten data science bertenaga RAG & Gemini AI.")
    
    st.markdown("---")
    st.subheader("📁 1. Unggah Dataset (CSV)")
    uploaded_file = st.file_uploader("Pilih file data untuk dianalisis", type=["csv"])
    
    st.markdown("---")
    st.subheader("🧠 2. Parameter RAG & LLM")
    model_mode = st.selectbox("Pilih Model:", ["Gemini 1.5 Flash (Rekomendasi)", "Gemini 1.5 Pro"])
    rag_context = st.checkbox("Aktifkan Konteks Buku Edukasi (RAG)", value=True)
    ai_creativity = st.slider("Tingkat Kreativitas AI (Temperature):", 0.0, 1.0, 0.2, step=0.1)
    
    st.markdown("---")
    st.info("💡 **Tips Edukatif:** Gunakan temperature rendah (0.2) untuk analisis data yang presisi dan berbasis fakta.")

# ── 3. HALAMAN UTAMA (Main Workspace) ────────────────────────────────────────
st.title("🤖 RAGeni: AI Data Science Assistant")
st.caption("Aplikasi Edukatif Pendamping Pembelajaran Statistik & Machine Learning")

# Distribusi Layout Utama menggunakan Columns (Pembagian area Kerja)
col_data, col_chat = st.columns([1.1, 0.9])

# --- KOLOM KIRI: DATA EXPLORER & ANALYTICS ---
with col_data:
    st.header("📊 Data Explorer Workspace")
    
    if uploaded_file is not None:
        # Load data secara interaktif
        df = pd.read_csv(uploaded_file)
        st.success(f"Berhasil memuat dataset: `{uploaded_file.name}`")
        
        # Ringkasan KPI Data
        kpi1, kpi2, kpi3 = st.columns(3)
        kpi1.metric("Jumlah Baris Data", value=f"{df.shape[0]} baris")
        kpi2.metric("Jumlah Kolom / Fitur", value=f"{df.shape[1]} kolom")
        kpi3.metric("Kolom dengan Missing Value", value=f"{df.isnull().any().sum()} fitur")
        
        # Tabs untuk memisahkan view data agar rapi dan ringan
        tab_view, tab_stats, tab_chart = st.tabs(["📄 Preview Data", "🔢 Statistik Deskriptif", "📈 Generator Grafik"])
        
        with tab_view:
            st.write("Tabel Interaktif (10 Data Pertama):")
            st.dataframe(df.head(10), use_container_width=True)
            
        with tab_stats:
            st.write("Statistik Deskriptif Otomatis:")
            st.dataframe(df.describe(), use_container_width=True)
            
        with tab_chart:
            st.write("Visualisasi Cepat Dataset:")
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            if len(numeric_cols) >= 2:
                col_x = st.selectbox("Pilih Sumbu X:", numeric_cols, index=0)
                col_y = st.selectbox("Pilih Sumbu Y:", numeric_cols, index=min(1, len(numeric_cols)-1))
                
                chart_type = st.radio("Tipe Grafik:", ["Line Chart", "Bar Chart"], horizontal=True)
                if chart_type == "Line Chart":
                    st.line_chart(df[[col_x, col_y]].set_index(col_x))
                else:
                    st.bar_chart(df[[col_x, col_y]].set_index(col_x).head(30))
            else:
                st.warning("Dibutuhkan minimal 2 kolom numerik untuk membuat grafik.")
    else:
        # Kondisi Default saat data belum diupload
        st.info("Silakan unggah file CSV Anda di panel kiri untuk memulai analisis statistik otomatis.")
        
        # Tampilkan visualisasi dummy edukatif
        st.subheader("Tren Pembelajaran Data Science Mahasiswa")
        dummy_data = pd.DataFrame(
            {"Kapasitas RAG (Metrik A)": [10, 24, 45, 78], "Akurasi LLM (Metrik B)": [40, 55, 70, 95]},
            index=["Minggu 1", "Minggu 2", "Minggu 3", "Minggu 4"]
        )
        st.line_chart(dummy_data)

# --- KOLOM KANAN: AI ASSISTANT & CHATBOT AREA ---
with col_chat:
    st.header("💬 AI Assistant (RAG System)")
    st.write("Tanyakan hasil analisis data, interpretasi statistik, atau teori materi kuliah di bawah ini:")
    
    # Render chat history dari session state
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            
    # Input chat dari user
    if user_query := st.chat_input("Ketik pertanyaan Anda (misal: 'Jelaskan apa itu nilai p-value')"):
        # Tampilkan chat user ke UI
        with st.chat_message("user"):
            st.write(user_query)
        st.session_state.messages.append({"role": "user", "content": user_query})
        
        # Simulasi Pemrosesan RAG & Gemini API dengan progress effect yang smooth
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            with st.spinner("RAGeni sedang mencari referensi buku & menganalisis konteks..."):
                time.sleep(1.2) # Simulasi latensi RAG
                
                # Respon edukatif dummy terstruktur berdasarkan arah aplikasi RAGeni
                response = f"**[RAGeni Response Mode: RAG Teraktifkan]**\\n\\n" \
                           f"Pertanyaan Anda mengenai *'{user_query}'* telah dianalisis.\\n\\n" \
                           f"Berdasarkan dokumen referensi data science yang tersimpan di database lokal (ChromaDB), " \
                           f"berikut adalah penjelasan ringkasnya:\\n" \
                           f"1. **Definisi:** Konsep tersebut sangat krusial bagi mahasiswa/dosen dalam melakukan validasi eksperimen.\\n" \
                           f"2. **Implementasi Python:** Anda dapat mengeceknya langsung menggunakan library `scipy.stats` atau mengamati ringkasan tabel `df.describe()` di sebelah kiri.\\n\\n" \
                           f"*Catatan: Ini adalah simulasi UI Chatbot RAGeni yang siap dihubungkan ke modul `src/llm_chain.py` menggunakan API Gemini.*"
                
                message_placeholder.markdown(response)
                
        # Simpan respon asisten ke state
        st.session_state.messages.append({"role": "assistant", "content": response})

# ── 4. NOTIFIKASI & LOGGER SISTEM (FOOTER STATUS) ────────────────────────────
st.markdown("---")
st.subheader("🖥️ Status Sistem & Infrastruktur")
col_s1, col_s2, col_s3 = st.columns(3)
with col_s1:
    st.success("Koneksi Vector DB (ChromaDB): Terhubung (Local)")
with col_s2:
    st.success("Gemini API Status: Ready (Authenticated)")
with col_s3:
    st.info("Environment: Google Colab Runtime")
