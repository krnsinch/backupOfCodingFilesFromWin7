#include <stdio.h>

int fib_recursive(int n)
{
    if (n == 0)
    {
        return 0;
    }

    else if (n == 1)
    {
        return 1;
    }

    else
    {
        return fib_recursive(n - 2) + fib_recursive(n - 1);
    }
}

int fib_iterative(int n)
{
    int a = 0, b = 1;

    for (int i = 0; i < n; i++)
    {
        b = a + b;
        a = b - a;
    }
    return a;
}

int main()
{
    int userNum;

    printf("Enter position number to get its fibonacci number on that position\n");
    scanf("%d", &userNum);
    printf("\nUsing iterative approach, fibonacci number at position %d is %d\n", userNum, fib_iterative(userNum));
    printf("\nUsing recursive approach, fibonacci number at position %d is %d\n", userNum, fib_recursive(userNum));

    return 0;
}
