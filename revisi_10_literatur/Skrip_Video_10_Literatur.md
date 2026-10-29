# Skrip video tugas Literature GAP Matrix sepuluh literatur

Nama Evaristo De Araujo. NIM P36.2026.00041. Durasi sekitar 8 sampai 10 menit.

## 1 Pembukaan dan konteks tugas
Tampilan: halaman judul PDF revisi.
Narasi: Selamat pagi atau selamat siang. Saya Evaristo De Araujo, NIM P36.2026.00041. Video ini menjelaskan Literature GAP Matrix sepuluh artikel dan pipeline RAG untuk proyek Fisheries Briefing Assistant Timor-Leste. Proyek ini membantu menyusun draf briefing perikanan pesisir dan perikanan skala kecil dari sumber yang dapat ditelusuri.

## 2 Hubungan dengan tugas sebelumnya
Tampilan: bagian konteks use case dan prompting pada PDF.
Narasi: Tugas pertama menetapkan masalah informasi yang tersebar dalam berbagai laporan. Pengguna utamanya adalah penyusun briefing bagi pimpinan. Atribut sumber mencakup lokasi, tanggal, tangkapan, upaya, spesies, dan pendapatan bila tersedia. Teknik zero-shot, few-shot, analisis bertahap yang dapat diperiksa, dan structured output menjadi dasar instruksi. Pada tugas ini, sumber eksternal dimasukkan melalui retrieval agar jawaban tidak hanya mengandalkan pengetahuan model.

## 3 Menjelaskan format contoh dosen
Tampilan: halaman matriks dan CSV revisi.
Narasi: Matriks mengikuti delapan kolom contoh, yaitu Paper, DOI, Problem, Metode, Dataset, Temuan, Keterbatasan, dan Future work. Dataset adalah data yang digunakan artikel yang ditelaah, bukan seluruh corpus tugas saya. Temuan adalah hasil artikel, bukan rencana kelompok. Keterbatasan dan future work dibedakan antara yang dinyatakan penulis dan usulan proyek.

## 4 Menjelaskan sepuluh referensi
Tampilan: daftar referensi lengkap pada PDF.
Narasi: Delapan artikel mendukung metode, evaluasi, atau penerapan RAG. Dua artikel memberi konteks perikanan Timor-Leste, yaitu PeskAAS dan co-management. Dua artikel tambahan dari versi lama membahas FLARE atau active retrieval dan praktik terbaik konfigurasi RAG. Artikel domain tidak saya sebut sebagai penerapan RAG. DOI dan URL dicantumkan agar sumber bisa diperiksa. DOI artikel RAG tahun 2020 mengarah ke versi arXiv, sedangkan tautan prosiding NeurIPS disediakan terpisah.

## 5 Menjelaskan pipeline
Tampilan: diagram alur dan notebook versi 3.
Narasi: Corpus prototipe adalah catatan literatur sekunder yang telah dikelompokkan menurut enam kolom isi. Retrieval BM25 memakai filter artikel dan kategori. Model Qwen2.5-3B-Instruct memilih ID bukti sesuai kategori dan membuat draf gap proyek. Kode merakit tabel dari catatan yang dipilih, memvalidasi format serta ID, lalu mengekspor CSV dan JSON. Karena bank bawaan hanya satu kandidat per kategori, demonstrasi ini belum menguji ranking pada kumpulan dokumen besar. Pengategorian bukti dilakukan secara editorial.

## 6 Menjalankan Google Colab
Tampilan dan tindakan: buka Pipeline_RAG_Fisheries_10_Literatur_v3.ipynb; pilih Runtime, Change runtime type, T4 GPU, lalu Run all.
Narasi: Model dijalankan pada komputer virtual Colab sehingga laptop tidak memerlukan Ollama. Notebook ini tidak memakai API key layanan model. Sel pertama memasang pustaka; sel berikutnya menyiapkan corpus dan kode; lalu model diunduh dan dimuat. Setelah itu sepuluh artikel diproses secara berurutan. Saya menunggu seluruh proses selesai.
Petunjuk: jeda menunggu boleh dipotong atau dipercepat dengan keterangan proses dipercepat. Jangan menggabungkan hasil eksekusi delapan artikel lama seolah-olah hasil sepuluh artikel baru.

## 7 Memeriksa hasil nyata
Tampilan: output run_manifest.json, errors.json, matrix.csv, dan gap_model.json dari eksekusi versi 3.
Narasi: Saya memeriksa rows_total, rows_schema_valid, dan rows_failed sesuai angka yang benar-benar tampil pada layar. Kelulusan teknis hanya berarti schema dan ID bukti valid. Itu bukan akurasi faktual seratus persen. Kesalahan tetap dicatat dalam errors.json tanpa mengganti hasil dengan matriks telaah secara diam-diam. Gap yang dihasilkan model disimpan terpisah dan masih perlu dinilai.
Petunjuk: bacakan angka aktual saja. Jika versi 3 belum dijalankan, nyatakan belum dijalankan dan jangan mengklaim 10 dari 10.

## 8 Menjelaskan analisis gap dan usulan paper
Tampilan: paragraf analisis pada PDF.
Narasi: Penggunaan RAG di perikanan sudah diteliti. Peluang proyek ini adalah pengujian briefing kebijakan dengan konteks Timor-Leste, metadata wilayah dan waktu, serta sitasi yang mendukung klaim. Artikel akuakultur dan multimodal tidak otomatis membuktikan sistem briefing efektif. Kami mengusulkan perbandingan model tanpa retrieval dengan RAG menggunakan penilaian fakta, sitasi, kesalahan angka atau periode, serta waktu penyusunan. Paragraf analisis laporan merupakan sintesis editorial berbantuan AI dan bukan generation model baru.

## 9 GitHub dan pengumpulan
Tampilan: https://github.com/Evaristo1976/Pipeline-RAG dan folder revisi_10_literatur setelah berhasil diunggah.
Narasi: Notebook, kode, corpus, referensi, dan hasil disimpan di GitHub agar dapat diperiksa. Versi lama dipertahankan sebagai riwayat. Laporan PDF memuat matriks sepuluh artikel, analisis, desain pipeline, batasan, dan URL repositori. PDF dikumpulkan melalui Kulino setelah review kelompok.

## 10 Penutup
Tampilan: halaman judul PDF.
Narasi: Tugas ini menghasilkan matriks sepuluh literatur sesuai format yang diminta dan prototipe pipeline yang dapat dijalankan ulang. Pengembangan berikutnya memerlukan teks lengkap, corpus yang lebih luas, serta evaluasi domain. Hasil model tetap perlu ditinjau manusia. Terima kasih.
