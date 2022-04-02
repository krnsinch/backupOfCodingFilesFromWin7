#include <stdio.h>

int main()
{
    // Uninitialized pointers are known as wild pointers
    char *ptr;  // wild pointer

    // it will store any garbage value (some random location) in it 
    // it can cause a lot of bugs in the program
    // to overcome this, we can assign NULL to it
    
    // cannot dereference a wild pointer as we can not be sure about the data in the memory it is pointing towards.
    // it can cause a lot of bugs and can also crash the program.
    printf("address stored at ptr is %d\n", ptr);  // garbage value
    printf("data stored at address stored at ptr is %d\n", *ptr);  // undifined behaviour

    return 0;
}
