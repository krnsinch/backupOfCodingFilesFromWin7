#include <stdio.h>

int main()
{
    long int mantissa, exponent, value;
    
    printf("enter mantissa: ");
    scanf("%ld", &mantissa);

    printf("enter exponent: ");
    scanf(" %ld", &exponent);

    value = mantissa;

    for (long int i = 0; i < (exponent - 1); i++)
    {
        value = value * mantissa;
    }

    printf("Value of %ld ^ %ld is %ld", mantissa, exponent, value);

    return 0;
}
