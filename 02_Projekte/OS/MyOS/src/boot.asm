BITS 32
global _start
extern kernel_main

section .text
    align 4
    dd 0x1BADB002
    dd 0x00
    dd -(0x1BADB002 + 0x00)

section .text
_start:
    mov esp, 0x90000
    call kernel_main
    hlt

section .note.GNU-stack noalloc noexec nowrite progbits