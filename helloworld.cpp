#include "windows.h"
#include "tchar.h"

int _tmain(int argc, TCHAR* argvc[])
{
	MessageBox(NULL,
		L"Hello World!",
		L"www.reversecore.com",
		MB_OK);

	return 0;
}