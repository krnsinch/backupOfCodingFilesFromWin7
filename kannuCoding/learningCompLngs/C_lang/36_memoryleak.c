#include <stdio.h>
#include <stdlib.h>

// when a dynamically allocated memory cann't be accessed and freed 
// by the progam or any other program, then it is memory leak

int main()
{
    int i = 0;
    int *n;

    while (i < 35000)
    {
        printf("Hello i am trying to leak memory %d\n", i);
        n = (int *)malloc(sizeof(int) * 34000);

        if (i % 100 == 0)
        {
            getchar();
        }

        i++;
    }
}
