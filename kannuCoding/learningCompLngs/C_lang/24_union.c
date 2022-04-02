#include <stdio.h>
#include <string.h>

// union is a user defined data type similar to structure
// difference b/w union and structure is that
// each member of structure has its own memory location
// whereas
// memebers of union uses a single shared memory location

// single shared memory is equal to the size of largest data member

union Employee
{
    char name[30];
    char post[30];
    int salary;
    char section;
};

union Employee mohan; 

int main()
{
    // initializing variables
    strcpy(mohan.name, "Mohan Trump");
    strcpy(mohan.post, "Chief Marketing Officer (C.M.O)");
    mohan.salary = 10000;
    mohan.section = 'B';
    
    // printing values
    printf("Employee name is %s\n", mohan.name);
    printf("Post: %s\n", mohan.post);
    printf("Salary: %d\n", mohan.salary);
    printf("Section: %c\n", mohan.section);
}