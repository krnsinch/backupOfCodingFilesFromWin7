#include <stdio.h>

int main()
{
    char choice;
    const float PI = 3.14;
    long double sqside, rectL, rectB, circleR, cbside,
        sphR, cylH, cylR;

    while (1)
    {
        printf("\n------------------\nChoose what to do-\n");
        printf("Area (a)\n");
        printf("Volume (v)\n");
        scanf(" %c", &choice);

        if (choice == 'a')
        {
            printf("\nChoose shape\n");
            printf("#2d Shapes-\n[1]. Square\
\n[2]. Rectangle\n[3]. Circle\n");

            printf("\n#3d Shapes-\n[4]. Cube\
\n[5]. Sphere\n[6]. Cylinder\n");

            scanf(" %c", &choice);

            if (choice == '1')
            {
                printf("\n>Square: Enter side- ");
                scanf(" %ld", &sqside);
                printf("Area: %ld", sqside * sqside);
            }

            else if (choice == '2')
            {
                printf("\n>Rectangle: Enter length- ");
                scanf(" %ld", &rectL);
                printf("           Enter breath- ");
                scanf(" %ld", &rectB);
                printf("Area: %ld", rectL * rectB);
            }

            else if (choice == '3')
            {
                printf("\n>Circle: Enter radius- ");
                scanf(" %ld", &circleR);
                printf("\nArea: %ld", PI * circleR * circleR);
            }

            else if (choice == '4')
            {
                printf("\n>Cube: Enter side- ");
                scanf(" %ld", &cbside);
                printf("\nArea: %ld", 6 * (cbside * cbside));
            }

            else if (choice == '5')
            {
                printf("\n>Sphere: Enter radius- ");
                scanf(" %ld", &sphR);
                printf("\nArea: %ld", 4 * PI * (sphR * sphR));
            }

            else if (choice == '6')
            {
                printf("\n>Cylinder: Enter radius- ");
                scanf(" %ld", &cylR);
                printf("\n           Enter height- ");
                scanf(" %ld", &cylH);
                printf("\nArea: %ld", (2 * PI * (cylR * cylR)) * cylH);
            }

            else if (choice == 'q')
            {
                break;
            }

            else
            {
                printf("\nInvalid!");
            }
        }

        else if (choice == 'b')
        {
        }
    }
    return 0;
}
