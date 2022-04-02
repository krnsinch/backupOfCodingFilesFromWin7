// Conditional statements are used when to perform some operation based on conditions
// when the condition in a conditional statement returns true (1) then the conditional
// statement execute or if returns false (0) then skipped

#include <stdio.h>

int main()
{
    char input, party, exit;
    int userAge;

    printf("\nNamaste! This is online voting platform. Here you can vote for\n");
    printf("your candidate. Vote who you think can rule better the country. \n");
    printf("\n\t\"Vote and encourage others too\"\n\n");
    printf("Press enter to continue...");
    scanf("%c", &input);

    if (input == '\n')
    {
        while (1)
        {
            printf("Enter your age: ");
            scanf("%d", &userAge);

            if (userAge >= 18 && userAge <= 150)
            {
                while (1)
                {
                    printf(
                        "\nVote your party\
\nEnter        Party\
\n'b'    ->    Bhartiya Janta Party (BJP)\
\n'c'    ->    Congress\
\n>>");
                    scanf(" %c", &party);

                    if (party == 'b')
                    {
                        printf("\nVoted to Bhartiya Janta Party (BJP)!\n***Thanks for Voting***\n");
                        break;
                    }

                    else if (party == 'c')
                    {
                        printf("\nVoted to Congress!\n***Thanks for Voting***\n");
                        break;
                    }

                    else
                    {
                        printf("Invalid input! ");
                    }
                }
                break;
            }

            else if (userAge >= 0 && userAge < 18)
            {
                printf("\nSmaller than 18!\nYou cannot vote right now! You should be atleast of 18 or greater age");
                break;
            }

            else
            {
                printf("\nInvalid input!");
            }
        }

        while (1)
        {
            printf("\nEnter 'e' to exit\n");
            scanf(" %c", &exit);

            if (exit == 'e')
            {
                break;
            }
        }
    }
}
