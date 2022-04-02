#include <stdio.h>
#include "temp.c"

// A storage class defines
// - whare variable gets memory allocation 
// - scope
// - default initial value
// - lifetime of variable

// storage classes - 
// auto
// register
// static
// extern

int func(int chVal)
{
    static int n = 20;

    if (chVal < n)
    {
        n = chVal;
    }
    else
    {
        n++;
    }
    return n;
}

int main()
{   
    /*
    extern - used to declare a variable
    A variable declaration provides assurance to the compiler that there exists a variable with the given type and name
    so that the compiler can proceed for further compilation without requiring the complete detail about the variable. 
    A variable definition has its meaning at the time of compilation only, the compiler needs actual variable definition
    at the time of linking the program. so it is useful when you are using multiple files and you define your variable
    in one of the files which will be available at the time of linking of the program. You will use the keyword extern  
    to declare a variable at any place. Though you can declare a variable multiple times in your C program, it can be 
    defined only once in a file, a function, or a block of code.
    */

    printf("the value of n in main function is %d", n);

    // register int x = 23;  // stored in the register of the cpu for faster data transfer
    // int y = 23;  // default to auto storage class stored in the ram
    // printf("The value of x stored in register of the cpu is %d\n", x);
    // printf("The value of y stored in ram is %d", y);
    // printf("value of n returned by func() is %d\n", func(34));
    // printf("value of n returned by func() is %d\n", func(34));
    // printf("value of n returned by func() is %d\n", func(4));
    // printf("value of n returned by func() is %d\n", func(34));
    return 0;
}