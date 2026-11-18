# Checklist dan catatan review

## Status paket saat penyerahan

- Delapan draf dibuat oleh Codex (AI), dibandingkan dengan cuplikan sumber lokal
  dan diperiksa secara struktural.
- Identitas commit, rentang baris, hash, sumber lisensi, dan atribusi tercatat
  dalam `sources.json`.
- Kode Rust pada contoh borrowing disalin utuh; literal, penekanan, dan tautan
  dibandingkan pada seluruh pasangan contoh.
- Belum ada review manusia, penilaian pembaca pemula, build situs terjemahan,
  pengujian latihan, atau publikasi. Paket tidak menyatakan hal-hal itu sudah
  lulus.
- Pengecualian penyajian: cuplikan CL hanya pengantar dan butir pertama;
  cuplikan shell berakhir sebelum daftar platform. Batas petikan dinyatakan,
  bukan dianggap sebagai cakupan halaman penuh.

## Hasil pemeriksaan aktual — 2026-11-17

Pemeriksaan lokal dengan Python standar, tanpa instalasi dependency:

| Pemeriksaan                                                          | Hasil                 |
| -------------------------------------------------------------------- | --------------------- |
| Pasangan sumber dan draf                                             | 8/8; 16 blok Markdown |
| Hash SHA-256 snapshot, commit checkout, dan rentang sumber           | 8/8 cocok             |
| Kesamaan blok kode, inline literal, dan target tautan antar pasangan | 8/8 cocok             |
| Literal `Nit:` beserta spasi akhirnya                                | Dipertahankan         |
| Tautan lokal dokumen paket                                           | 7/7 tujuan tersedia   |
| Whitespace seluruh berkas paket, termasuk untracked                  | Lulus                 |

Pemeriksaan tautan dokumen mengecualikan blok kutipan: tautan relatif asli di
dalam contoh memang mengacu pada struktur proyek sumber. URL upstream pada
atribusi dikunci ke commit, tetapi ketersediaan HTTP semua tautan commit
tersebut belum diuji. Pemeriksaan struktur tidak membuktikan kealamian atau
ketepatan makna; delapan pasangan juga telah dibandingkan oleh AI dengan alasan
editorial yang ditulis per contoh. Belum ada bukti review manusia.

## Checklist per unit

Simpan hasil dengan identitas unit, commit sumber, tanggal, pembuat draf,
pemeriksa (manusia/AI), temuan, keputusan, dan bukti. Centang hanya setelah
benar-benar diperiksa.

- [ ] Seluruh proposisi sumber, kondisi, negasi, pengecualian, dan tingkat
      keharusan tetap ada.
- [ ] Tidak ada ringkasan, klaim tambahan tanpa label, atau perubahan tingkat
      kepastian.
- [ ] Pembaca dapat memahami kalimat tanpa harus menerjemahkannya kembali ke
      Inggris.
- [ ] Istilah cocok dengan glosarium dan konteks; kata umum tidak bercampur
      Inggris tanpa alasan.
- [ ] Catatan penerjemah terpisah dan memiliki tanggal/rujukan bila diperlukan.
- [ ] Kode, komentar kode, output, identifier, literal, dan URL referensi utuh.
- [ ] Heading, penekanan, daftar, dan tautan tetap membawa makna yang sama.
- [ ] Atribusi, lisensi, riwayat kontribusi, dan penandaan perubahan tersedia.
- [ ] Review AI dan manusia dibedakan; tidak ada klaim review yang belum
      dilakukan.

## Pemeriksaan tambahan sebelum rilis produksi

- [ ] Inventaris mencakup seluruh halaman, latihan, solusi tersedia, catatan
      pengajar, WIP, media teks, dan unduhan yang disepakati.
- [ ] Tidak ada terjemahan kosong, fuzzy yang diklaim selesai, atau penanda
      pekerjaan tertunda dalam unit siap.
- [ ] Semua tautan internal serta anchor hasil render valid; fallback Inggris
      diberi label.
- [ ] Build native dan pemeriksaan kode yang relevan berhasil; simpan perintah
      serta hasil aktual.
- [ ] Tampilan ponsel, keyboard, hierarki heading, alt text, dan keterbacaan
      kode diperiksa.
- [ ] Tautan eksternal bermasalah ditangani menurut dampaknya; blocker latihan
      tidak disembunyikan.
- [ ] Perbandingan sumber oleh manusia selesai sebelum menggunakan status review
      manusia atau siap belajar menurut gerbang yang disepakati.
- [ ] Commit acuan, status, batas cakupan, dan kanal GitHub Issues terlihat oleh
      pembaca.

## Skenario yang harus ditolak

| Masalah                                             | Mengapa gagal                                                    |
| --------------------------------------------------- | ---------------------------------------------------------------- |
| “Unsafe Rust selalu menyebabkan undefined behavior” | Menghapus kondisi if dan mengubah can menjadi kepastian.         |
| “Reviewer harus memberi komentar Nit”               | Mengubah kebebasan memberi komentar menjadi kewajiban.           |
| “Semua platform sudah memiliki terminal”            | Menghapus nearly/probably serta mengacaukan shell dan terminal.  |
| “Throughput adalah waktu satu operasi”              | Menukar definisi throughput dan latency.                         |
| Semua empat teknik scaling diwajibkan               | Mengubah daftar contoh bersyarat menjadi resep universal.        |
| Mengganti `echo $SHELL` dengan perintah lain        | Memperbarui contoh tanpa izin dalam pekerjaan terjemahan.        |
| Mengklaim seluruh halaman selesai dari cuplikan     | Menyamakan cakupan contoh editorial dengan kelengkapan produksi. |

## Catatan untuk penilai pengguna

Nilai delapan contoh dari akurasi, kelengkapan dalam batas petikan, kealamian,
konsistensi istilah, serta kejelasan bagi pemula. Sebutkan nomor contoh, frasa
yang bermasalah, dan alasannya. Preferensi gaya dapat direvisi; syarat menjaga
makna dan keutuhan literal tetap wajib. Temuan serius diperbaiki sebelum pedoman
dianggap stabil.
