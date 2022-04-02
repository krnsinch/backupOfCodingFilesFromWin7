#include <stdio.h>

void func(int *x, int *y);

int main()
{
    int a = 4, b = 3;

    printf("Before call by reference-\n\tvalue of a is %d\n\tvalue of b is %d", a, b);
    func(&a, &b);
    printf("\nAfter call by reference-\n\tvalue of a is %d\n\tvalue of b is %d", a, b);

    return 0;    
}

void func(int *x, int *y)
{
    int temp = *x;
    *x = *x + *y;
    *y = temp - *y;
}
