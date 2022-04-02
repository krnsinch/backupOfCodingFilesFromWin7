/*
Typecasting is a way to convert one data type into another one
It is also known as data conversion or type conversion.
 
C Language Provides two methods of type casting :
Implicit type casting
Explicit type casting

Implicit type casting : - program automatically converts the variable from one data type to other, 
                        without losing its original meaning or sense. 
                        - It follows strict rules in converting data type of variables as it always
                        converts lower data types to higher ones.

Explicit type casting : Explicit type casting means conversion of data type from one to
                        another forcefully by programmer. It is user defined conversion.
 
*/

#include <stdio.h>

int main()
{
    short n = 24;

    printf("%f\n", (float)n); // accessing data from n variable by typecasting its data to float data type
    printf("%d\n", n);
}
