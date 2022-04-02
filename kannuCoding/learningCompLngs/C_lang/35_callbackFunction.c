#include <stdio.h>

// If a function's reference is passed to another function as an argument to call it,
// is known as a Callback function

void func1()
{
    printf("I am printed by func1 function");
}

void func2(void (*funcPtr) ())
{
    (*funcPtr)();
}

int main()
{
    void (*ptr) () = func1;
    func2(ptr);
    return 0;
}

