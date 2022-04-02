#include <stdio.h>

/*
This is a program which takes input number from user
and print its multiplication table
*/

int main()
{
    int userNum, range;

    // taking input number
    printf("Enter a number to display its multiplication table: ");
    scanf("%d", &userNum);
    printf("Enter range: ");
    scanf("%d", &range);

    // printing multiplication table of given number

    for (int n = 1; n <= range; n++)
    {
        printf("\n%d x %d = %d", userNum, n, userNum * n);
    }
}
