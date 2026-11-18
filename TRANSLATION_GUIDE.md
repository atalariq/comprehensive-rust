# Pedoman editorial

Versi 1.0 · 2026-11-17

## Pembaca dan kesetiaan terhadap sumber

Pembaca sasaran belum lancar berbahasa Inggris; pengalaman teknis mereka
beragam. Terjemahan mengurangi hambatan bahasa tanpa menjanjikan hilangnya
prasyarat. Comprehensive Rust, misalnya, merupakan kursus dengan pengajar bagi
programmer berpengalaman yang baru mengenal Rust (lihat [STYLE.md](STYLE.md)).
Prasyarat, edisi, kebutuhan perangkat, dan tujuan sumber harus tetap terlihat.

Terjemahkan seluruh penjelasan, bukan intisarinya. Pertahankan alur argumen,
perbandingan, daftar, batasan, pengecualian, humor, dan sudut pandang penulis.
Jangan menghapus pengulangan yang sengaja menekankan suatu gagasan. Kalimat
panjang boleh dipecah jika hubungan logikanya tetap utuh.

## Gaya bahasa

Gunakan bahasa Indonesia semi-formal, ejaan baku, kalimat aktif yang alami, dan
sapaan Anda bila perlu. Pertahankan “kami” jika sumber merujuk penulis/pengajar;
jangan otomatis menggantinya menjadi “kita”. Hindari slang, basa-basi, kalimat
promosi, dan tambahan seperti “tentunya” atau “sangat penting” jika tidak ada di
sumber. Judul memakai kapitalisasi Indonesia sambil mempertahankan nama produk
dan istilah baku.

Contoh pola: “Anda dapat menjalankan perintah ini” lebih langsung daripada “Anda
dapat melakukan pelaksanaan perintah ini”. Ringkas berarti membuang kerumitan
kalimat, bukan informasi.

## Istilah dan literal

Pertahankan istilah teknis Inggris. Kata umum seperti membaca, menjalankan, atau
hasil tetap diterjemahkan; jangan mencampurkan bahasa tanpa tujuan. Pada
kemunculan pertama per halaman, beri penjelasan singkat bila istilah diperlukan
untuk memahami materi. Penjelasan tambahan yang melampaui sumber diberi label
catatan penerjemah.

Gunakan [glosarium](TRANSLATION_GLOSSARY.md); catat istilah baru sebelum
menerapkannya ke banyak halaman. Makna kontekstual mengungguli pencocokan kata.
Jangan menyamakan shell dengan terminal, latency dengan throughput, atau
ownership dengan hak akses. Kapitalisasi mengikuti istilah sumber. Istilah
Inggris tidak otomatis dimiringkan atau diberi backtick. Pertahankan penekanan
sumber yang memang bermakna.

Backtick menandai literal: `echo $SHELL`, `/bin/bash`, identifier, atau nama
berkas yang sedang dirujuk. Pertahankan blok kode, komentar di dalam kode,
perintah, output, identifier, escape, placeholder, dan directive persis. Jangan
memperbaiki atau menerjemahkan kode sebagai bagian pekerjaan ini.

## Kekuatan pernyataan

| Bentuk sumber               | Arah terjemahan                     | Yang harus diperiksa                                |
| --------------------------- | ----------------------------------- | --------------------------------------------------- |
| must / need to              | harus / perlu, sesuai konteks       | Apakah benar syarat atau sekadar kebutuhan praktis? |
| should                      | sebaiknya / disarankan              | Jangan otomatis menjadi “harus”.                    |
| may / can                   | boleh / mungkin / dapat             | Bedakan izin, kemungkinan, dan kemampuan.           |
| generally / usually         | umumnya / biasanya                  | Jangan hilangkan batas generalisasi.                |
| nearly / roughly / probably | hampir / kurang lebih / kemungkinan | Jangan ubah perkiraan menjadi kepastian.            |
| only / unless / if / not    | hanya / kecuali jika / jika / tidak | Pastikan cakupan dan kondisi negasi tetap sama.     |

Tabel ini panduan penalaran, bukan kamus substitusi otomatis. Angka, satuan,
nama produk, analogi budaya, dan contoh tetap mengikuti sumber. Jangan
mengonversi satuan atau mengganti analogi secara diam-diam.

## Catatan penerjemah dan cacat sumber

Gunakan bentuk berikut di luar alur teks penulis:

> **Catatan penerjemah — YYYY-MM-DD:** penjelasan tambahan, alasan
> penambahannya, dan rujukan jika memuat klaim yang perlu dibuktikan.

Catatan harus singkat dan diperlukan untuk memahami materi. Jangan menyisipkan
kurikulum baru, solusi tambahan, atau opini pribadi. Gunakan catatan untuk
menjelaskan istilah sulit atau masalah sumber yang sudah diverifikasi. Jangan
menyatakan sumber salah hanya karena terjemahannya terasa janggal.

