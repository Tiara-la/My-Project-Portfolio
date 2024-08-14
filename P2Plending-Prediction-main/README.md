# Sistem-P2P-Lending-Pred

Implementasi sistem pada penelitian ini menggunakan framework Streamlit dan environment pada python.  
 
 ![img](Icon/image_2023-09-22_15-26-33.png) <br>
 ![image_2023-09-22_15-26-42](https://github.com/Tiara-la/P2PlendingPred.github.io/assets/57089512/e675152d-b63b-46e1-b849-3fd113cdbb6d) <br>
Gambar 4.19. Tampilan Halaman Home <br> <br>

Gambar 4.19 merupakan halaman Home dari web prediksi risiko gagal bayar pinjaman dimana pengguna dapat melihat informasi tentang web ini. Selain menu Home, pada bagian samping terdapat menu sidebar yang berisi menu Manual Input dan CSV Input. Tampilan menu Manual Input dapat dilihat pada Gambar 4.20.

![image_2023-09-22_15-26-51](https://github.com/Tiara-la/P2PlendingPred.github.io/assets/57089512/b3b64011-c4d7-44fd-b37d-90c3710f3eb4) <br>
Gambar 4.20. Tampilan Menu Manual Input <br> <br>

Pada menu Manual Input pengguna dapat melakukan prediksi dengan meng-input data secara manual satu persatu. Ada 3 data yang harus dimasukan sesuai dengan hasil seleksi fitur yang telah dilakukan sebelumnya. Data-data yang perlu pengguna input-kan adalah day past due, principal balance dan principal paid.
Setelah data dimasukan satu persatu, selanjutnya pengguna bisa menekan button “Predict” untuk mendapat hasil prediksi. Ketika pinjaman masuk kategori default maka akan muncul hasil berupa tulisan “Prediksi pinjaman ini adalah Default”. Namun jika pinjaman masuk kategori non-default makan akan muncul hasil berupa tulisan “Prediksi pinjaman ini adalah Non-Default”. Tampilan hasil prediksi dapat dilihat pada Gambar 4.21.
 
 
 ![image_2023-09-22_15-26-51](https://github.com/Tiara-la/P2PlendingPred.github.io/assets/57089512/b3b64011-c4d7-44fd-b37d-90c3710f3eb4) <br>
Gambar 4.21. Tampilan Hasil Prediksi pada Menu Manual Input <br> <br>

Kemudian pada bagian menu CSV Input pengguna dapat melakukan prediksi dengan banyak data sekaligus. Data yang dapat di-input-kan berformat csv. Caranya yaitu dengan meng-upload data yang berformat csv pada bagian Drag and drop file. Tampilan dari menu CSV Input dapat dilihat pada Gambar 4.22.

![image_2023-09-22_15-29-54](https://github.com/Tiara-la/P2PlendingPred.github.io/assets/57089512/af8b7808-b008-4859-9cb7-221768bf72e1) <br>
Gambar 4.22. Tampilan Menu CSV Input <br> <br>

Setelah data ter-upload, sistem akan otomatis mambaca file dan akan menampilkan tampilan file yang telah di-upload dan pengguna dapat langsung melakukan prediksi dengan menekan button “Predict”. Tampilan ketika data telah terbaca oleh sistem dapat dilihat pada Gambar 4.23.

![image_2023-09-22_15-30-01](https://github.com/Tiara-la/P2PlendingPred.github.io/assets/57089512/7e5cb8c5-0d21-46c4-ac9f-67a7abc18f48)
<br>
Gambar 4.23. Tampilan Ketika Data Telah Terbaca Sistem <br> <br>
Proses prediksi akan berlangsung beberapa saat, hingga muncul tampilan data dengan kolom baru yaitu y_pred yang merupakan hasil prediksi dari data yang berisi kelas 0 dan 1. Tampilan dari hasil prediksi pada menu CSV Input dapat dilihat pada Gambar 4.24.

![image_2023-09-22_15-30-07](https://github.com/Tiara-la/P2PlendingPred.github.io/assets/57089512/e8cf6655-652d-4759-9401-01fba59313f9) <br>
Gambar 4.24. Tampilan Hasil Prediksi pada Menu CSV Input <br> <br>

Setelah hasil prediksi keluar, pengguna juga dapat melihat visualisasi jumlah dan perbandingan dari jumlah kelas prediksi untuk memudahkan pengguna dalam melihat perbandingan jumlah data default dengan non-default. Tampilan dari hasil visualisasi hasil prediksi dapat dilihat pada Gambar 4.25. 

![image_2023-09-22_15-30-14](https://github.com/Tiara-la/P2PlendingPred.github.io/assets/57089512/a38949cc-38f5-4584-9b39-b117385b86cb) <br>
Gambar 4.25. Visualisasi Hasil Prediksi <br> <br>
