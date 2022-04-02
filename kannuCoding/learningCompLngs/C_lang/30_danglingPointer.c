#include <stdio.h>
#include <stdlib.h>

int *danglingFunc()
{
    int a = 23;
    return &a;
}

int main()
{
    // Dangling pointer- pointers that are pointing to a memory location that has been freed

    // causes of dangling pointer
    // Case 1: de-allocation of a memory block
    int *danglingPtr1 = (int *)malloc(4 * sizeof(int));
    danglingPtr1[0] = 23;
    danglingPtr1[1] = 34;
    danglingPtr1[2] = 24;
    danglingPtr1[3] = 30;
    free(danglingPtr1); // allocated memory is freed, now danglingPtr1 pointer is a dangling pointer

    // Case 2: function returning local variable address
    int *danglingPtr2 = danglingFunc(); // after returning address of a, danglingFunc's allocated memory
                                        // is freed up, so danglingPtr2 is a dangling pointer

    // Case 3: if a variable goes out of a scope
    int *danglingPtr3;
    // a scope
    {
        int a = 90;
        danglingPtr3 = &a; // address of a stored in danglingPtr3
    }
    // here out of the above scope memory allocated for a is freed
    // now danglingPtr3 is a dangling pointer

    // assign NULL to the pointer, now the pointer is not pointing
    // to the any memory location
    danglingPtr1 = NULL;
    danglingPtr2 = NULL;
    danglingPtr3 = NULL;
    printf("%d", danglingPtr3);
    return 0;
}
