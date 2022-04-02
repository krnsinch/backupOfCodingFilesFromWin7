#include <stdio.h>

int main()
{
    int n;

    for (int i = 0; i < 10; i++)
    {
        printf("Hello;\n");

        for (int i2 = 0; i2 < 5; i2++)
        {
            printf("Enter a number (enter 0 to exit)");
            scanf("%d", &n);

            if (n == 0)
            {
                goto end;   /*  A goto statement provides an unconditional jump from the
                                goto statement to a labeled statement in the same function.   */
            }
        }
    }

end: // end is this label's name, you can give any name
    printf("Ok, we are quiting...");
}
