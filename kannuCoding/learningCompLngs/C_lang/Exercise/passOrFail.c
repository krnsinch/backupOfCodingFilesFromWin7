#include <stdio.h>

int percentage(int n, int total);

int main()
{
    int marks[3], marksScored = 0, totalMarks = 10 * 3, ptg;

    printf("_______GET RESULT_______\n");
    printf("Enter marks of all 3 subjects out of 10--\n\n");

    for (int i = 0; i < 3; i++)
    {
        printf("enter marks of subject %d: ", i + 1);
        scanf("%d", &marks[i]);
        marksScored += marks[i];
    }

    printf("\n_________________________________________________________\n");
    printf("Subjects\t\tMarks scored\t\tOut of\n");
    for (int i = 0; i < 3; i++)
    {
        printf("subject%d\t\t%d\t\t\t%d\n", i + 1, marks[i], 10);
    }

    printf("---------------------------------------------------------\n");
    printf("Total\t\t\t%d\t\t\t%d", marksScored, totalMarks);

    ptg = percentage(marksScored, totalMarks);
    printf("\n\nPercentage = %d%%", ptg);

    if (ptg >= 33)
    {
        printf("\t\t(passed!)");
    }
    else
    {
        printf("\t\t(failed!)");
    }

    char ask = '1';
    while (ask != '0')
    {
        printf("\n\nenter '0' to exit...");
        scanf(" %c", &ask);
    }

    return 0;
}

int percentage(int n, int total)
{
    int percent = (float)n / total * 100;
    return percent;
}
