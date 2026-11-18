# Paket editorial terjemahan Indonesia

Versi kebijakan: 1.0. Tanggal: 2026-11-17.

Paket ini menjadi acuan terjemahan Comprehensive Rust, Google Engineering
Practices, Missing Semester, dan System Design Primer. Tujuannya membantu
pembaca Indonesia memahami sumber tanpa mengubah materi menjadi ringkasan atau
adaptasi kurikulum.

Urutan baca:

1. [Pedoman editorial](GUIDE.md).
2. [Glosarium awal](GLOSSARY.md).
3. [Delapan contoh beranotasi](SAMPLES.md).
4. [Checklist dan catatan pemeriksaan](REVIEW.md).

Status: contoh disusun dan dibandingkan dengan sumber oleh Codex (AI); belum
dinilai pengguna atau reviewer manusia. Tidak ada klaim review independen. Paket
belum merupakan rilis terjemahan kursus.

Sumber contoh dikunci ke commit checkout lokal dalam [manifest](sources.json),
bukan diklaim sebagai upstream terbaru. Cuplikan asli disimpan verbatim agar
perbandingan dapat diulang. Tautan sumber memakai commit tetap. Paket belum
dipasang ke situs atau katalog PO.

## Batas kerja

Paket editorial disimpan di workspace Rust agar bisa ditinjau bersama. Pada
tahap integrasi, salin kebijakan yang disetujui ke masing-masing repo beserta
versi dan pengecualian lokal; tidak diperlukan repo pusat baru. Mekanisme native
tetap berlaku, khususnya Gettext untuk Rust. Pedoman ini melengkapi, bukan
mengganti, instruksi kontribusi proyek.

Urutan produksi: Google Engineering Practices → Comprehensive Rust → Missing
Semester (2026 → 2020 → 2019) → System Design Primer. Seluruh materi pada edisi
pilihan menjadi target, termasuk WIP, latihan, solusi yang memang tersedia,
catatan pengajar, diagram, dan unduhan buatan proyek. Setiap edisi dilacak
terpisah. Video/audio dan bacaan eksternal tetap ditautkan dalam bahasa asli;
subtitle merupakan pekerjaan tambahan.

## Atribusi dan lisensi

Contoh terjemahan adalah perubahan bahasa oleh Codex untuk proyek terjemahan
`atalariq` (pemilik workspace); bukan terjemahan resmi atau dukungan dari
penulis asli. Nama pemilik publik mengikuti akun `atalariq`; tidak ada atribusi
sebagai penerjemah manusia atas draf AI.

- Comprehensive Rust: Google LLC dan kontributor; prosa/gambar
  [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/), kode/contoh
  [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0). Notice kode pada
  cuplikan dipertahankan.
- Google Engineering Practices: Google dan kontributor;
  [CC-BY-3.0](https://creativecommons.org/licenses/by/3.0/).
- Missing Semester: penulis dan kontributor The Missing Semester of Your CS
  Education;
  [CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
  Terjemahan cuplikannya tetap berlisensi tersebut, termasuk batas nonkomersial
  dan ShareAlike.
- System Design Primer: Copyright 2017 Donne Martin dan kontributor;
  [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).

Lisensi per cuplikan berlaku pada teks sumber dan terjemahannya, bukan
diseragamkan dengan lisensi repo tempat paket disimpan. Pedoman, glosarium, dan
catatan editorial baru dalam paket ini tersedia di bawah CC-BY-4.0, dengan
atribusi proyek terjemahan `atalariq` dan keterangan bantuan AI. Lisensi
spesifik cuplikan mengungguli ketentuan umum ini. Dokumen lisensi sumber
ditautkan per cuplikan; periksa notice tambahan sebelum mengimpor materi lain
atau kontribusi terdahulu.
