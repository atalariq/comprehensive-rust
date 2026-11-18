# Glosarium awal

Versi 1.0 · istilah Inggris dipertahankan; kolom makna adalah bantuan pemahaman,
bukan pengganti wajib dalam kalimat. Penjelasan tambahan di halaman diberi label
catatan penerjemah. Bentuk yang dihindari berikut merujuk konteks ini, bukan
larangan bahasa universal.

| Istilah / konteks                  | Makna kontekstual                                               | Bentuk yang dipakai / contoh                                                | Bentuk yang dihindari                                           |
| ---------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------- |
| ownership / Rust                   | Aturan kepemilikan nilai                                        | caller tetap memiliki ownership atas input                                  | ownership = hak akses                                           |
| borrow, borrowing / Rust           | Akses ke nilai melalui reference tanpa memindahkan ownership    | Fungsi meminjam nilai; istilah borrowing tetap pada judul/penjelasan konsep | mengambil alih nilai                                            |
| caller / pemanggilan fungsi        | Kode yang memanggil fungsi                                      | caller tetap memiliki ownership                                             | pengguna akhir                                                  |
| input / fungsi                     | Nilai masukan                                                   | ownership atas input                                                        | selalu diterjemahkan sebagai ketikan pengguna                   |
| Safe Rust / Rust                   | Bagian Rust dengan jaminan keamanan sumber                      | Safe Rust                                                                   | Rust aman berarti seluruh aplikasi bebas bug                    |
| Unsafe Rust / Rust                 | Bagian Rust yang memungkinkan operasi tambahan dengan prasyarat | Unsafe Rust                                                                 | kode yang pasti salah                                           |
| undefined behavior / Rust          | Perilaku yang tidak ditentukan menurut aturan bahasa            | dapat memicu undefined behavior                                             | hasil acak (terlalu sempit)                                     |
| safe abstraction / Rust            | Abstraksi dengan antarmuka aman yang membungkus detail unsafe   | lapisan safe abstraction                                                    | sekadar menyembunyikan kode                                     |
| CL / Google review                 | Changelist: satu unit perubahan untuk review                    | ukuran CL                                                                   | selalu disamakan dengan satu commit                             |
| self-contained / CL                | Perubahan yang utuh dan dapat dipahami dalam cakupannya         | satu perubahan yang utuh dan mandiri                                        | tidak boleh bergantung pada sistem lain                         |
| reviewer / review                  | Orang yang meninjau perubahan                                   | diskusikan dengan reviewer                                                  | selalu auditor                                                  |
| code health / review               | Kualitas menyeluruh kode yang dibahas sumber                    | code health sistem                                                          | hanya kecepatan eksekusi                                        |
| shell / kursus                     | Program untuk menjalankan perintah dan mengolah input/output    | pilih shell                                                                 | terminal                                                        |
| terminal / kursus                  | Antarmuka untuk berinteraksi dengan shell                       | buka terminal                                                               | shell                                                           |
| prompt / shell                     | Tempat/penanda kesiapan shell menerima perintah                 | prompt shell                                                                | prompt AI dalam konteks ini                                     |
| latency / desain sistem            | Waktu untuk melakukan tindakan atau menghasilkan hasil          | latency yang dapat diterima                                                 | jumlah operasi per detik                                        |
| throughput / desain sistem         | Jumlah tindakan atau hasil per satuan waktu                     | throughput maksimal                                                         | waktu satu operasi                                              |
| bottleneck / desain sistem         | Bagian yang membatasi kinerja sistem                            | identifikasi bottleneck                                                     | selalu database                                                 |
| scalability / desain sistem        | Kemampuan sistem menangani perubahan skala beban                | masalah scalability                                                         | sekadar performa satu mesin                                     |
| trade-off / desain sistem          | Konsekuensi pilihan yang menukar keuntungan dan keterbatasan    | bahas trade-off                                                             | kompromi yang pasti buruk                                       |
| load balancer / desain sistem      | Komponen pembagi beban                                          | Load balancer                                                               | penerjemahan nama komponen yang menghilangkan istilah pencarian |
| horizontal scaling / desain sistem | Menambah jumlah instance/node                                   | Horizontal scaling                                                          | menambah kapasitas satu mesin                                   |
| caching / desain sistem            | Pemanfaatan cache                                               | Caching                                                                     | penyimpanan permanen                                            |
| database sharding / desain sistem  | Pembagian data ke beberapa shard                                | Database sharding                                                           | sekadar membuat replika                                         |

Literal contoh yang dilindungi: `Nit:` (termasuk spasi setelah titik dua),
`echo $SHELL`, `/bin/bash`, `/usr/bin/zsh`, `cmd.exe`, `add`. Nama Bash, ZSH,
PowerShell, Windows Subsystem for Linux, dan Rust mengikuti bentuk sumber pada
cuplikan.

Penambahan istilah: sertakan proyek dan bagian sumber, makna yang dimaksud,
contoh kalimat, serta alasan jika berbeda dari entri yang sudah ada. Jangan
mengubah semua proyek hanya demi menyeragamkan dua makna yang berbeda.
