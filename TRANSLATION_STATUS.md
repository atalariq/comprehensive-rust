# Status terjemahan Indonesia

Diperbarui: 2026-11-18 · kebijakan editorial 1.0.

## Progres aktual

**Seluruh Rust Fundamentals Hari 1–4 sudah diterjemahkan dan diperiksa AI:** 194
halaman kursus sesuai navigasi sumber, termasuk latihan, solusi, dan catatan
pengajar. Ditambah 9 halaman pengantar, penggunaan Cargo, dan panduan pengajar,
cakupan yang dikerjakan mencapai **203 dari 641 halaman Markdown sumber**.

Cakupan lengkap batch ini:

- Pengantar kursus, panduan pengajar, struktur kursus, shortcut keyboard, daftar
  terjemahan, dan penggunaan Cargo.
- Hari 1: Hello World, tipe/nilai, control flow, tuple/array, reference, string,
  dan tipe buatan pengguna.
- Hari 2: pattern matching, method/trait, generics, closure, tipe standard
  library, dan trait standard library.
- Hari 3: pengelolaan memori, ownership, move/copy/clone/drop, smart pointer,
  borrowing, interior mutability, dan lifetime.
- Hari 4: iterator, module/visibility, testing, error handling, Unsafe Rust, dan
  wrapper FFI.

Label navigasi Hari 1–4 juga dilengkapi. Istilah reference diseragamkan,
termasuk perbaikan typo lama pada label tersebut. Materi pendalaman setelah
Fundamentals masih dalam proses; teks yang belum diterjemahkan tetap menggunakan
bahasa Inggris. Banner Indonesia menjelaskan status parsial ini.

Katalog `po/id.po` memiliki **6.922 entri aktif**: **2.136 terisi non-fuzzy**,
**69 fuzzy**, dan **4.717 belum diterjemahkan**. Sebanyak **2.133 pesan**
termasuk dalam pemeriksaan kumulatif. Angka terisi mencakup literal dan istilah
yang sengaja dipertahankan sama, sehingga bukan jumlah prosa baru yang berubah
bahasa. Cakupan per halaman, hash sumber, dan batas Fundamentals tercatat dalam
`TRANSLATION_QA.json`.

**Belum ada review manusia, review independen, atau publikasi.** Istilah
“diterjemahkan” menyatakan cakupan entri, bukan sertifikasi mutu atau validasi
seluruh klaim teknis sumber. Kursus asli memiliki prasyarat pengalaman
memprogram dan dirancang dengan pengajar; penerjemahan tidak mengubahnya menjadi
kursus pemrograman dari nol.

## Acuan sumber dan atribusi

Acuan sumber tetap `baf25efd192d7c68ef0552aa6803c8aba0f77c4f`, yaitu HEAD
upstream yang diverifikasi pada 2026-11-17. Commit ini dipertahankan untuk fase
terjemahan berjalan. Branch kerja: `indonesian`; branch `main` tetap pada
snapshot sebelumnya. Katalog diperbarui pada sesi sebelumnya melalui ekstraksi
native `mdbook-xgettext` dan GNU Gettext `msgmerge`. Perubahan terjemahan tidak
mengedit `msgid` atau berkas sumber Inggris.

Sumber: Google LLC dan kontributor Comprehensive Rust. Prosa/gambar memakai
[CC-BY-4.0](LICENSE-CC-BY); kode/contoh memakai [Apache-2.0](LICENSE).
Kontribusi terdahulu Aji Prio Sejati tetap dikreditkan melalui metadata
`X-Previous-Translator`. Terjemahan dan pemeriksaan sesi ini dikerjakan Codex
(AI) untuk proyek `atalariq`. Ini terjemahan komunitas, bukan klaim dukungan
resmi Google.

Blok kode, komentar kode, string/output contoh, perintah, identifier, dan notice
kode dipertahankan. Diagram ASCII yang berada dalam blok kode juga
dipertahankan; istilah penunjangnya dijelaskan dalam glosarium. Glosarium Rust
Fundamentals diperluas untuk membantu pembacaan istilah tanpa mengubah teks
penulis asli.

## Pemeriksaan aktual

- GNU Gettext `msgfmt --check --statistics` lulus untuk katalog hasil akhir.
- Audit batch lulus untuk 2.133 pesan non-fuzzy: literal, target tautan, markup
  terkait, dan hash seluruh 641 halaman sumber tetap sesuai.
- Batas navigasi Fundamentals diperiksa: seluruh **194/194 halaman** yang
  ditautkan antara Hari 1 dan akhir Hari 4 termasuk dalam cakupan yang
  dikerjakan, tanpa entri kosong/fuzzy.
