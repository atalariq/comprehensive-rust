# Delapan contoh terjemahan beranotasi

Status seluruh contoh: diperiksa AI; menunggu penilaian pengguna. Ini cuplikan
editorial, bukan terjemahan penuh halaman. Heading tampilan yang tidak termasuk
petikan ditulis sebagai label di luar blok. Teks asli dan terjemahan dibungkus
blok Markdown agar URL relatif, anchor, dan literal dapat dibandingkan tanpa
berpura-pura menjadi halaman produksi.

Lisensi tiap cuplikan berlaku juga pada terjemahannya. Keterangan perubahan:
penerjemahan Inggris → Indonesia oleh Codex (AI), 2026-11-17; alasan perubahan
dijelaskan per contoh. Tidak ada dukungan resmi penulis sumber yang diklaim.

## 1. Borrowing a Value → Meminjam Nilai

Sumber:
[comprehensive-rust: src/borrowing/shared.md, baris 10–37](https://github.com/google/comprehensive-rust/blob/c271ecdcb63c37195fcc9715039a96ed7d758e80/src/borrowing/shared.md#L10-L37).

Atribusi: Google LLC dan kontributor. Lisensi:
[CC-BY-4.0](https://github.com/google/comprehensive-rust/blob/c271ecdcb63c37195fcc9715039a96ed7d758e80/LICENSE-CC-BY).

### Asli

````markdown
# Borrowing a Value

As we saw before, instead of transferring ownership when calling a function, you
can let a function _borrow_ the value:

<!-- mdbook-xgettext: skip -->

```rust,editable
# // Copyright 2023 Google LLC
# // SPDX-License-Identifier: Apache-2.0
#
#[derive(Debug)]
struct Point(i32, i32);

fn add(p1: &Point, p2: &Point) -> Point {
    Point(p1.0 + p2.0, p1.1 + p2.1)
}

fn main() {
    let p1 = Point(3, 4);
    let p2 = Point(10, 20);
    let p3 = add(&p1, &p2);
    println!("{p1:?} + {p2:?} = {p3:?}");
}
```

- The `add` function _borrows_ two points and returns a new point.
- The caller retains ownership of the inputs.
````

### Draf Indonesia

````markdown
# Meminjam Nilai

Seperti yang telah kita lihat, alih-alih memindahkan ownership saat memanggil
fungsi, Anda dapat membiarkan fungsi _meminjam_ nilai tersebut:

<!-- mdbook-xgettext: skip -->

```rust,editable
# // Copyright 2023 Google LLC
# // SPDX-License-Identifier: Apache-2.0
#
#[derive(Debug)]
struct Point(i32, i32);

fn add(p1: &Point, p2: &Point) -> Point {
    Point(p1.0 + p2.0, p1.1 + p2.1)
}

fn main() {
    let p1 = Point(3, 4);
    let p2 = Point(10, 20);
    let p3 = add(&p1, &p2);
    println!("{p1:?} + {p2:?} = {p3:?}");
}
```

- Fungsi `add` _meminjam_ dua titik dan mengembalikan titik baru.
- caller tetap memiliki ownership atas input.
````

### Alasan editorial

“Meminjam” menjelaskan tindakan borrow; istilah ownership dan caller
dipertahankan. “Tetap” menjaga pembedaan ownership input dan nilai baru yang
dikembalikan. Kode disalin utuh, termasuk notice dan directive. Judul
diterjemahkan sebagai frasa tindakan, bukan nama konsep ownership.

## 2. Unsafe Rust → Unsafe Rust

Sumber:
[comprehensive-rust: src/unsafe-rust/unsafe.md, baris 10–21](https://github.com/google/comprehensive-rust/blob/c271ecdcb63c37195fcc9715039a96ed7d758e80/src/unsafe-rust/unsafe.md#L10-L21).

Atribusi: Google LLC dan kontributor. Lisensi:
[CC-BY-4.0](https://github.com/google/comprehensive-rust/blob/c271ecdcb63c37195fcc9715039a96ed7d758e80/LICENSE-CC-BY).

### Asli

````markdown
# Unsafe Rust

The Rust language has two parts:

- **Safe Rust:** memory safe, no undefined behavior possible.
- **Unsafe Rust:** can trigger undefined behavior if preconditions are violated.

We saw mostly safe Rust in this course, but it's important to know what Unsafe
Rust is.

Unsafe code should be small and isolated, and its correctness should be
carefully documented. It should be wrapped in a safe abstraction layer.
````

### Draf Indonesia

````markdown
# Unsafe Rust

Bahasa Rust memiliki dua bagian:

- **Safe Rust:** aman dari sisi memori, tidak memungkinkan undefined behavior.
- **Unsafe Rust:** dapat memicu undefined behavior jika prasyarat dilanggar.

Dalam kursus ini, kita lebih banyak membahas safe Rust, tetapi penting juga
untuk mengetahui apa itu Unsafe Rust.

Kode unsafe sebaiknya berukuran kecil dan terisolasi, dan kebenarannya sebaiknya
didokumentasikan dengan cermat. Kode tersebut sebaiknya dibungkus dalam lapisan
safe abstraction.
````

### Alasan editorial

“Dapat ... jika” mempertahankan kemampuan bersyarat, bukan kepastian bahwa semua
kode unsafe salah. Ketiga anjuran should memakai “sebaiknya”. Pernyataan Safe
Rust mengikuti sumber dan tidak diperluas menjadi janji bahwa aplikasi bebas
bug.

## 3. What is Small? → Seberapa Kecil?

Sumber:
[google-engineering-practices: review/developer/small-cls.md, baris 46–53](https://github.com/google/eng-practices/blob/3bb3ec25b3b0199f4940b1aa75f0ac5c5753301c/review/developer/small-cls.md#L46-L53).

Atribusi: Google dan kontributor. Lisensi:
[CC-BY-3.0](https://github.com/google/eng-practices/blob/3bb3ec25b3b0199f4940b1aa75f0ac5c5753301c/LICENSE).

### Asli

````markdown
In general, the right size for a CL is **one self-contained change**. This means
that:

-   The CL makes a minimal change that addresses **just one thing**. This is
    usually just one part of a feature, rather than a whole feature at once. In
    general it's better to err on the side of writing CLs that are too small vs.
    CLs that are too large. Work with your reviewer to find out what an
    acceptable size is.
````

### Draf Indonesia

````markdown
Secara umum, ukuran CL yang tepat adalah **satu perubahan yang utuh dan
mandiri**. Artinya:

- CL membuat perubahan minimal yang menangani **satu hal saja**. Biasanya, ini
  hanya satu bagian dari suatu fitur, bukan seluruh fitur sekaligus. Secara
  umum, lebih baik membuat CL yang terlalu kecil daripada terlalu besar.
  Diskusikan dengan reviewer Anda untuk menentukan ukuran yang dapat diterima.
````

### Alasan editorial

“Secara umum” dan “biasanya” tetap ada. Self-contained dijelaskan sebagai “utuh
dan mandiri”; ini tidak menambah larangan tentang dependency. CL dan reviewer
tetap istilah Inggris. Cuplikan hanya mencakup pengantar dan butir pertama,
bukan seluruh daftar sumber.

## 4. The Standard of Code Review → Standar Code Review

Sumber:
[google-engineering-practices: review/reviewer/standard.md, baris 51–58](https://github.com/google/eng-practices/blob/3bb3ec25b3b0199f4940b1aa75f0ac5c5753301c/review/reviewer/standard.md#L51-L58).

Atribusi: Google dan kontributor. Lisensi:
[CC-BY-3.0](https://github.com/google/eng-practices/blob/3bb3ec25b3b0199f4940b1aa75f0ac5c5753301c/LICENSE).

### Asli

````markdown
Reviewers should _always_ feel free to leave comments expressing that something
could be better, but if it's not very important, prefix it with something like
"Nit: " to let the author know that it's just a point of polish that they could
choose to ignore.

Note: Nothing in this document justifies checking in CLs that definitely
_worsen_ the overall code health of the system. The only time you would do that
would be in an [emergency](../emergencies.md).
````

### Draf Indonesia

````markdown
Reviewer sebaiknya _selalu_ merasa leluasa menyampaikan komentar bahwa sesuatu
masih bisa diperbaiki. Namun, jika hal itu tidak terlalu penting, awali komentar
dengan penanda seperti "Nit: " agar penulis tahu bahwa itu hanya penyempurnaan
kecil yang boleh diabaikan.

Catatan: Tidak ada bagian dalam dokumen ini yang membenarkan memasukkan CL yang
jelas-jelas _memperburuk_ code health sistem secara keseluruhan. Satu-satunya
keadaan ketika Anda akan melakukan hal tersebut adalah dalam
[keadaan darurat](../emergencies.md).
````

### Alasan editorial

“Sebaiknya selalu merasa leluasa” mempertahankan should always tanpa membuat
kewajiban memberi komentar. Pilihan mengabaikan Nit tetap ada. Literal "Nit: "
mempertahankan spasi. Negasi, penekanan memperburuk, serta pengecualian
emergency tidak dihilangkan.

## 5. What is the shell? → Apa Itu Shell?

Sumber:
[missing-semester: _2026/course-shell.md, baris 98–107](https://github.com/missing-semester/missing-semester/blob/1d695c94ccafdce3f06d6b9dfe3e6f106097693a/_2026/course-shell.md#L98-L107).

Atribusi: The Missing Semester of Your CS Education: penulis dan kontributor.
Lisensi:
[CC-BY-NC-SA-4.0](https://github.com/missing-semester/missing-semester/blob/1d695c94ccafdce3f06d6b9dfe3e6f106097693a/license.md).

### Asli

````markdown
Nearly all platforms you can get your hands on have a shell in one form
or another, and many of them have several shells for you to choose from.
While they may vary in the details, at their core they are all roughly
the same: they allow you to run programs, give them input, and inspect
their output in a semi-structured way.

To open a shell _prompt_ (where you can type commands), you first need a
_terminal_, which is the visual interface to a shell. Your device
probably shipped with one installed, or you can install one fairly
easily:
````

### Draf Indonesia

````markdown
Hampir semua platform yang dapat Anda gunakan memiliki shell dalam suatu bentuk,
dan banyak di antaranya menyediakan beberapa shell untuk dipilih. Walaupun
detailnya dapat berbeda, pada dasarnya shell-shell tersebut kurang lebih sama:
Anda dapat menjalankan program, memberikan input, dan memeriksa output-nya
secara semi-terstruktur.

Untuk membuka _prompt_ shell (tempat Anda mengetik perintah), Anda terlebih
dahulu memerlukan _terminal_, yaitu antarmuka visual ke shell. Kemungkinan
perangkat Anda sudah dilengkapi terminal, atau Anda dapat memasangnya dengan
cukup mudah:
````

### Alasan editorial

“Hampir”, “kurang lebih”, dan “kemungkinan” mempertahankan ketidakpastian
sumber. Shell, terminal, dan prompt tidak disamakan. Akhir bertanda titik dua
dipertahankan: daftar platform berikutnya berada di luar cuplikan, bukan hilang
dari terjemahan halaman penuh.

## 6. Exercises — Unix shell → Latihan — Unix Shell

Sumber:
[missing-semester: _2026/course-shell.md, baris 560–568](https://github.com/missing-semester/missing-semester/blob/1d695c94ccafdce3f06d6b9dfe3e6f106097693a/_2026/course-shell.md#L560-L568).

Atribusi: The Missing Semester of Your CS Education: penulis dan kontributor.
Lisensi:
[CC-BY-NC-SA-4.0](https://github.com/missing-semester/missing-semester/blob/1d695c94ccafdce3f06d6b9dfe3e6f106097693a/license.md).

### Asli

````markdown
1. For this course, you need to be using a Unix shell like Bash or ZSH. If
   you are on Linux or macOS, you don't have to do anything special. If you
   are on Windows, you need to make sure you are not running cmd.exe or
   PowerShell; you can use [Windows Subsystem for
   Linux](https://docs.microsoft.com/en-us/windows/wsl/) or a Linux virtual
   machine to use Unix-style command-line tools. To make sure you're running
   an appropriate shell, you can try the command `echo $SHELL`. If it says
   something like `/bin/bash` or `/usr/bin/zsh`, that means you're running
   the right program.
````

### Draf Indonesia

````markdown
1. Untuk kursus ini, Anda perlu menggunakan Unix shell seperti Bash atau ZSH.
   Jika Anda menggunakan Linux atau macOS, tidak ada hal khusus yang perlu
   dilakukan. Jika Anda menggunakan Windows, pastikan Anda tidak menjalankan
   cmd.exe atau PowerShell; Anda dapat menggunakan
   [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/)
   atau mesin virtual Linux untuk menggunakan tool command-line bergaya Unix.
   Untuk memastikan Anda menjalankan shell yang sesuai, coba perintah
   `echo $SHELL`. Jika hasilnya seperti `/bin/bash` atau `/usr/bin/zsh`, berarti
   Anda menjalankan program yang tepat.
````

### Alasan editorial

“Perlu” merupakan kebutuhan mengikuti kursus, sedangkan “dapat” menawarkan
pilihan. Linux/macOS, kondisi Windows, nama program, URL, perintah, serta path
dipertahankan. Ini menerjemahkan petunjuk sumber, bukan menambahkan klaim bahwa
latihan telah dijalankan di semua platform.

## 7. Latency vs throughput → Latency dan Throughput

Sumber:
[system-design-primer: README.md, baris 428–432](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/README.md#L428-L432).

Atribusi: Donne Martin dan kontributor; Copyright 2017 Donne Martin. Lisensi:
[CC-BY-4.0](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/LICENSE.txt).

### Asli

````markdown
**Latency** is the time to perform some action or to produce some result.

**Throughput** is the number of such actions or results per unit of time.

Generally, you should aim for **maximal throughput** with **acceptable latency**.
````

### Draf Indonesia

````markdown
**Latency** adalah waktu yang diperlukan untuk melakukan suatu tindakan atau
menghasilkan suatu hasil.

**Throughput** adalah jumlah tindakan atau hasil tersebut per satuan waktu.

Secara umum, Anda sebaiknya menargetkan **throughput maksimal** dengan **latency
yang dapat diterima**.
````

### Alasan editorial

Definisi waktu dan jumlah per satuan waktu tidak tertukar. “Secara umum” serta
“sebaiknya” menjaga sifat anjuran; acceptable tidak diganti “minimal” atau
“nol”.

## 8. Step 4: Scale the design → Langkah 4: Skalakan Desain

Sumber:
[system-design-primer: README.md, baris 261–268](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/README.md#L261-L268).

Atribusi: Donne Martin dan kontributor; Copyright 2017 Donne Martin. Lisensi:
[CC-BY-4.0](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/LICENSE.txt).

### Asli

````markdown
Identify and address bottlenecks, given the constraints.  For example, do you need the following to address scalability issues?

* Load balancer
* Horizontal scaling
* Caching
* Database sharding

Discuss potential solutions and trade-offs.  Everything is a trade-off.  Address bottlenecks using [principles of scalable system design](#index-of-system-design-topics).
````

### Draf Indonesia

````markdown
Identifikasi dan tangani bottleneck dengan mempertimbangkan batasan yang ada.
Misalnya, apakah Anda memerlukan hal-hal berikut untuk menangani masalah
scalability?

- Load balancer
- Horizontal scaling
- Caching
- Database sharding

Bahas solusi yang mungkin beserta trade-off-nya. Setiap pilihan memiliki
trade-off. Tangani bottleneck menggunakan
[prinsip desain sistem yang dapat diskalakan](#index-of-system-design-topics).
````

### Alasan editorial

Daftar tetap pertanyaan kemungkinan, bukan kewajiban memakai keempat teknik.
Batasan, trade-off, dan tautan fragmen dipertahankan. “Scalability” tetap
istilah konsep, sementara label tautan principles diterjemahkan secara alami.
