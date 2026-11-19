---
minutes: 1
---

<!--
Copyright 2025 Google LLC
SPDX-License-Identifier: CC-BY-4.0
-->

# Mengapa mempelajari unsafe Rust?

Kita tahu bahwa menulis kode tanpa jaminan yang disediakan Rust ...

> “Use-after-free (UAF), integer overflow, serta read/write out of bounds (OOB)
> mencakup 90% kerentanan, dengan OOB sebagai yang paling umum.”
>
> — **Jeff Vander Stoep and Chong Zhang**, Google.
> "[Queue the Hardening Enhancements](https://security.googleblog.com/2019/05/queue-hardening-enhancements.html)"

... jadi mengapa `unsafe` menjadi bagian dari bahasa ini?

## Garis Besar

{{%segment outline}}

<details>

Keyword `unsafe` ada karena belum tersedia teknologi compiler
yang membuatnya tidak lagi diperlukan. Compiler tidak dapat memverifikasi semuanya.

</details>
