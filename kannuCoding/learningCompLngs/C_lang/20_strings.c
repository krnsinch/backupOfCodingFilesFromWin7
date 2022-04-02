// string is a one-dimensional null terminated array of characters

#include <stdio.h>

void main()
{   
    // declaring strings
    char name1[] = {'r', 'a', 'm', '\0'};
    // or 
    char name2[] = "laxman";

    // printing strings on the console
    // by printf()
    printf("printing by printf function:\nname1 is %s\nname2 is %s", name1, name2);

    // by puts() - writes a string to stdout with a newline character appended.
    puts("\n\nprinting by puts function:\nname1 is "); 
    puts(name1);
    puts("name2 is "); 
    puts(name2);

    // taking input from the console
    char cityName[5];

    printf("Enter a four or less character city name\n");
    // by scanf()
    // scanf("%s", cityName);
    // by gets() - to get string input from stdin
    gets(cityName);
    printf("Your entered city name is %s", cityName);
}
