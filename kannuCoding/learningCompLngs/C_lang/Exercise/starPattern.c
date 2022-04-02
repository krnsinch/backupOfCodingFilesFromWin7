#include <stdio.h>

int main()
{
    int starPatternNo, noOfRows;

    printf("Printing Star-Pattern");

    while (1)
    {
        printf("\n--------------------------\nEnter\tto do\n0\tupside-down star-pattern\n1\tdownside-up star-pattern\n>>");
        scanf("%d", &starPatternNo);

        if (starPatternNo != 0 && starPatternNo != 1)
        {
            printf("Invalid input!");
            continue;
        }

        printf("Enter no. of rows: ");
        scanf("%d", &noOfRows);

        if (starPatternNo == 0)
        {
            for (int i = 0; i < noOfRows; i++)
            {
                for (int j = 0; j <= i; j++)
                {
                    printf("* ");
                }
                printf("\n");
            }
        }

        else if (starPatternNo == 1)
        {
            for (int i = 0; i < noOfRows; i++)
            {
                for (int j = 0; j < noOfRows - i; j++)
                {
                    printf("* ");
                }
                printf("\n");
            }
        }
    }
}
