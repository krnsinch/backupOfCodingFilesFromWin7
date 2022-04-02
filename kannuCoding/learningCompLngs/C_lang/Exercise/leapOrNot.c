#include <stdio.h>
char isleap_year(int year);

int main()
{
    int year;
    printf("enter an year to check if it is leap year or not\n");
    scanf("%d", &year);

    if (isleap_year(year) == '1')
    {
        printf("yes! %d is a leap year", year);
    }
    else if (isleap_year(year) == '0')
    {
        printf("no! %d is not a leap year", year);
    }

    char ask = '1';
    while (ask != '0')
    {
        printf("\n\nenter '0' to exit...");
        scanf(" %c", &ask);
    }

    return 0;
}

char isleap_year(int year)
{
    if (year % 4 == 0)
    {
        return '1';
    }
    else
    {
        return '0';
    }
}