Untuk sumber keliru/kedaluwarsa: catat kutipan, commit, bukti, dampak, dan
penanganan; pertahankan pembedaan tulisan penulis dan koreksi. Perubahan kode
atau substansi ditangani terpisah. Jika masalah dapat menyesatkan secara serius
atau menghalangi latihan, jangan beri status siap belajar sampai penanganannya
jelas. Jangan menunggu jadwal kuartalan untuk koreksi serius.

## Struktur, tautan, dan media

Terjemahkan judul, navigasi, caption, alt text, uraian latihan, dan penjelasan
di luar kode. Pertahankan urutan serta hierarki heading. Sumber Inggris tetap
utuh. Gunakan namespace/nama berkas terjemahan native, bukan mengganti sumber.

Bedakan URL referensi yang dilindungi dari tautan navigasi: URL eksternal sumber
tidak diubah; tautan internal boleh dipetakan ke padanan Indonesia yang siap.
Pertahankan anchor eksplisit dan kestabilan URL sejauh mekanisme proyek
memungkinkan. Heading terjemahan memerlukan pemeriksaan anchor hasil render,
karena slug dapat berubah. Jangan mengandalkan pemeriksaan Markdown saja.

Teks diagram buatan proyek juga diterjemahkan. Jika gambar tidak bisa diedit
dengan baik, sediakan keterangan Indonesia yang memetakan seluruh label
bermakna, bukan hanya ringkasan. Pertahankan gambar sumber dan atribusinya.
Materi unduhan termasuk cakupan; format yang belum dapat diperiksa menjadi
blocker tercatat, bukan diam-diam dikecualikan. Video/audio dan sumber eksternal
diberi keterangan bahwa bahasa aslinya tetap digunakan.

## Alur kerja dan status

1. Verifikasi upstream resmi, periksa build dasar, lalu catat commit acuan fase
   produksi. Contoh editorial paket ini sengaja memakai snapshot lokal
   teridentifikasi.
2. Inventarisasi unit sumber dan padanannya, termasuk catatan pengajar, aset,
   latihan, solusi tersedia, dan WIP. WIP sumber berbeda dari terjemahan belum
   selesai.
3. Audit karya Indonesia terdahulu sebelum reuse: makna, versi sumber, lisensi,
   kredit, dan kesesuaian gaya. Jangan mengklaim karya terdahulu sebagai hasil
   baru.
4. Susun draf berbantuan AI dan bandingkan setiap unit dengan sumber. Catat
   siapa/apa yang memeriksa dan bukti pemeriksaannya.
5. Jalankan pemeriksaan yang relevan serta checklist; revisi temuan sebelum
   rilis unit.

Status minimum: belum tersedia, draf AI, diperiksa AI, ditinjau penerjemah
manusia, siap belajar, perlu pembaruan. Review AI tidak mengisi kolom reviewer
manusia. Sesuai keputusan awal, review manusia mandiri cukup; reviewer
independen tidak wajib. Penyerahan pekerjaan kepada AI tidak otomatis
membuktikan gerbang review manusia telah terpenuhi. Selama belum ada penilaian
manusia, paket ini berstatus diperiksa AI dan menunggu penilaian pengguna.

## Ketentuan produksi yang telah disepakati

Ikuti Gettext Rust dan mekanisme native repo lain. Rust memakai `po/id.po`;
jangan mengedit `msgid`. Pisahkan refresh katalog dari perubahan terjemahan;
entri fuzzy belum dianggap selesai. Jangan menggandakan Markdown sumber untuk
mengganti alur PO.

Rilis bertahap per unit utuh. Kelengkapan, konsistensi istilah, keutuhan kode,
tautan/anchor, build, dan review sumber wajib diperiksa. Tautan eksternal mati
dicatat dan ditangani berdasarkan dampak belajar. Navigasi memuat seluruh
cakupan dengan status; yang belum siap mengarah ke sumber Inggris berlabel,
bukan draf AI tanpa penanda.

Publikasi melalui fork mandiri. Gunakan GitHub Pages untuk situs yang sesuai dan
Markdown GitHub untuk System Design Primer. Akses terbuka tanpa login, paywall,
iklan, atau analytics tambahan. Periksa ponsel, navigasi keyboard, heading, dan
keterbacaan kode. Integrasi serta deployment belum dilakukan pada tahap
editorial.

Periksa perubahan upstream per kuartal; tandai unit terdampak sampai selesai
ditinjau. Sediakan GitHub Issues, tautan sumber, commit, dan status review.
Koreksi serius ditangani segera menurut dampaknya tanpa menjanjikan SLA tetap.
Jangan mengklaim terjemahan selalu mutakhir.
