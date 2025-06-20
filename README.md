# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
Tingginya tingkat siswa yang dropout menyebabkan kekhawatiran terhadap citra institusi dan efektivitas sistem akademik. Institusi ingin mengetahui sejak dini siswa yang berisiko tinggi untuk dropout agar dapat diberikan intervensi lebih awal.

### Cakupan Proyek
- Menyiapkan dataset.
- Exploratory Data Analysis (EDA).
- Pemodelan machine learning menggunakan Random Forest dan XGBoost.
- Pembuatan business dashboard menggunakan Metabase.
- Pembuatan prototipe aplikasi machine learning dengan Streamlit.

## Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance

Setup environment:
- Anaconda
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

- Shell/Terminal
```bash
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```
- Note:
Turunkan versi python (ke versi 3.9) dan scikit learn jika bermasalah dengan dependensi imbalanced_learn

## Business Dashboard
Business dashboard dibuat menggunakan Metabase dan berisi visualisasi untuk memantau status siswa dan faktor-faktor yang memperngaruhinya. Dashboard ini membantu institusi mengambil keputusan berbasis data.

- **URL:** http://localhost:3000/
- **Email:** `root@mail.com`
- **Password:** `root123`

**Dashboard mencakup:**
- Feature diambil berdasarkan feature importances dari model Random Forest (best_rf.feature_importances_)
- Distribusi status siswa
- Demografi dan background akademik
- Rata-rata nilai masuk dan performa per semester
- Pengaruh faktor sosial-ekonomi seperti beasiswa, hutang, dan biaya kuliah
- Pengaruh faktor makroekonomi seperti inflasi, dan GDP

## Menjalankan Sistem Machine Learning
Prototipe sistem Machine Learning ini dikembangkan menggunakan Streamlit. Aplikasi ini dirancang untuk memprediksi status siswa berdasarkan data dimasukkan. Untuk menjaga fokus dan efisiensi, hanya fitur-fitur utama yang paling berpengaruh pada model (berdasarkan feature importances dari model Random Forest best_rf.feature_importances_) yang ditampilkan dalam form.

**Cara Menggunakan Aplikasi:**
1. Akses Aplikasi: https://studentperformance-adi.streamlit.app/
2. Isi Data Siswa: terdapat tiga jenis kontrol:
    - Radio Button: Untuk memilih salah satu dari beberapa opsi.
    - Drop-down: Untuk memilih satu opsi dari daftar.
    - Slider: Untuk memilih nilai dalam rentang tertentu.
    Setiap fitur input dilengkapi dengan tooltip (deskripsi singkat yang muncul saat kursor diarahkan ke elemen tanda tanya "?") untuk membantu memahami data yang diperlukan.
3. Dapatkan Prediksi: Setelah semua data siswa terisi lengkap, klik tombol "Predict". Aplikasi akan menampilkan hasil prediksi status siswa.

## Conclusion
Model Machine Learning Random Forest yang telah disesuaikan (Tuned) menunjukkan kemampuan yang cukup baik dalam memprediksi status siswa, dengan tingkat akurasi sekitar 75%. Faktor-faktor paling berpengaruh terhadap status siswa adalah performa akademik di semester pertama dan kedua. Selain itu, nilai saat pendaftaran dan status sosial ekonomi siswa juga memiliki dampak signifikan.

Dashboard analitik dan prototipe aplikasi Machine Learning dirancang untuk membantu Jaya Jaya Institut dalam mengidentifikasi siswa-siswa yang berisiko tinggi mengalami dropout. Dengan demikian, institusi dapat mengambil tindakan pencegahan yang lebih cepat dan terarah untuk mendukung keberhasilan siswa.

### Rekomendasi Action Items
- Lakukan pemantauan berkala terhadap siswa dengan performa rendah dan biaya kuliah tertunggak.
- Sediakan bimbingan tambahan untuk siswa dengan nilai akademik semester awal yang rendah.
- Gunakan model prediktif sebagai sistem peringatan dini untuk memberikan intervensi tepat waktu.
- Lakukan evaluasi kebijakan penerimaan agar mempertimbangkan profil risiko siswa sejak awal.
