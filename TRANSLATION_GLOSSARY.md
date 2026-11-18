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

## Tambahan Rust Fundamentals — 2026-11-18

Istilah berikut tetap menggunakan bahasa Inggris dalam materi. Penjelasannya
merupakan bantuan penerjemah, terpisah dari teks penulis asli. Konteks sumber:
[pattern matching](src/pattern-matching.md),
[method dan trait](src/methods-and-traits.md), [generics](src/generics.md),
[closure](src/closures.md), [standard library](src/std-types.md),
[ownership](src/memory-management.md), [borrowing](src/borrowing.md),
[lifetime](src/lifetimes.md), [error handling](src/error-handling.md), dan
[Unsafe Rust](src/unsafe-rust.md).

| Istilah / konteks               | Makna kontekstual                                                                                  | Contoh penggunaan                                       | Hindari menyamakan dengan                                          |
| ------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------ |
| pattern / pencocokan            | Bentuk yang dicocokkan dengan struktur atau nilai data                                             | pattern pada match arm                                  | pencarian teks saja                                                |
| destructuring / data            | Menguraikan nilai menjadi bagian penyusunnya                                                       | destructuring tuple                                     | merusak atau menghapus nilai                                       |
| irrefutable / pattern           | Pattern yang selalu cocok dengan nilai bertipe sesuai                                              | irrefutable pattern pada let                            | pattern yang cocok dengan semua tipe                               |
| match guard / pattern           | Kondisi tambahan untuk memilih arm yang pattern-nya cocok                                          | match guard yang memeriksa suatu kondisi                | if yang baru dijalankan dalam arm terpilih                         |
| shadowing / variabel            | Binding baru memakai nama yang sudah digunakan                                                     | pattern membuat variabel baru melalui shadowing         | perubahan nilai pada binding lama                                  |
| receiver / method               | Objek yang menjadi sasaran pemanggilan method                                                      | receiver berupa `&self`                                 | semua argumen method                                               |
| trait bound / generics          | Persyaratan trait yang harus dipenuhi tipe                                                         | `T: Clone` sebagai trait bound                          | konversi otomatis ke tipe lain                                     |
| associated type / trait         | Tipe yang ditentukan implementasi trait                                                            | associated type `Output`                                | parameter tipe yang dipilih caller saat memanggil fungsi           |
| monomorphization / generics     | Pembuatan implementasi khusus untuk tipe konkret yang digunakan                                    | monomorphization fungsi generic                         | pencarian method melalui vtable saat runtime                       |
| static dispatch / trait         | Penentuan implementasi panggilan berdasarkan informasi tipe saat kompilasi                         | static dispatch pada fungsi generic                     | dynamic dispatch                                                   |
| dynamic dispatch / trait object | Pemilihan implementasi saat runtime melalui informasi objek                                        | dynamic dispatch melalui vtable                         | kompilasi ulang fungsi saat runtime                                |
| type erasure / trait object     | Tipe konkret disembunyikan di balik antarmuka trait object                                         | type-erased `dyn Trait`                                 | hilangnya pemeriksaan tipe                                         |
| closure / fungsi                | Fungsi anonim yang dapat menangkap variabel dari environment-nya                                   | closure sebagai predicate filter                        | fungsi yang selalu menangkap variabel                              |
| capture / closure               | Cara closure memperoleh akses ke variabel dari scope luar                                          | capture by reference atau by value                      | selalu melakukan clone                                             |
| coercion / tipe                 | Penyesuaian tipe otomatis pada konteks yang diizinkan Rust                                         | closure tanpa capture menjadi function pointer          | cast bebas antarsemua tipe                                         |
| predicate / filter              | Fungsi atau closure yang menghasilkan keputusan benar/salah                                        | predicate menentukan pesan yang lolos filter            | nilai log yang sedang disaring                                     |
| lossless / konversi             | Konversi yang mempertahankan informasi nilai                                                       | konversi lossless melalui `From`                        | sekadar konversi yang bisa dikompilasi                             |
| infallible / konversi           | Konversi yang tidak memiliki kasus kegagalan dalam kontraknya                                      | infallible conversion                                   | konversi yang pasti tidak kehilangan data tanpa melihat kontraknya |
| fallible / konversi             | Konversi yang dapat gagal untuk input tertentu                                                     | fallible conversion melalui `TryFrom`                   | fungsi yang pasti gagal                                            |
| truncation / integer            | Pemotongan bagian representasi nilai                                                               | truncation menjadi tipe integer lebih kecil             | pembulatan numerik biasa                                           |
| allocator / memori              | Mekanisme penyedia dan pengelola alokasi memori                                                    | heap allocator                                          | garbage collector                                                  |
| memory locality / memori        | Kedekatan lokasi memori data yang diakses                                                          | memory locality pada stack                              | jaminan semua akses selalu cepat                                   |
| interior mutability / borrowing | Pola yang memungkinkan perubahan data melalui shared reference dengan aturan keamanan yang sesuai  | `Cell` dan `RefCell`                                    | mengabaikan seluruh aturan borrowing                               |
| lifetime elision / signature    | Aturan sintaks untuk melengkapi lifetime yang tidak ditulis                                        | lifetime elision pada argumen dan nilai kembalian       | analisis isi fungsi untuk menebak lifetime                         |
| prelude / scope                 | Sekumpulan item yang tersedia tanpa import eksplisit                                               | `HashMap` tidak termasuk prelude                        | seluruh standard library                                           |
| grapheme cluster / string       | Kelompok karakter Unicode yang dapat dipandang sebagai satu karakter oleh pembaca                  | satu grapheme cluster dapat memuat beberapa `char`      | selalu satu byte atau satu `char`                                  |
| sound / abstraksi Rust          | Memenuhi persyaratan keamanan yang diperlukan agar penggunaan safe tidak memicu undefined behavior | safe wrapper yang sound                                 | bebas dari semua jenis bug                                         |
| unsound / abstraksi Rust        | Dapat melanggar jaminan keamanan melalui penggunaan yang seharusnya safe                           | safe function yang dapat menyebabkan undefined behavior | sekadar adanya block unsafe                                        |
| NUL-terminated / FFI            | Representasi string C dengan byte nol sebagai penanda akhir                                        | string yang dibuat dengan `CString`                     | pointer null                                                       |
| inaccessible / diagram move     | Nilai tidak dapat diakses melalui binding yang ownership-nya telah dipindahkan                     | label s1 setelah move pada diagram                      | heap selalu langsung dibebaskan setelah move                       |

Pada pembahasan perbandingan, **reflexive** berarti suatu nilai setara dengan
dirinya sendiri; **symmetric** berarti arah perbandingan tidak mengubah
kesetaraan; **transitive** berarti kesetaraan berantai tetap berlaku. Istilah
tersebut tetap dipertahankan agar pembaca dapat mencocokkannya dengan
dokumentasi trait.
