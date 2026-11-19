---
minutes: 5
---

<!--
Copyright 2026 Google LLC
SPDX-License-Identifier: CC-BY-4.0
-->

# Merujuk Path secara Hygienic

Path item dan crate bersifat unhygienic. Karena itu, path item dalam definisi macro
akan merujuk item yang berbeda dari yang dimaksud jika nama module atau crate
di awal path didefinisikan di call site secara berbeda dari perkiraan penulis macro.

Dalam satu crate, penggunaan path absolut (yang dimulai dengan `::` atau nama
crate) merupakan langkah awal untuk merujuk item tanpa ambiguitas. Namun, nama crate
dapat tertutupi oleh module dalam crate saat ini, atau crate tersebut
dapat diimpor dengan nama berbeda di call site. Jadi, bahkan path absolut pun belum
sepenuhnya andal untuk merujuk item dari macro.

Namun, ada jalan keluarnya: kita dapat merujuk **crate yang mendefinisikan macro**
tanpa ambiguitas hanya melalui metavariable `$crate`.

Ini dapat digunakan untuk merujuk item lokal dari crate yang sama dengan macro
tanpa khawatir ada gangguan, di mana pun call site macro tersebut.

```rust,compile_fail
// Macro-defining crate `custom_vec`
/// A custom Vec type with API similar to the standard one.
pub struct Vec<T>(...);

macro_rules! vec {
    ($elems: $expr) => {
        // Always refers to this crate's `Vec<T>` type, regardless of call-site
        // environment; `$crate` always refers to the macro-defining crate.
        let v = $crate::Vec::new(); for i in $elems { v.push(i); }; v
    };
}

// Main crate, which depends on `custom_vec` but aliases it to the name `cvec`.
type Vec<T> = std::vec::Vec<T>;

fn main() {
    // In this context, `::Vec` is a local type alias of the stdlib's `Vec`.
	let _ = ::Vec::<u8>::new();
	// But the macro expansion's `$crate` still refers to the defining crate,
	// without needing to worry about this crate having renamed its import, or
	// anything else about the local lexical environment.
    let n = cvec::vec!([50]);
}
```

<details>

- Dalam contoh ini, penggunaan keyword `crate` maupun path yang dimulai dengan `::Vec`
  akan sama-sama di-resolve ke type alias dalam crate utama untuk tipe vec dari stdlib.
- Karena crate utama mengganti nama impor crate `custom_vec` menjadi `cvec`,
  path yang dimulai dengan `custom_vec` akan gagal menemukan crate tersebut.
- Path berbasis `$crate` tetap diekspansi dengan benar ke crate yang mendefinisikan macro,
  meskipun ada kendala tersebut.

</details>
