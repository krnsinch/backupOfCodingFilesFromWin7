#include <stdio.h>

int is_div_by_97(int n);

int main()
{
    int n;
    printf("enter a number to check if it is divisible by 97 or not\n");
    scanf("%d", &n);
    
    if (is_div_by_97(n))
    {
        printf("Yes! %d is divisible by 97", n);
    }
    else
    {
        printf("No! %d is not divisible by 97", n);
    }

    char ask = '1';
    while (ask != '0')
    {
        printf("\n\nenter '0' to exit...");
        scanf(" %c", &ask);
    }

    return 0;
}

int is_div_by_97(int n)
{
    int remainder = n % 97;

    if (remainder == 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
