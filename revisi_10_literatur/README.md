# Revisi tugas sepuluh literatur versi 3

Nama: Evaristo De Araujo. NIM: P36.2026.00041.

Matriks mengikuti contoh dosen dengan delapan kolom persis:
Paper | DOI | Problem | Metode | Dataset | Temuan | Keterbatasan | Future work.

Terdapat 10 artikel: R1-R8 mengenai metode/evaluasi/penerapan RAG dan D1-D2 tentang konteks perikanan Timor-Leste. ID lama dipertahankan untuk audit; nomor baris bukan ID baru. Dua tambahan adalah FLARE dan Searching for Best Practices in RAG. Semua memiliki DOI, dengan R1 memakai DOI versi arXiv.

## Cara menjalankan di Colab
Unggah Pipeline_RAG_Fisheries_10_Literatur_v3.ipynb melalui File > Upload notebook. Pilih Runtime > Change runtime type > T4 GPU, lalu Run all. Tidak memerlukan Ollama atau API key. Model Qwen2.5-3B-Instruct diunduh pada server Colab. Sumber dan kode tertanam di notebook sehingga tidak perlu mengubah path atau mengunggah ZIP lain. Ketersediaan GPU mengikuti layanan Colab.

## Demo lokal tanpa model
Jalankan python pipeline.py dari folder ini. Hasil results/demo_10 berstatus editorial_demo_no_model. Demo tidak membuktikan model generatif telah dijalankan. Gunakan notebook untuk menjalankan model dan menyimpan manifest baru.

## Cakupan implementasi
Corpus berisi 60 catatan sekunder terkurasi, enam kategori per artikel. Catatan bukan kutipan asli full text. Retriever BM25 memakai filter artikel dan kategori; bank bawaan hanya satu kandidat per kategori, sehingga pemilihan bukti sangat terbatas dan belum menguji kemampuan ranking kompetitif. Pengategorian corpus dilakukan secara editorial. Model memilih evidence_id sesuai kategori dan menghasilkan gap_proyek yang disimpan terpisah. Teks tabel dirakit dari catatan terpilih untuk menghindari terjemahan kutipan dan perpindahan kategori.

Validasi mencakup schema, ID artikel, ID bukti, dan kategori field. Ini tidak membuktikan kebenaran semantik atau kecukupan penelusuran literatur. Future work berlabel Penulis jika berasal dari arah penelitian artikel dan Usulan proyek jika merupakan interpretasi proyek. Keterbatasan berlabel Batas transfer (analisis) tidak dinyatakan sebagai limitation dari penulis.

## Status dan integritas hasil
Matriks pada hasil_telaah dan laporan PDF adalah telaah editorial berbantuan AI. Paragraf analisis disertakan sebagai sintesis editorial, bukan keluaran baru model. Versi 2 sudah dijalankan pengguna untuk 8 artikel dan lolos validasi teknis 8/8, tetapi masih memiliki kesalahan isi. Hasil tersebut tidak boleh disebut hasil versi 3 atau 10/10. Notebook versi 3 belum dijalankan pada GPU saat paket disiapkan; uji lokal hanya menguji retrieval, ekspor, validator, dan sintaks notebook. Review kelompok terhadap sumber asli tetap diperlukan.

## Berkas penting
- data/literature_10.json: corpus dan evidence_id berkategori.
- pipeline.py: implementasi retrieval, pemanggilan callback model, validasi, dan ekspor.
- hasil_telaah: matriks serta analisis editorial dengan status.
- results/demo_10: hasil demo tanpa model (jika disertakan).
- REFERENSI.md: DOI, URL dan penunjuk sumber.
- Skrip_Video_10_Literatur.md: panduan rekaman versi sepuluh artikel.

## Memperbarui GitHub dan Kulino
Repositori tujuan: https://github.com/Evaristo1976/Pipeline-RAG
Unggah folder revisi_10_literatur melalui Add file > Upload files. Pertahankan folder dan hasil lama sebagai riwayat. Setelah Colab versi 3 benar-benar dijalankan, ekstrak ZIP hasil dan unggah pada folder hasil_model_v3 yang berbeda. Periksa manifest, errors.json, dan isi tabel. PDF revisi digunakan untuk Kulino setelah kelompok meninjau identitas dan isinya. Tidak ada klaim bahwa versi baru telah terunggah otomatis ke GitHub.


## Pembaruan setelah eksekusi pengguna
Pada 29 Oktober 2026, hasil Colab versi 3 telah diperiksa: model Qwen2.5-3B-Instruct dipanggil 10 kali pada Tesla T4, 10 baris lolos schema serta ID kategori, dan 0 gagal. CSV dan JSON sesuai; semua pilihan pada raw output cocok dengan matriks dan hash corpus sesuai manifest. Ini bukan akurasi faktual 100 persen atau benchmark ranking. Hasil asli ada pada hasil_model_v3 dan pemeriksaan terpisah pada audit_v3. Gap model R4 dan R5 masih memerlukan koreksi fokus; lihat telaah_gap_model.csv. Kalimat status belum dieksekusi di atas merujuk waktu awal penyiapan paket, bukan status setelah pembaruan ini. Unggahan versi 3 ke GitHub belum diverifikasi.
