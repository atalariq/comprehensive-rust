# Status terjemahan Indonesia

Diperiksa pada 2026-11-19. Acuan sumber: `baf25efd192d7c68ef0552aa6803c8aba0f77c4f`.

Seluruh 6.922 entri aktif katalog Indonesia telah terisi: 0 fuzzy dan 0 kosong. Cakupan inventaris adalah 641 berkas Markdown sumber: 628 halaman materi buku, satu berkas navigasi, serta 12 berkas pendukung atau WIP yang tidak masuk navigasi upstream. Dua belas berkas terakhir diterjemahkan lengkap secara terpisah di `translation-supplements/id/`; tersedia sebagai Markdown, dengan status WIP dan referensi lama dari sumber tetap dijelaskan. Berkas sumber Inggris dan seluruh source code tidak diubah.

Terjemahan dibuat dengan bantuan Codex dan worker OpenCode/Hermes menggunakan DeepSeek, lalu diperiksa oleh agent Codex lain. Seluruh 60 batch baru (4.786 entri), materi Fundamentals terdahulu, tiga label navigasi lama, dan 12 berkas pendukung telah diperiksa. Sebanyak 41 koreksi hasil review telah diterapkan, termasuk jumlah sumpit pada latihan deadlock, karakter literal Rust, arah negasi, istilah cache key, dan kekuatan kata should/must. Ini review AI, bukan review manusia atau sertifikasi kebenaran materi.

## Validasi aktual

- GNU `msgfmt --check` dan audit katalog lulus; seluruh 641 hash sumber tetap sama.
- Build HTML Inggris dan Indonesia lulus tanpa pemulihan sumber berdasarkan tanggal PO.
- Sebanyak 858 HTML dibandingkan; seluruh 1.376 block `pre` dan multiset literal inline code identik. Urutan inline code boleh mengikuti tata bahasa Indonesia setelah review makna.
- Audit tautan memakai mount proyek sebenarnya `/comprehensive-rust/`, mencakup tautan lintas locale, anchor, dan ZIP latihan. Hasil final tercatat dalam `TRANSLATION_QA.json`.
- ZIP latihan dibuat untuk kedua locale. PDF Indonesia tidak dibuat; tautan PDF secara eksplisit mengarah ke PDF sumber Inggris.
- Picker bahasa hanya menawarkan locale Inggris dan Indonesia yang diterbitkan oleh fork ini.

## Materi sumber dan lisensi

Penulis asli: Google dan kontributor Comprehensive Rust. Materi berlisensi CC BY 4.0; source code mengikuti notice Apache 2.0 yang menyertainya. Notice asli, kode, komentar kode, perintah, output, identifier, dan target rujukan dipertahankan. Terjemahan komunitas ini tidak menyiratkan dukungan resmi Google.

Warning HTML tidak seimbang dan outline Unsafe yang tidak ditemukan muncul pada build Inggris maupun Indonesia. Keduanya merupakan diagnostik sumber yang dipertahankan, bukan perubahan terjemahan. Pernyataan historis dan contoh unsafe yang sengaja unsound tetap mengikuti sumber. Tidak ada klaim bahwa setiap latihan atau seluruh contoh telah dieksekusi.

README pendukung tentang pemulihan sumber menurut tanggal PO menggambarkan workflow upstream historis. Workflow fork `scripts/build-pages.sh` membangun source pin secara langsung dan tidak menghapus atau me-restore `src/` maupun `third_party/`.

## Publikasi dan pemeliharaan

Release lokal telah divalidasi; status publikasi HTTP dicatat setelah deployment terverifikasi. Situs fork menggunakan project Pages dan pengaturan domain akun yang diwariskan, tanpa mengubah DNS atau repository situs pribadi.

Saat upstream berubah, perbarui source pin dan inventaris hash, lalu tinjau ulang entri terdampak. Jangan menghapus fuzzy tanpa review. Laporan koreksi dapat dikirim melalui GitHub Issues fork dengan path, kutipan, dan rujukan sumber. Penulis asli dan kontributor terjemahan sebelumnya tetap dikreditkan.
