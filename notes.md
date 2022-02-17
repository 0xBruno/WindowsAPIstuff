# Windows API
- Dynamic entry which can change and expand between releases
- Official implementation is on your Windows machine (in DLLs)
    - kernel32.dll, user32.dll, ntdll.dll in Windows System directory.
- Ctypes enables us to wrap Python around C 
    - "Speaking C" lets us interface with the Windows API

## Hacker focused API calls
1. OpenProcess
2. CreateRemoteThread
3. WriteProcessMemory


# Unicode & ANSII

The win32 API will have unicode and ansii version of functions:
- unicode "W" appended to the name
- ansii "A" appended to the name


