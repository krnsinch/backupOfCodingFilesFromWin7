#include <stdio.h>

int main()
{
    int age, marks;

    printf("Enter your age\n");
    scanf("%d", &age);

    switch (age)
    {
    case 20:
        printf("Your age is 20\nEnter your marks\n");
        scanf("%d", &marks);

        switch (marks)
        {
        case 60:
            printf("Your marks are 60\n");
            break;

        case 40:
            printf("Your marks are 40\n");
            break;

        default:
            printf("Invalid marks!\n");
        }
        break;

    case 50:
        printf("Your age is 50\n");
        break;

    default:
        printf("Invalid age!\n");
    }
}
