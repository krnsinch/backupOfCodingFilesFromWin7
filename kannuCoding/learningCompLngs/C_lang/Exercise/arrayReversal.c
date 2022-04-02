#include <stdio.h>

void rv_arr(int *arr, int size_of_arr);
void print_arr(int arr[], int size_of_arr);


int main()
{
    int arr[] = {1, 2, 3, 4, 5, 6, 67}, size_of_arr = sizeof(arr)/sizeof(int);
    
    printf("Array to reverse:\n");
    print_arr(arr, size_of_arr);

    printf("\n\nReversed array:");

    // by reversing (changing) the main array
    // puts("  (by reversing/changing the array arr)");
    // rv_arr(arr, size_of_arr);
    // print_arr(arr, size_of_arr);
    
    // ------------------------------------------------
    // by don't reversing the main array 
    // puts("  (by don't reversing/changing the array arr)");
    // for (int i = (size_of_arr - 1); i >= 0 ; i--)
    // {
    //     printf("%d ", arr[i]);
    // }

}


void rv_arr(int *arr, int size_of_arr)
{
    for (int i = 0, j = (size_of_arr - 1); i < (size_of_arr/2); i++, j--)
    {   
        int temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
    }
}


void print_arr(int arr[], int size_of_arr)
{
    for (int i = 0; i < size_of_arr; i++)
    {
        printf("%d ", arr[i]);
    }
}

