#include <stdio.h>
#include <string.h>

int hcf(int x, int y);

int main()
{
    int n1, n2;
    puts("Find HCF:");
    printf("enter 1st number: ");
    scanf("%d", n1);
    getchar();
    printf("enter 2nd number: ");
    scanf("%d", n2);
    getchar();
    printf("H.C.F. of %d and %d is %d", n1, n2, hcf(n1, n2));

    return 0;
}

int hcf(int x, int y)
{
    int temp_y, hcf;

    while (1)
    {
        if (x % y == 0)
        {
            hcf = y;
            return hcf;
        }

        else
        {
            temp_y = y;
            y = x % y;
            x = temp_y;
        }
    }
}