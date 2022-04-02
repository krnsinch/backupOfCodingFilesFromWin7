#include <stdio.h>
#include <string.h>

// structure is a user defined data type which can include different type of data
// variables in structure are called members

struct Employee 
{
    // int class = 10; // can not initialize during declaration of members
    int salary;        // as when a datatype is declared, no memory is allocated for it.
    int roomNo;        // Memory is allocated only when variables are created/defined.
    char section;
    char name[30];
    char post[30];    
};

struct Employee ram, shyam, rahul, laxman;

int main()
{
    char employeeName[30], employees[10][30];
    int szOfEmployees = sizeof(employees)/sizeof(char);

    // initializing members' values
    ram.salary = 2000;  // we access members of structure using structure member operator (.)
    ram.roomNo = 50;
    ram.section = 'E';
    strcpy(ram.name, "Ram Williams");
    strcpy(ram.post, "Finance Manager");

    // printing details
    printf("Employee name: %s\n", ram.name);
    printf("Room no.: %d\n", ram.roomNo);
    printf("Section: %c\n", ram.section);
    printf("Post: %s\n", ram.post);

}


