<!--
Copyright 2024 Google LLC
SPDX-License-Identifier: CC-BY-4.0
-->

# Materi Kursus

Berkas dalam direktori ini membentuk materi kursus. Berkas di sini
juga dapat menyertakan materi pihak ketiga dari `../third_party/`.

Saat menerbitkan terjemahan kursus, kami menggunakan `git restore` untuk mengembalikan direktori `src/` dan
`third_party/` di root repository ke tanggal yang tercantum pada
header POT-Creation-Date terjemahan. **Seluruh materi yang dapat diterjemahkan
harus berada dalam kedua direktori tersebut.** Berkas lainnya (seperti
`book.toml` dan `theme/`) tidak dikembalikan, dan kami selalu menggunakan versi
terbarunya.
