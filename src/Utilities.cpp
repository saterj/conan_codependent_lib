#include "Utilities.h"
#include <algorithm>

Utilities::Utilities() 
{
}

Utilities::~Utilities() 
{
}

void Utilities::NullArray(char array[], int size)
{
	// Counter Declaration
	int ctr = 0;
	printf(FilePaths::stuff.c_str());

	while (ctr <= size)
	{
		array[ctr] = '\0';
		ctr++;
	} // while

	return;
}

