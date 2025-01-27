section .data
idt: times 256 dq 0        ; Platz für 256 Einträge (64 Bit pro Eintrag)
idt_ptr:                   ; IDT-Pointer (6 Bytes: Größe + Adresse)
    dw 256 * 8 - 1         ; Größe der IDT (256 Einträge à 8 Byte)
    dd idt                 ; Adresse der IDT

section .text
global load_idt
global set_idt_gate

; *** Funktion: load_idt ***
; Lädt die IDT mittels lidt-Befehl
load_idt:
    lidt [idt_ptr]       ; Läd den IDT-Pointer in die CPU
    ret

; *** Funktion: set_idt_gate ***
; Parameter:
; - [esp + 4]: Interrupt-Nummer (Index in der IDT)
; - [esp + 8]: Adresse des Handlers
set_idt_gate:
    pusha
    mov eax, [esp + 4]
    mov ebx, [esp + 8]
    shl eax, 3
    lea ecx, [idt + eax]

    mov word [ecx], bx
    mov word [ecx + 2], 0x08
    mov byte [ecx + 4], 0
    mov byte [ecx + 5], 0x8E
    shr ebx, 16
    mov word [ecx + 6], bx

    popa
    ret

; *** GNU-Stack-Sektion ***
section .note.GNU-stack noalloc noexec nowrite progbits
