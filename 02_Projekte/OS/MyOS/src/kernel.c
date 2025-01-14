#include <stdint.h>

#define KEYBOARD_DATA_PORT 0x60
#define VIDEO_MEMORY (char*) 0xB8000

int cursor_pos = 0;

extern void load_idt();
extern void set_idt_gate(int n, uint32_t handler);

void init_idt() {
    load_idt();
}


uint8_t inb(uint16_t port) {
    uint8_t result;
    asm volatile("inb %1, %0" : "=a"(result) : "Nd"(port));
    return result;
}

char scancode_to_ascii(uint8_t scancode) {
    static char keymap[] = {
        0, 27, '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '\b',
        '\t', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\n',
        0, 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', '`',
        0, '\\', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 0,
        '*', 0, ' ', 0, // usw.
    };

    if (scancode >= sizeof(keymap)) {
        return 0;
    }

    return keymap[scancode];
}

void print_char(char c) {
    char *video_memory = VIDEO_MEMORY;
    video_memory[cursor_pos * 2] = c;
    video_memory[cursor_pos * 2 + 1] = 0x07;
    cursor_pos++;
}

void print_string(const char *str) {
    for (int i = 0; str[i] != '\0'; i++) {
        print_char(str[i]);
    }
}


void keyboard_handler() {
    uint8_t scancode = inb(KEYBOARD_DATA_PORT);
    char ascii = scancode_to_ascii(scancode);

    if (ascii) {
        print_char(ascii);
    }
}

void init_keyboard() {
    set_idt_gate(33, (uint32_t)keyboard_handler);
}

void kernel_main(unsigned long magic, unsigned long addr) {
    print_string("Hello, Salamana Leckum OS!");
    print_string("Type something");
    
    init_idt();
    init_keyboard();

    asm volatile("sti");

    while (1);
}