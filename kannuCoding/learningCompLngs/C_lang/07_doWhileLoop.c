// Loops are used to repetively execute a particular block of code
// or instruction

// do-while loop is a exit-controlled loop means that the block of
// code is executed first and then condition is checked

// until the condition returns true (1) then further loops or if returns false (0)
// then jumps out of the do-while loop

#include <stdio.h>

int main()
{
    int n = 0, user_num;

    printf("Enter range\n");
    scanf("%d", &user_num);

    printf("Series-\n");

    do
    {
        printf("%d\n", n);
        n += 1;

    } while (n <= user_num);
}

