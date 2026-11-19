---
minutes: 5
---

<!--
Copyright 2026 Google LLC
SPDX-License-Identifier: CC-BY-4.0
-->

# Mendefinisikan Unsafe Rust

<!-- mdbook-xgettext: skip -->

```bob
╭───────────────────────────────────────────────────────────╮
│╭─────────────────────────────────────────────────────────╮│
││                                                         ││
││  Safe                                                   ││
││  Rust                                                   ││
││                                                         ││
││                                                         ││
│╰─────────╮                                               ││
│          │                                               ││
│  Unsafe  │                                               ││
│   Rust   │                                               ││
│          ╰───────────────────────────────────────────────╯│
╰───────────────────────────────────────────────────────────╯
```

<details>

“Unsafe Rust merupakan superset dari Safe Rust.”

“Unsafe Rust menambahkan kemampuan ekstra, seperti melakukan dereference pada raw
pointer dan memanggil fungsi yang dapat melanggar jaminan safety Rust jika dipanggil
secara tidak benar.”

“Kemampuan ekstra ini disebut _unsafe operations_.”

“Unsafe operation menyediakan fondasi bagi
standard library Rust. Misalnya, tanpa kemampuan melakukan dereference pada raw pointer,
`Vec` atau `Box` tidak mungkin diimplementasikan.”

“Compiler tetap membantu Anda saat menulis Unsafe Rust. Borrow checking
dan type safety tetap berlaku. Unsafe operation memiliki aturannya sendiri, yang akan
kita pelajari di kelas ini.”

</details>
