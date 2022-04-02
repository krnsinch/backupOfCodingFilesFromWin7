#include<stdio.h>

int main()
{   
    // making a calculator for adding two integers
    int a, b;

    printf("\n***Calculator for adding two integers***\n\n");

    printf("Enter value of a: "); 
    scanf("%d", &a);

    printf("Enter value of b: "); 
    scanf("%d", &b);
    
    printf("Sum of %d and %d is %d\n\n", a, b, a + b);

    return 0;
}

