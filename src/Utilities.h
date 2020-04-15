#include <stdio.h>
#include <iostream>
#include <string.h>
#ifndef WIN32
#include <unistd.h>
#include "dirent.h"
#endif
#include <cstdlib>
#include <vector>
#include <sstream>
#include <sys/stat.h>
#include <time.h>
#include <math.h>

#include <fstream>
#include <stdint.h>
#include <string>
#include <json/json.h>
#include "File_Paths.h"
#include <mutex>
#include <algorithm>

class Utilities {
public:
	Utilities();
	virtual ~Utilities();

	/*!
	 * \fn NullArray(char array[], int size)
	 * \brief Nulls out a specified array to a specific size.
	 * \param array Character array to nullify.
	 * \param size The size of the array.
	 * \return void
	 */
	void NullArray(char array[], int size);

};
