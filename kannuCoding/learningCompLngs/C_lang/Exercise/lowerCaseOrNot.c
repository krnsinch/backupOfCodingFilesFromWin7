#include <stdio.h>

int main()
{
    char ch, islower = '0';

    printf("enter a character: ");
    scanf("%c", &ch);

    for (int i = 97; i < 123; i++)
    {
        if (ch == (char)i)
        {
            islower = '1';
        }
    }

    if (islower == '0')
    {
        printf("You have not entered a character in lower case!");
    }

    else if (islower == '1')
    {
        printf("You have entered a character in lower case!");
    }
}
