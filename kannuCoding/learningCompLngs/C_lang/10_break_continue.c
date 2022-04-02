// break statement is used to end a loop or switch statement
// continue statement leads to next iteration(repetation), skipping left code

#include<stdio.h>

int main()
{
    int age, i;

    

    for (i = 0; i < 10; i++)
    {
        printf("\nEnter age\n");
        scanf("%d", &age);

        if (age > 50 && age < 150)
        {
            printf("\nYou have crossed 50\n");
            break;
        }

        else if (age > 10)
        {
            printf("\nYou can keep on...\n");
            continue;
        }

        else if (age > 0)
        {
        printf("\nYour are a small child right now!\n");
        break;
        }

        else
        {
            printf("\nPlease check your input!\n");
        }
        
    }

    printf("\n***Thanks for giving your time***");
}





