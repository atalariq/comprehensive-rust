# Unsafe Rust

The Rust language has two parts:

- **Safe Rust:** memory safe, no undefined behavior possible.
- **Unsafe Rust:** can trigger undefined behavior if preconditions are violated.

We saw mostly safe Rust in this course, but it's important to know what Unsafe
Rust is.

Unsafe code should be small and isolated, and its correctness should be
carefully documented. It should be wrapped in a safe abstraction layer.
