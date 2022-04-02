#include <stdio.h>

// Instructions for functions are stored in code segment

// function pointers are used to stored the address of instructions of function 
// or to point to the function

int sum(int n1, int n2)
{
    return n1 + n2;
    
}

int main()
{
    printf("%d\n", sum(2, 6));  // testing the function

    // declaring a function pointer
    int (*funcPtr) (int, int);

    // pointing to sum function
    funcPtr = &sum; 

    // calling sum function by de-referencing funcPtr
    int n = (*funcPtr)(2, 6);
    printf("%d\n", n);

    return 0;
}

