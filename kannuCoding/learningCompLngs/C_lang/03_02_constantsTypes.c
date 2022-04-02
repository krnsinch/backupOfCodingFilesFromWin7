#include <stdio.h>

int main()
{
    // Types of constants (literals)
    
    int mtEverestHeight = 8;  // 8 is int constant
    printf("The height of Mt. Everest is %d km (approx.)", mtEverestHeight);
    
    const float PI = 3.14;  // 3.14 is float constant
    printf("\nThe value of %c is %.2f (approx.)", 227, PI);

    char ch = 'A';  // 'A' is char constant
    printf("\nThe corresponding ascii value of character 'A' in int type is %d", ch);

    return 0;
}

