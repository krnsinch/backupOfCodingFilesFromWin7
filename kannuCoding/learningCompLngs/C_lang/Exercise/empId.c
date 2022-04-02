#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    int idLen, no_of_employees;
    char *id;

    puts("___________ABC Pvt. ltd___________");
    puts("Take employees' id");

    printf("\nHow many employees are there in the company?_");
    scanf("%d", &no_of_employees);

    printf("__________________");

    for (int i = 0; i < no_of_employees; i++)
    {
        printf("\n------------------\n\n");
        printf("Employee %d:\n", i + 1);
        printf("enter length of your id: ");
        scanf("%d", &idLen);

        id = (char *)malloc(idLen * sizeof(char));

        printf("enter Id: ");
        scanf("%s", id);
    
        printf("Your Employee id is %s\n", id);
        
        free(id);
    }

    return 0;
}
