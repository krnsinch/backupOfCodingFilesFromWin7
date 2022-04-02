/*
The for loop in C language is used to iterate(repeat) the statements
or a part of the program several times
It is used to traverse the data structures like arrays and linked lists

Syntax:
for(Expression 1; Expression 2; Expression 3){  
//code to be executed  
}  

-----------------------------
Expression 1:
- initialization of the loop variable. 

- We can initialize more than one variable in Expression 1.

- Expression 1 is optional.

-----------------------------
Expression 2:
- Expression 2 is a conditional expression. It checks for a specific condition to be satisfied.
  If it is not, the loop is terminated.

- Expression 2 can have more than one condition. However, the loop will iterate until the last
  condition becomes false. Other conditions will be treated as statements.

- Expression 2 is optional.

- Expression 2 can perform the task of expression 1 and expression 3. That is, we can initialize
  the variable as well as update the loop variable in expression 2 itself.

- We can pass zero or non-zero value in expression 2. However, in C, any non-zero value is true,
  and zero is false by default.

-----------------------------
Expression 3:
- Expression 3 is used to update the loop variable.

- We can update more than one variable at the same time.

- Expression 3 is optional.
-----------------------------

*/

#include<stdio.h>

int main()
{
    int n = 0, j;

    for(j = 1;           //  initializing (optional)
        printf("this"), j < 3, n < 5;    //  other statements will be executed, but only last condition can run or stop the loop (optional)
        n += 1)          //  incrementing variable (optional)           
    {
        printf("%d %d\n", n, j);
    }
}
