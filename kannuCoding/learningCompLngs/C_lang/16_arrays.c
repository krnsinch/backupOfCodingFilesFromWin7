/*
Array is a data structure which is a collection of contiguous memory locations of same data type
arrays's name is just a name given to base address of array (first byte address)
*/

#include <stdio.h>

int main()
{
    // one-dimensional array
    int vector[] = {50, 60, 45, 34};  // no need to define size here, compiler will automatically determine

    vector[2] = 12; // changing value at 2 index

    // printf("Printing one dimensional array (size is %d bytes)-", sizeof(vector));
    // for (int i = 0; i < 5; i++)
    // {
    //     printf("\nElement at %d index = %d", i, vector[i]);
    // }

    // // two-dimensional array
    // int matrice[3][5] = {{1, 2, 3, 4, 5}, {11, 22, 33, 44, 55}, {111, 222, 333, 444, 555}};

    // printf("\n\nIndex no.   element of array\n");

    // for (int i = 0; i < 3; i++)
    // {
    //     for (int j = 0; j < 5; j++)
    //     {
    //         printf("(%d, %d)  -->  %d\n", i, j, matrice[i][j]);
    //     }
    //     printf("\n");
    // }

    // // arrays name
    // int arr[7] = {1, 2, 3, 4, 5, 90};
    
    // // when array name arr is operand of the sizeof operator
    // // then arr represents the whole array
    // printf("Size of arr array is %d bytes\n", sizeof(arr)); 
    
    // // arr points to first element of the array
    // printf("first element: address is %d, value is %d\n", arr, *arr); 
    // // is same as
    // printf("first element: address is %d, value is %d\n", &arr[0], arr[0]);
    
    // printf("second element: address is %d, value is %d\n", arr + 1, *(arr + 1));
    // // is same as
    // printf("second element: address is %d, value is %d\n", &arr[1], arr[1]);

    return 0;
}
