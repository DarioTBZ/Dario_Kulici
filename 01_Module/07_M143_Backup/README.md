# Backup Systeme

Command zum Qemu starten: 
qemu-system-x86_64 \                                                                                                                                            

-m 8192 \

-cpu qemu64 \

-smp 4 \

-drive file=truenas_scale_disk.qcow2,format=qcow2 \

-net nic \

-net user \

-vga virtio \