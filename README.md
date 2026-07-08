# RAGeni
Asisten Pintar Interaktif untuk memahami berbasis web yang dirancang khusus untuk lingkungan akademis (siswa, mahasiswa, dan dosen).

---

## 🚀 Fitur Utama

* **Dual-Workspace Layout:** Antarmuka multitasking horizontal yang memisahkan area eksplorasi data (kiri) dengan asisten AI chatbot (kanan).
* **Interactive Data Explorer:** Unggah dataset berformat CSV untuk mendapatkan ringkasan KPI data, visualisasi grafik otomatis (Line & Bar Chart), serta statistik deskriptif tanpa menulis kode.
* **Context-Aware AI Chatbot:** Chatbot pintar yang tidak hanya menjawab pertanyaan umum, tetapi juga dibekali memori percakapan (`st.session_state`) dan basis dokumen edukasi lokal via RAG.
* **Parameter AI Fleksibel:** Pengaturan tingkat kreativitas model (Temperature) langsung dari sidebar demi hasil analisis yang presisi.
* **Ultra-Lightweight & Cloud Ready:** Dibangun dengan Python dan Streamlit, memastikan performa aplikasi tetap cepat dan responsif saat di-deploy ke cloud.

---

## 🏗️ Arsitektur Teknis

Aplikasi ini menggunakan arsitektur modular tiga lapis (Three-Tier):
1. **Frontend / Presentation:** Streamlit UI Components (Reaktif & Ringan).
2. **Logic & AI Orchestrator:** Python, Google GenAI SDK (Gemini 2.5 Flash API), dan Pandas/NumPy untuk pemrosesan data lokal.
3. **Storage & Vector Space:** ChromaDB (Lokal/In-Memory) untuk menyimpan embedding dokumen panduan materi data science (Sistem RAG).

---

## 📂 Struktur Proyek

```text
materi-rag-app/
├── .streamlit/
│   └── config.toml          # Konfigurasi tema & server Streamlit
├── data/
│   └── vector_db/           # Direktori penyimpanan lokal ChromaDB
├── documents/
│   └── edukasi/             # File PDF/MD panduan dasar data science
├── src/
│   ├── database.py          # Modul inisialisasi & query ChromaDB
│   ├── llm_chain.py         # Konfigurasi integrasi Gemini API
│   └── processor.py         # Logika pengolahan CSV & statistik
├── app.py                   # File utama entry-point aplikasi Streamlit
├── requirements.txt         # Daftar dependency package
└── README.md                # Dokumentasi proyek
