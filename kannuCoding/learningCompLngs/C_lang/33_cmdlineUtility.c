#include <stdio.h>

int main(int argc, char const *argv[])
{
    if (argc > 1)
    {
        for (int i = 0; i < argc; i++)
        {
            printf("arg%d is %s\n", i + 1, argv[i]);
        }
                
    }
    return 0;
}
