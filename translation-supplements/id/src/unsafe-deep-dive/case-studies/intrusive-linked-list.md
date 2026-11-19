<!--
Copyright 2026 Google LLC
SPDX-License-Identifier: CC-BY-4.0
-->

# Intrusive Linked List Tokio

> Sesuai dengan tokio v1.48.0

Proyek Tokio memelihara [implementasi intrusive linked list][ill] yang
memperlihatkan banyak use case `unsafe` serta sejumlah tipe dan trait dari
ekosistem unsafe Rust, termasuk `cell::UnsafeCell`, `mem::ManuallyDrop`,
[pinning](../pinning/what-pinning-is.md), dan unsafe trait.

Linked list merupakan struktur data yang sulit diimplementasikan dalam Rust karena
sangat bergantung pada alamat memory yang tetap stabil. Hal ini tidak
terjadi secara alami, karena tipe Rust berganti alamat memory setiap kali
dipindahkan.

## Penelusuran Awal

API publik disediakan oleh tipe `LinkedList<L, T>`, yang memuat field
untuk awal dan akhir list. `Option<NonNull<T>>` dapat dibaca sebagai
`Option<*mut T>`, dengan jaminan bahwa null pointer tidak akan pernah dibuat.

`NonNull<T>` bersifat "_covariant_ terhadap `T`", yang berarti `NonNull<T>` mewarisi
hubungan [variance] dari `T`.

```rust,ignore
# // Copyright 2026 Google LLC
# // SPDX-License-Identifier: Apache-2.0
#
use core::marker::PhantomData;

// ...

/// An intrusive linked list.
///
/// Currently, the list is not emptied on drop. It is the caller's
/// responsibility to ensure the list is empty before dropping it.
pub(crate) struct LinkedList<L, T> {
    /// Linked list head
    head: Option<NonNull<T>>,

    /// Linked list tail
    tail: Option<NonNull<T>>,

    /// Node type marker.
    _marker: PhantomData<*const L>,
}
```

`LinkedList` tidak bersifat `Send` maupun `Sync`, kecuali targetnya memiliki sifat tersebut.

```rust,ignore
# // Copyright 2026 Google LLC
# // SPDX-License-Identifier: Apache-2.0
#
unsafe impl<L: Link> Send for LinkedList<L, L::Target> where L::Target: Send {}
unsafe impl<L: Link> Sync for LinkedList<L, L::Target> where L::Target: Sync {}
```

Trait `Link` yang digunakan pada trait bound tersebut didefinisikan berikutnya. `Link` adalah
unsafe trait yang mengelola hubungan antar node ketika list perlu
meneruskan reference ke pemanggil di luar.

Berikut definisi trait tersebut. Method terpentingnya adalah `pointers()`, yang
mengembalikan struct `Pointers`. `Pointers` menyediakan akses ke kedua ujung
link dengan menandai dirinya sebagai `!Unpin`.

```rust,ignore
# // Copyright 2026 Google LLC
# // SPDX-License-Identifier: Apache-2.0
#
pub unsafe trait Link {
    type Handle;

    type Target;

    fn as_raw(handle: &Self::Handle) -> NonNull<Self::Target>;

    unsafe fn from_raw(ptr: NonNull<Self::Target>) -> Self::Handle;

    /// # Safety
    ///
    /// The resulting pointer should have the same tag in the stacked-borrows
    /// stack as the argument. In particular, the method may not create an
    /// intermediate reference in the process of creating the resulting raw
    /// pointer.
    unsafe fn pointers(
        target: NonNull<Self::Target>,
    ) -> NonNull<Pointers<Self::Target>>;
}
```

Di `Pointers` inilah bagian menariknya terjadi:

```rust,ignore
# // Copyright 2026 Google LLC
# // SPDX-License-Identifier: Apache-2.0
#
pub(crate) struct Pointers<T> {
    inner: UnsafeCell<PointersInner<T>>,
}

struct PointersInner<T> {
    prev: Option<NonNull<T>>,
    next: Option<NonNull<T>>,

    /// This type is !Unpin due to the heuristic from:
    /// <https://github.com/rust-lang/rust/pull/82834>
    _pin: PhantomPinned,
}
```

## Catatan

Memahami seluruh implementasinya memerlukan waktu, tetapi merupakan pengalaman
yang bermanfaat. Kode ini menunjukkan cara menggabungkan banyak bagian ekosistem
unsafe Rust menjadi struktur data yang dapat digunakan dan memiliki performance tinggi. Selamat menjelajah!

[ill]: https://docs.rs/tokio/1.48.0/src/tokio/util/linked_list.rs.html
[variance]: https://doc.rust-lang.org/reference/subtyping.html
