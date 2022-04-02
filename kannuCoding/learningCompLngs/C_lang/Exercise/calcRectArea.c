#include <stdio.h>

int main()
{
    // printf("%d", 'q');
    int length, breath, area;

    printf("Find area of rectangle\t(enter 'q' to quit)");

    while (1)
    {
        printf("\nEnter length: ");
        scanf("%d", &length);
        printf("Enter breath: ");
        scanf("%d", &breath);

        if (length == 113 || breath == 113)
        {
            break;
        }

        area = length * breath;

        if (area == 1 || area == -1)
        {
            printf("Area = %d sq.unit\n", area);
        }

        else
        {
            printf("Area = %d sq.units\n", area);
        }
    }
    return 0;
}