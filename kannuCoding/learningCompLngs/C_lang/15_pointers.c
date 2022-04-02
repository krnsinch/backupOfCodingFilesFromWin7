/*
Base Address : The first byte address of any variable is known as base address/memory address.

Pointer
- a memory location that contains memory address of another memory location.
*/

#include <stdio.h>

int main()
{
    int c = 5;
    int *ptrc = NULL;  // should assign NULL when not assigned any value during initialization
    ptrc = &c;

    // accessing address of variable c
    printf("The address of variable c from pointer ptrc is %d", ptrc);

    // accessing data by dereferencing pointer
    printf("\nThe value of variable c from pointer ptrc is %d", *ptrc);

    // can assign value by dereferencing pointer
    printf("\n\nValue of c is %d", c);
    *ptrc = 7;
    printf("\nNow, value of c is %d", c);

    //////////////////////////////////////
    // Pointer arithmetic
    int n = 2;
    char *p = &n;

    printf("\n\nPointer Arithmetic-");
    printf("\nThe address stored in p is %d", *p);
    p = p + 1;  // pointer + n means pointer + sizeof(type of pointer) * n
    printf("\nNow, address stored in p is %d", p);
    return 0;
}
