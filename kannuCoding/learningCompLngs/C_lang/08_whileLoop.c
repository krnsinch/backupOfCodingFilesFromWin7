// while loop is a entry-controlled loop mean that the 
// condition is checked first and then block of code is executed

// until the condition returns true (1) then loops or if returns false (0)
// then jumps out of the while loop

#include<stdio.h>

int main()
{
    int n = 0, userNum;

    printf("Enter range\n");
    scanf("%d", &userNum);
    printf("\nSeries\n");

    while (n <= userNum)
    {
        printf("%d\n", n);
        n += 1;
    }
}



