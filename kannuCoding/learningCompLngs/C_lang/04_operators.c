// Symbols that are used to perform actions or operations on some values or value
// are known as operators
// the values on which operation is performed are known as operands

/*
Arithmetic operators
- used to perform mathematical operations

Operator    Description
+           Addition
−           Subtraction
*           Multiplication
/           Division
%           Modulus


Relational Operators
- used for the comparison between two or more numbers
C has six relational operators and their return value is in Boolean i.e. either True or False (1 or 0)

Note - any nonzero value in c returns true(1) and zero returns false(0)

Operator    Description
>           Greater than
<           Less than
>=          Greater than or equal to
<=          Lesser than or equal to
==          Is equal to
!=          Is not equal to


Logical Operators
There are three logical operators i.e. AND, OR and NOT

AND: returns 1 when both operands are true else 0
OR: returns 1 when either operand is true
Not: it is used to reverse the logical state of the operand.

Symbol      Operator

&&          AND operator

||          OR Operator

!           NOT Operator


Bitwise Operators
To perform bit level operations
They convert the values we provide to them in binary format 
and then compare them to provide us the results.

Symbols     Operators
&           Bitwise AND
|           Bitwise OR
^           Bitwise XOR
~           Bitwise complement
<<          Shift left
>>          Shift right


Assignment Operators
- used to assign values

Operator    Description
=           Assigns values from right side operands to left side operand
+=          It adds the right operand to the left operand and assign the result to the left operand.
-=          It subtracts the right operand from the left operand and assigns the result to the left operand.
*=          It multiplies the right operand with the left operand and assigns the result to the left operand.
/=          It divides the left operand with the right operand and assigns the result to the left operand.

*/

#include<stdio.h>

int main()
{
    int x = 1;
    int y = 0; 

    printf("x + y = %d\n", x + y);  // arithmetic operation
    printf("x > y = %d\n", x > y);  // relation operation
    printf("! y = %d\n", ! y);  //  logical operation
    printf("x | y = %d\n", x | y);  //  bitwise operation
    x += 1;   // assignment operation 

}

