<!--
Copyright 2022 Google LLC
SPDX-License-Identifier: CC-BY-4.0
-->

# FFI yang Ditulis Manual

Kita dapat mendeklarasikan fungsi eksternal secara manual:

```rust
# // Copyright 2022 Google LLC
# // SPDX-License-Identifier: Apache-2.0
#
unsafe extern "C" {
    safe fn abs(x: i32) -> i32;
}

fn main() {
    let x = -42;
    let abs_x = abs(x);
    println!("{x}, {abs_x}");
}
```

Kita sudah melihatnya pada
[latihan Safe FFI Wrapper](../../exercises/day-3/safe-ffi-wrapper.md).

> Ini mengasumsikan pemahaman menyeluruh tentang platform tujuan. Tidak direkomendasikan untuk
> production.

<details>

- Ini hanya contoh pengantar. Untuk library yang sesungguhnya, sebaiknya gunakan
  `bindgen` seperti yang ditunjukkan pada slide berikutnya.

</details>
