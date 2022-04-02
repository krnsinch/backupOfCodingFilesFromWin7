#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

int random(int range);
char comp_choose();
int winner(char chs1, char chs2);

int main()
{
    char player_choose, cmp_choose, ask;
    int win, loop, n = 0, p1score = 0, p2score = 0;

    puts("__________STONE PAPER SCISSOR__________");
    puts("enter- 's' for stone");
    puts("       'p' for paper");
    puts("       'c' for scissor");
    puts("       '0' to exit");
    printf("How many time you want to play with computer: ");
    scanf("%d", &loop);

    while (n < loop)
    {
        printf("\nPlayer1 (me): ");
        scanf(" %c", &player_choose);

        if (player_choose == '0')
        {
            break;
        }

        cmp_choose = comp_choose();
        printf("Player2 (comp.): %c", cmp_choose);

        win = winner(player_choose, cmp_choose);
        if (win == 1)
        {
            printf("\nYou got it!\n");
            p1score++;
        }
        else if (win == 0)
        {
            printf("\nComp got it!\n");
            p2score++;
        }
        else if (win == 2)
        {
            printf("\nIts Tie!\n");
        }

        printf("\nYour Score: %d\nComp Score: %d\n", p1score, p2score);
        printf("------------------------\n");
        n++;
    }

    printf("________________________\n");
    printf("Total Score:\nYour: %d\nComp: %d\n", p1score, p2score);
    if (p1score > p2score)
    {
        printf("\n***Finally, you Win!***\n");
    }
    else if (p2score > p1score)
    {
        printf("\n***Finally, comp Win!***\n");
    }
    else if (p1score == p2score)
    {
        printf("\nFinally, its a tie!\n");
    }

    // asking for exit
    while (ask != '0')
    {
        printf("\nenter '0' to exit...");
        scanf(" %c", &ask);
    }

    return 0;
}

int random(int range)
{
    srand(time(NULL));
    int randno = rand() % range;
    return randno;
}

char comp_choose()
{
    int rand = random(3);
    if (rand == 0)
    {
        return 's';
    }
    else if (rand == 1)
    {
        return 'p';
    }
    else if (rand == 2)
    {
        return 'c';
    }
}

int winner(char chs1, char chs2)
{
    if (chs1 == chs2)
    {
        return 2;
    }
    else if (chs1 == 's')
    {
        if (chs2 == 'p')
        {
            return 0;
        }
        else if (chs2 == 'c')
        {
            return 1;
        }
    }
    else if (chs1 == 'p')
    {
        if (chs2 == 's')
        {
            return 1;
        }
        else if (chs2 == 'c')
        {
            return 0;
        }
    }
    else if (chs1 == 'c')
    {
        if (chs2 == 'p')
        {
            return 1;
        }
        else if (chs2 == 's')
        {
            return 0;
        }
    }
}
