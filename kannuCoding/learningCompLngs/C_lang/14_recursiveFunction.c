/*
Recursive Functions :
Recursive functions or Recursion is a process when a function calls a copy of itself to work on smaller problems.

Recursion is the process in which a function calls itself directly or indirectly.

Any function which calls itself is called recursive function.
Any problem which can be solved recursively can also be solved iteratively. 

Base condition in recursion :
The case at which the function doesn’t recur is called the base case.

Recursive Case :
The instances where the function keeps calling itself to perform a subtask i.e. solving problem 
by dividing it in small parts, is called the recursive case.

*/

#include <stdio.h>

int factorial(int n)
{
    if (n == 1 || n == 0)
    {
        return 1;
    }
    else
    {
        return n * factorial(n - 1);

    }
}

int main()
{
    int userNum; 

    printf("Enter a whole number to get its factorial\n");
    scanf("%d", &userNum);
    printf("Factorial of %d is %d", userNum, factorial(userNum));

    return 0;
}
