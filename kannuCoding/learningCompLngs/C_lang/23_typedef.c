#include <stdio.h>

int main()
{
    // typedef keyword used to give a alternative name to a data type
    typedef unsigned int ui;
    unsigned int height1 = 23;
    ui height2 = 23; // can also use ui instead unsigned int

    printf("%d\n", height1);
    printf("%d\n", height2);

    ///////////////////////////////////////////////
    int *a, b;  // here, a will be pointer to int variable, but b will be just a int variable
    int c = 40;

    a = &c;
    b = &c;  //  throws warning

    typedef int* intptr; // now intptr is alias of int*
    
    intptr d, e;  // now d and e both will be pointer to int variable
    d = &c;
    e = &c;
    
}

