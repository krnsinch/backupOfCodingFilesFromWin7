/*
Data Types (defines the type of data)-
Built-in     	int, char, float, double
Derived      	array, pointer, structure, union
Enumeration  	enum
Void 	        void

Constants
- Such entities which can not be changed by a computer program
- like literals such as, "cat", 'a', 34, 8.23, etc.
- or constant memeory locations

Variables
a variable is a storage location (identified by a memory address) paired with an associated symbolic name,
which contains a particular type of data
*/

#include <stdio.h>
#define EARTH_GRAVITY 9.8

void main()
{
    /*
    Variable Definition
    Syntax:
    type variable_name;
    or
    type variable_name, variable_name, variable_name;
    */

    /*
    data type specifies to allocate     size and type of data an object(named region of storage) can accomodate

    */
    int volt, current = 45, ohm;  // declaring variables and can also initialize/assign value or later in program
    const float PI = 3.14;

    volt = 25;
    ohm = 34;

    // printf("Circuit details: %d v,  %d i, %d ohm", volt, current, ohm);
    printf("Size of usigned int is %d bytes", sizeof(unsigned int));  // sizeof() operator to get size  
    printf("\nValue of pi is %12.2f", PI);
    printf("\nAcceleration due to gravity on Earth is %-10.1f ms^-2", EARTH_GRAVITY);
    

}

