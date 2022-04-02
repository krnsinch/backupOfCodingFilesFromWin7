// preprocessor directive - 
// a type of instruction which is executed by preprocessor before compilation

// #include directive
#include <stdio.h> // the angle brackets say to look only in the standard directories
#include "b.c"     // the quotation marks say to look in the current directory first
                   // and if not found then look in standard directories

// disk drive full path can also be used
#include "D:\kannuCoding\learningCompLngs\C_lang\myfolder\this.c"
#include <D:\kannuCoding\learningCompLngs\C_lang\myfolder\that.c>

// -----------------------------------

// define directive
// A macro is a segment of code which is replaced by the value of macro after preprocessing
// Macros are used to make a sequence of computing instructions available to the programmer 
// as a single program statement
#define PI 3.14        // Object-like Macros is an identifier that is replaced by value
#define square(a) a *a // Function-like Macros

int main()
{
    // using variable of other included files
    printf("value of a by including b.c file is %d\n", a);
    printf("acceleration on earth is %f\n", earth_gravity);
    printf("acceleration on mars is %f\n", mars_gravity);

    // using user defined macros
    printf("value of pi is %f\n", PI);
    printf("square of 4 is %d\n", square(4));

    // using predefined macros in C
    printf("\nTime is %s\n", __TIME__);
    printf("Date is %s\n", __DATE__);
    printf("Name of this file is %s\n", __FILE__);
    printf("Line is %d\n", __LINE__);
    printf("ANSI: %d\n", __STDC__); // defines 1 when the compiler compiles with the ANSI standards

    return 0;
}
