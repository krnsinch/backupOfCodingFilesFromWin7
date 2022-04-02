#include <stdio.h>
#include <string.h>

void askexit();

struct Driver_details
{
    char name[30];
    int drivingLisenceNo;
    char route[30];
    int kms;
};

int main()
{
    struct Driver_details drivers[3];
    int szOf_drivers = sizeof(drivers) / sizeof(struct Driver_details);

    puts("___________QUICKER TRAVEL AGENCY___________");
    puts("\nManaging drivers details");

    for (int i = 0; i < szOf_drivers; i++)
    {
        printf("\n[driver %d]\n", i + 1);
        printf("enter name: ");
        scanf(" %s", &drivers[i].name);

        printf("enter driving Lisence no.: ");
        scanf(" %d", &drivers[i].drivingLisenceNo);

        printf("enter route: ");
        scanf(" %s", &drivers[i].route);

        printf("enter travelled distance (in km): ");
        scanf(" %d", &drivers[i].kms);
    }

    askexit();

    return 0;
}

void askexit()
{
    char ask;

    while (1)
    {
        printf("\nEnter q to exit...");
        scanf(" %c", &ask);

        if (ask == 'q')
        {
            return;
        }
    }
}