- Build HTML Indonesia dengan backend exerciser, xgettext, dan
  `mdbook-linkcheck2` 0.13.0 berhasil.
- Audit render lulus: **858 halaman HTML**, **1.376 blok `pre` identik** antara
  Inggris dan Indonesia, serta **1.302 tautan lokal** pada 203 halaman yang
  dikerjakan valid. Angka blok mencakup salinan pada halaman print, bukan jumlah
  contoh kode unik.
- Pemeriksaan browser pada latihan error handling memastikan judul dan uraian
  Indonesia tampil, contoh kode tetap tersedia, serta viewport 390 piksel tidak
  mengalami overflow halaman. Ini bukan uji perangkat fisik.
- PDF belum dibangun. Unduhan PDF yang tidak tersedia pada build lokal
  dilaporkan terpisah, sesuai pengecualian link checker sumber. Backend
  `mdbook-pandoc` tidak diklaim lulus.
- Konfigurasi dprint upstream saat ini tidak menyediakan formatter PO. Katalog
  diformat menggunakan GNU Gettext `msgcat --width=80`, kemudian diperiksa
  dengan `msgfmt`. Ini bukan klaim bahwa pemeriksaan dprint PO lulus.

Perintah audit, dengan GNU Gettext pada PATH:

```sh
python3 scripts/check-id-translation.py
python3 scripts/check-id-rendered.py /tmp/comprehensive-rust-en/html /tmp/comprehensive-rust-id/html
```

Untuk build, sediakan tool native yang tercantum di README/TRANSLATIONS,
termasuk preprocessor course, gettext, svgbob, dan backend exerciser. Gunakan
perintah yang tidak mengubah checkout sumber:

```sh
mdbook build -d /tmp/comprehensive-rust-en
MDBOOK_BOOK__LANGUAGE=id MDBOOK_OUTPUT__HTML__SITE_URL=/comprehensive-rust/id/ mdbook build -d /tmp/comprehensive-rust-id
```

Jangan menjalankan `.github/workflows/build.sh` langsung pada checkout kerja:
script itu melakukan restore versi sumber berdasarkan tanggal POT. Build di atas
memakai commit acuan saat ini tanpa restore atau penghapusan sumber.

## Masalah dari sumber

Build Inggris dan Indonesia sama-sama memperlihatkan warning tag HTML yang tidak
seimbang pada sejumlah halaman smart pointer, macro, Chromium, dan unsafe deep
dive. Outline Unsafe pada halaman struktur kursus juga menghasilkan
`not found - {{%course outline Unsafe}}`. Diagnostik ini dipertahankan dan
halaman tersebut tetap ditandai memiliki masalah sumber, meskipun semua prosa
lainnya diterjemahkan.

Instruksi Fibonacci mempertahankan keterangan sumber tentang `n` mencapai 48
pada isi utama dan “sekitar 47” pada catatan pengajar. Contoh unsafe yang memang
ditandai unsound tetap demikian; penerjemahan tidak mengganti contoh menjadi
implementasi berbeda. Tidak ada klaim bahwa seluruh latihan sudah dieksekusi
atau seluruh contoh aman dijalankan.

## Pekerjaan yang masih terbuka

Selesaikan pendalaman di luar Fundamentals: macro, Android, Chromium,
bare-metal, concurrency, idiomatic Rust, dan unsafe deep dive, termasuk WIP
serta materi pendampingnya. Mulai dari unit macro berikut Fundamentals dalam
navigasi sumber. Setiap batch memerlukan perbandingan makna, audit kode/tautan,
dan build ulang. Jangan menghapus flag fuzzy tanpa memeriksa isinya.

Refresh katalog dan perubahan terjemahan perlu dipisahkan saat menyiapkan
commit/PR agar jelas ditinjau. Pemeliharaan mengikuti pemeriksaan upstream per
kuartal, dengan penandaan perlu pembaruan untuk halaman terdampak. Koreksi makna
serius ditangani tanpa menunggu jadwal; laporan dapat disampaikan melalui GitHub
Issues fork dengan path, kutipan, dan sumber pembanding.

Google Engineering Practices telah memiliki 14/14 halaman terjemahan dalam repo
terpisah. Missing Semester seluruh edisi dan System Design Primer belum
dikerjakan pada tahap penerjemahan ini dan tetap dalam cakupan pekerjaan
berikutnya. Tidak ada repo yang dipush atau dideploy.

Snapshot cuplikan asli paket editorial dikecualikan secara sempit dari formatter
untuk menjaga petikan verbatim. Pemeriksaan typo sumber Inggris tetap aktif;
pengecualian tambahan hanya mencakup dokumen prosa Indonesia terkait terjemahan.
