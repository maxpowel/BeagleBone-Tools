#! /usr/bin/python
# Enable PWM Timer on Beaglebone
# Obtained from https://groups.google.com/forum/#!msg/beagleboard/alKf67dwMHI/b9W2igN6Lr4J
from mmap import mmap
import struct

def enable():
	MMAP_OFFSET = 0x44c00000                # base address of registers
	MMAP_SIZE   = 0x48ffffff-MMAP_OFFSET    # size of the register memory space
	CM_PER_BASE = 0x44e00000 - MMAP_OFFSET
	CM_PER_EPWMSS1_CLKCTRL = CM_PER_BASE + 0xcc
	CM_PER_EPWMSS0_CLKCTRL = CM_PER_BASE + 0xd4
	CM_PER_EPWMSS2_CLKCTRL = CM_PER_BASE + 0xd8
	with open("/dev/mem", "r+b") as f:
		mem = mmap(f.fileno(), MMAP_SIZE, offset=MMAP_OFFSET)
	def _andReg(address, mask):
		""" Sets 32-bit Register at address to its current value AND mask. """
		_setReg(address, _getReg(address)&mask)
	def _orReg(address, mask):
		""" Sets 32-bit Register at address to its current value OR mask. """
		_setReg(address, _getReg(address)|mask)
	def _xorReg(address, mask):
		""" Sets 32-bit Register at address to its current value XOR mask. """
		_setReg(address, _getReg(address)^mask)
	def _getReg(address):
		""" Returns unpacked 32 bit register value starting from address. """
		return struct.unpack("<L", mem[address:address+4])[0]
	def _setReg(address, new_value):
		""" Sets 32 bits at given address to given value. """
		mem[address:address+4] = struct.pack("<L", new_value)
	val = _getReg(CM_PER_EPWMSS1_CLKCTRL)
	if(val != 0x2):
		_setReg(CM_PER_EPWMSS1_CLKCTRL, 0x2)
		open("/sys/kernel/debug/omap_mux/gpmc_a2", 'w').write("6")
		open("/sys/kernel/debug/omap_mux/gpmc_a3", 'w').write("6")
		open("/sys/kernel/debug/omap_mux/mcasp0_aclkx", 'w').write("1")
		open("/sys/kernel/debug/omap_mux/mcasp0_fsx", 'w').write("1")
		open("/sys/kernel/debug/omap_mux/gpmc_ad9", 'w').write("4")
		open("/sys/kernel/debug/omap_mux/gpmc_ad8", 'w').write("4")
		open("/sys/kernel/debug/omap_mux/ecap0_in_pwm0_out", 'w').write("0")
		open("/sys/kernel/debug/omap_mux/mcasp0_ahclkr", 'w').write("4")

