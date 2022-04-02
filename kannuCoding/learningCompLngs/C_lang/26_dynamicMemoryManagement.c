#include <stdio.h>
#include <stdlib.h>

// static and dynamic memory both are allocated at the runtime
// static memory - size is fixed
// dynamic memory - size can be changed at runtime

// Dynamic Memory Allocation is a way in which size of a data structure can be changed during runtime

// 4 functions used in dynamic memory allocation defined in stdlib.h
// Function	        Description
// malloc	        allocates the specified number of bytes
// realloc	        increases or decreases the size of the specified block of memory, moving it if necessary
// calloc	        allocates the specified number of bytes and initializes them to zero
// free	            releases the specified block of memory back to the system

int main()
{
    int n, szOf_arr, *ptr_to_int;
    char *ptr_to_char;

    // using malloc
    printf("What should be size of int array: ");
    scanf("%d", &n);

    szOf_arr = n * sizeof(int);
    ptr_to_int = (int *)malloc(szOf_arr);

    for (int i = 0; i < n; i++)
    {
        printf("Enter value at position %d\n", i);
        scanf("%d", &ptr_to_int[i]);
    }
    for (int i = 0; i < n; i++)
    {
        printf("Value at position %d of array is %d\n", i, ptr_to_int[i]);
    }
    free(ptr_to_int);

    printf("\n-------------------------\n\n");

    // using calloc
    printf("What should be size of char array: ");
    scanf("%d", &n);

    szOf_arr = n * sizeof(int);
    ptr_to_char = (char *)calloc(n, sizeof(char));

    for (int i = 0; i < n; i++)
    {
        printf("Enter value at position %d\n", i);
        scanf(" %c", &ptr_to_char[i]);
    }
    for (int i = 0; i < n; i++)
    {
        printf("Value at position %d of char array is %c\n", i, ptr_to_char[i]);
    }

    // using realloc
    printf("\nWhat should be size of new char array: ");
    scanf("%d", &n);

    szOf_arr = n * sizeof(char);
    ptr_to_char = (char *)realloc(ptr_to_char, szOf_arr);

    for (int i = 0; i < n; i++)
    {
        printf("Enter value at position %d\n", i);
        scanf(" %c", &ptr_to_char[i]);
    }
    for (int i = 0; i < n; i++)
    {
        printf("Value at position %d of char array is %c\n", i, ptr_to_char[i]);
    }
    free(ptr_to_char);
    
    // asking for exit the program
    char ask;
    while (1)
    {
        printf("\n\nenter 'q' to exit...");
        scanf(" %c", &ask);

        if (ask == 'q')
        {
            break;
        }
    }

    return 0;
}
