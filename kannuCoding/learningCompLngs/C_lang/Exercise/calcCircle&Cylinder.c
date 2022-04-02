#include <stdio.h>

// global variables
double PI = 3.14159;


double area_of_circle(double radius)
{
    double area = 2 * 3.14159 * radius;
    return area;
}


double volume_of_cylinder(double radius, double height)
{
    double volume = (2 * 3.14159 * radius) * height;
    return volume;
}


int main()
{
    double radius, height;
    int choice;

    printf("Find area of circle or volume of cylinder");

    while (1)
    {
        printf("\n-----------------------------------------\nenter 0 for circle\n      1 for cylinder\n");
        scanf("%d", &choice);

        if (choice == 0)
        {
            printf("\nCircle-");
            printf("\nenter radius: ");
            // scanf("%ld", &radius);

            // printf("Area = %ld\n", area_of_circle(radius));
        }

        else if (choice == 1)
        {
            printf("\nCylinder-");
            printf("\nenter radius: ");
            // scanf("%ld", &radius);
            // printf("enter height: ");
            // scanf("%ld", &radius);
            // printf("Volume = %ld\n", volume_of_cylinder(radius, height));
        }

        else if ((char)choice == 'q\n')
        {
            printf("quitting...");
        }
    }
}


