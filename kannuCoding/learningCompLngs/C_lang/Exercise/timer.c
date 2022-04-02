#include <stdio.h>
#include <unistd.h>

int main()
{
    int h = 0, m = 0, s = 0, s2 = 0;

    while (1)
    {
        printf("%dhr : %dmin : %dsec", h, m, s);
        sleep(1);
        s += 1;
        s2 += 1;

        if (s == 59)
        {
            m += 1;
            s = 0;
        }
        if (s2 == 3600)
        {
            h += 1;
            s2 = 0;
        }
        system("cls");
    }

    return 0;
}