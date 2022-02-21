from ctypes import *
from ctypes import wintypes

kernel32 = windll.kernel32
SIZE_T = c_size_t

VirtualAlloc = kernel32.VirtualAlloc
VirtualAlloc.argtypes = (wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.DWORD)
VirtualAlloc.restype = wintypes.LPVOID

MEM_COMMIT      = 0x00001000
MEM_RESERVE     = 0x00002000

# Memory Protection Constant
# https://docs.microsoft.com/en-us/windows/win32/memory/memory-protection-constants
PAGE_EXECUTE_READWRITE = 0x40

mem_alloc_size = 1024 * 12

ptr = VirtualAlloc(None, mem_alloc_size, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)

error = GetLastError()

if error:
    print(error)
    print(WinError(error))

print("VirtualAlloc: ", hex(ptr))
print(f"Size of memory allocated: {mem_alloc_size} bytes")

input()