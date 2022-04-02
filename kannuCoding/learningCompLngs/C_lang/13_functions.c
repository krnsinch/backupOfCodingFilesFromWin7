/*
Types of Functions :
Library Functions – pre-defined functions in C Language which are included in C header files.
E.g. printf(), scanf() etc.

User defined Functions – Functions created by programmer to reduce complexity of a program.

Syntax:
return_type function_name (data_type parameter1, data_type parameter2, ...)
{
    // code
}

*/

#include <stdio.h>

int average(int x, int y)
{
    return (x + y) / 2;
}

int main()
{
    int num1, num2;

    printf("\nEnter two numbers to get their average\n");
    printf("1st number\n");
    scanf("%d", &num1);
    printf("2nd number\n");
    scanf("%d", &num2);

    printf("Average: %d", average(num1, num2));
    return 0;
}
