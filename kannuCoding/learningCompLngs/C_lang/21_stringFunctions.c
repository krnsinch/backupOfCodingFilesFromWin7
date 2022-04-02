#include <stdio.h>
#include <string.h>

void main()
{
    char s1[] = "rohan", s2[] = " is a good boy";

    // strcat
    puts(strcat(s1, s2));
    puts(s1);

    // strlen
    printf("\nlength of s1 is %d\n", strlen(s1));
    printf("lenght of s2 is %d\n", strlen(s2));

    // strrev
    printf("\nreversed string of \"%s\" is %s", s2, strrev(s2));
    printf("\nreversed string of \"%s\" is\n", s2);

    // strcpy()
    printf("\nvalue of s1 is %s", s1);
    printf("\nNow, value of s1 is %s\n", strcpy(s1, s2));

    // strcmp()
    char s3[] = "abm", s4[] = "bbm";
    printf("\n%d", strcmp(s3, s4));

}

