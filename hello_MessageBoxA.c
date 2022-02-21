#include <stdio.h>
#include <windows.h>

void main(){
    HWND hWnd; 
    LPCSTR lpText, lpCaption;
    UINT uType; 
    

    hWnd = NULL; 
    lpText = "Hello World!";
    lpCaption = "Win32 from C!";
    // MB_OK
    uType = 0x00000000L; 

    MessageBoxA(hWnd, lpText, lpCaption, uType); 
}