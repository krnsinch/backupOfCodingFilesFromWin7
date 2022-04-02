#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char  *argv[])
{
    if (argc > 1)
    {
        char  *operation = argv[1];
        int n1 = atoi(argv[2]), n2 = atoi(argv[3]);

        if (strcmp(operation, "add") == 0)
        {
            printf("%d", n1 + n2);
        }

        else if (strcmp(operation, "sub") == 0)
        {
            printf("%d", n1 - n2);
        }

        else if (strcmp(operation, "mul") == 0)
        {
            printf("%d", n1 * n2);
        }

        else if (strcmp(operation, "div") == 0)
        {
            printf("%d", n1 / n2);
        }
    }

    return 0;
}
