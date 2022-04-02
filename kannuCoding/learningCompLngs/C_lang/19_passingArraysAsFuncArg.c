#include <stdio.h>

// functions declaration
int avg(int array[2], int noOfTerms);
void makeZero_byPointer(int *ptr, int noOfTerms);

int main()
{
    int arr[] = {1, 2, 3, 6};
    printf("Average is %d", avg(arr, 4));  // passing array to array parameter

    int arr2[] = {1, 2, 3, 6, 4, 9};
    makeZero_byPointer(arr2, 4);  // by passing array to pointer parameter

    printf("\nChanged array is");  

    int arr2_size = sizeof(arr2)/sizeof(int);
    for (int i = 0; i < arr2_size; i++)
    {
        if (i == (arr2_size - 1))
        {
            printf(" %d", arr2[i]);
        }
        else
        {
            printf(" %d,", arr2[i]);
        }
    }

    return 0;
}

// array as parameter
int avg(int array[2], int noOfTerms)
{
    int sum = 0;
    
    for (int i = 0; i < noOfTerms; i++)
    {
        sum = sum + array[i];
    }

    return sum / noOfTerms;
}

// pointer as parameter
void makeZero_byPointer(int *ptr, int noOfTerms)
{
    for (int i = 0; i < noOfTerms; i++)     
    {
        *(ptr + i) = 0;
        // or 
        // ptr[i] = 0;
    }
    
}


