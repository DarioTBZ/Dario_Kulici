CC = gcc
LD = ld
ASM = nasm
CFLAGS = -ffreestanding -m32 -nostdlib -fno-pie
LDFLAGS = -m elf_i386 -Ttext 0x1000 -e_start

SRC = src
BUILD = build
ISO = iso

all: kernel

kernel:
	mkdir -p $(BUILD)
	$(ASM) -f elf $(SRC)/boot.asm -o $(BUILD)/boot.o
	$(ASM) -f elf $(SRC)/idt.asm -o $(BUILD)/idt.o
	$(CC) $(CFLAGS) -c $(SRC)/kernel.c -o $(BUILD)/kernel.o
	$(LD) $(LDFLAGS) -o $(BUILD)/kernel.elf $(BUILD)/boot.o $(BUILD)/kernel.o $(BUILD)/idt.o
	mkdir -p $(ISO)/boot/grub
	cp $(BUILD)/kernel.elf $(ISO)/boot/
	cp $(SRC)/grub.cfg $(ISO)/boot/grub/
	grub-mkrescue -o my_os.iso $(ISO)

run:
	qemu-system-x86_64 -cdrom my_os.iso

clean:
	rm -rf $(BUILD) my_os.iso
