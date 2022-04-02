/*
Two ways to call a function-
Call by value: the value of the argument is copied into the formal parameters.
Call by reference: the address of argument is copied into the formal parameter.
*/

#include <stdio.h>

int Value(int x)
{
    return x;
}

void changeValue(int *x)
{
    *x = *x + 2;
}

int main()
{
    int a = 5;
    
    printf("The value of a before call by reference is %d", Value(a));  // call by value 

    changeValue(&a); // call by reference
    printf("\nThe value of a after call by reference is %d", a);  

    return 0;
}
