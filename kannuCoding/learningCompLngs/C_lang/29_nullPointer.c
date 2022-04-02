#include <stdio.h>

int main(){
    // A NULL pointer is a pointer that does not point to any memory location.
    // It generally points to NULL or 0th memory location, so in simple words,
    // no memory is allocated to a NULL pointer.
    
    int *ptr = NULL;
    // should not dereference null pointer
    printf("The data store at address stored at ptr is %d\n", *ptr);  // program crashes due to dereferencing null pointer
        
    // can be used for error handling
    // like
    if (ptr != NULL){
        printf("The data store at address stored at ptr is %d\n", *ptr);
    }
    else{
        printf("ptr is assigned to NULL\n");
    }

    return 0;
}
