#include <stdio.h>

float tax(float income);
float percent(float n, float total);

int main()
{
    float income, incometax;

    printf("***INCOME TAX SERVICES***\n");
    printf("enter your income\nemployee income: ");
    scanf("%f", &income);

    incometax = tax(income);

    if (incometax == 0)
    {
        printf("No tax on employees whose income is less than 2.5 lakh");
    }
    else
    {
        printf("Income tax paid by you is %f", incometax);
    }

    // asking for exit...
    char ask = '1';
    while (ask != '0'){
        printf("\n\nenter '0' to exit...");
        scanf(" %c", &ask);
    }
    return 0;
}

float percent(float pt, float total)
{
    float ptg = (pt / (float)100) * total;
    return ptg;
}

float tax(float income)
{
    float taxPaid;

    if (income > 1000000.0)
    {
        taxPaid = percent(30, income);
        return taxPaid;
    }
    else if (income >= 500000.0 || income == 1000000.0)
    {
        taxPaid = percent(20, income);
        return taxPaid;
    }
    else if (income >= 250000.0)
    {
        taxPaid = percent(5, income);
        return taxPaid;
    }
    else if (income < 250000.0)
    {
        taxPaid = 0;
        return taxPaid;
    }
}
