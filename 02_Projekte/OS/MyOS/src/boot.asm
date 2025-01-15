BITS 32
global _start
extern kernel_main

section .data
msg db "Hello, Kernel!", 0


section .text
global print
print:
    pusha
    mov esi, msg
    mov edi, 0xB8000
.loop:
    lodsb
    cmp al, 0
    je .done
    mov [edi], al
    mov byte [edi + 1], 0x0F
    add edi, 2
    jmp .loop
.done
    popa
    ret

section .text
align 4
dd 0x1BADB002
dd 0
dd -(0x1BADB002 + 0x00)

section .text
_start:
    mov esp, 0x90000
    call kernel_main
    call print
    hlt

section .note.GNU-stack noalloc noexec nowrite progbits