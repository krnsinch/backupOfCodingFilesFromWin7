#include <stdio.h>

int main()
{
    // Void pointer is a pointer that has no data type associated with it
    // can be type casted to any pointer type
    // it is a general purpose pointer
    int a = 25;
    char b = 'c';

    void *ptr; // void pointer ptr
    ptr = &a;
    printf("address of int a stored in void ptr is %d\n", ptr);

    ptr = &b;
    printf("address of char b stored in void ptr is %d\n", ptr);

    // C does not allow void pointers to be dereferenced
    // printf("%d", *ptr);  // throws compile time error

    // to dereference, typecast it
    printf("\nvalue stored at c is %c\n", *((char *)ptr));

    // cannot use pointer arithmetic with void pointers
    // some compilers allow but we should not do that to make progam more error free
    printf("\naddress stored at ptr is %d\n", ptr);
    printf("address stored at ptr + 1 is %d\n", ptr + 1);

    return 0;
}
