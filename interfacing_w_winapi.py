from ctypes import * 
from ctypes.wintypes import HWND, LPCSTR, UINT, INT, LPSTR, LPDWORD
from winsound import MB_OK

MessageBoxA = windll.user32.MessageBoxA
MessageBoxA.argtypes = (HWND, LPCSTR, LPCSTR, UINT)
MessageBoxA.restype = INT

lpText = LPCSTR(b"Hello World!")
lpCaption = LPCSTR(b"Win32API from Python!")
uType = UINT(MB_OK)

MessageBoxA(None, lpText, lpCaption, uType)



