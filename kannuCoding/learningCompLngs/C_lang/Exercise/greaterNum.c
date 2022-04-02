#include <stdio.h>

int main()
{
    int num[4], n = num[0];

    for (int i = 0; i < 4; i++)
    {
        printf("enter number: ");
        scanf("%d", num[i]);
    }
    
    
    for (int i = 0; i < 4; i++)
    {
        if (n > num[i + 1])
        {
            continue;
        }
        else
        {
            n = num[i + 1];
        }
    }

    printf("\n%d is greatest number from the entered numbers!", n);

    return 0;
}
