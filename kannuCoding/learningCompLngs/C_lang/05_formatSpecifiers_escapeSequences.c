/*
Format specifier
- used in the formatted input and output functions, determines the format of the input and output
- Through this, we tell the compiler in what format/type we want to access data from a variable
according to ASCII (American Standard Code for information interchange) table

The commonly used format specifiers in printf() function are:

Format Specifier            Type
%c                  Used to print the character
%d                  Used to print the signed integer
%f                  Used to print the float values
%i                  Used to print the unsigned integer
%l                  Used to long integer
%lf                 Used to print the double integer
%lu                 Used to print the unsigned int or unsigned long integer
%s                  Used to print the String
%u                  Used to print the unsigned integer

*/

#include <stdio.h>

int main()
{
    int h1, h2, p_e1, p_e2;

    h1 = 6;
    h2 = 3;
    p_e1 = 10;
    p_e2 = 5;

    printf("Height (in m)\t\tP.E. (in J)\n%d\t\t\t%d\n%d\t\t\t%d\n", h1, p_e1, h2, p_e2);
}

/*
An escape sequence is a sequence of characters that does not represent itself, 
but is translated into another character or a sequence of characters that may be
difficult or impossible to represent directly.

Escape Sequences in C
Escape Sequence     Description
\t                  Inserts a tab
\b                  Inserts a backspace
\n                  Inserts a newline.
\r                  Inserts a carriage return.
\f                  Inserts a form feed.
\’                  Inserts a single quote character.
\”                  Inserts a double quote character.
\\                  Inserts a backslash character.

*/
