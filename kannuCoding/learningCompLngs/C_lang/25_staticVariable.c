#include <stdio.h>

// static variables are variables which have the property of preserving their value
// and are only intialized using constant literals

int func1()
{
    // int a = 56;  // local variable of func1()
    // printf("The value of a in func1 is %d and address is %d\n", a, &a);
    
    static int s;  // 0 will be stored if not initialized
    printf("The value of static variable s is %d\n", s);
    s++;
    return 0;
}


int main()
{   
    // int a = 23;  // local variable of main()
    func1();
    func1();
    func1();
    func1();
    // printf("The value of a in main func is %d and address is %d\n", a, &a);
    
    return 0;
}


