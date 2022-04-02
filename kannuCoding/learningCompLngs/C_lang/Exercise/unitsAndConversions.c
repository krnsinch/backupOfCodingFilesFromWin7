#include <stdio.h>

/*
kms to miles
inches to feet
cms to inches
pound to kgs
inches to meters
*/

float km_to_miles(float km)
{
    // 1km = 0.621371 miles
    return km * 0.621371;
}

float inch_to_foot(float inch)
{
    // 1inch = 0.0833333 foot
    return inch * 0.0833333;
}

float cm_to_inch(float cm)
{
    // 1cm = 0.393701 inches
    return cm * 0.393701;
}

float pounds_to_kg(float pounds)
{
    // 1 pound = 0.453592 kgs
    return pounds * 0.453592;
}

float inch_to_meters(float inch)
{
    // 1 inch = 0.0254 m
    return inch * 0.0254;
}

int main()
{
    char userChoice;
    float userNum;

    while (1)
    {
        printf("-------------------------------------\
\nConversions-\n\
[1]. kms to miles\n\
[2]. inches to foot\n\
[3]. cms to inches\n\
[4]. pound to kgs\n\
[5]. inches to meters\n\
Enter conversion's index to choose it\n\
enter 'q' to quit\n\
\nWhich conversion?\n");
        
        scanf(" %c", &userChoice);

        if (userChoice == '1')
        {
            // kms to miles
            printf("\nkms to miles\nEnter km: ");
            scanf("%f", &userNum);
            printf("%f km = %f miles\n", userNum, km_to_miles(userNum));
        }

        else if (userChoice == '2')
        {
            // inches to foot
            printf("\ninch to foot\nEnter inch: ");
            scanf("%f", &userNum);
            printf("%f inch = %d ft\n", userNum, inch_to_foot(userNum));
        }

        else if (userChoice == '3')
        {
            // cms to inches
            printf("\ncm to inch\nEnter cm: ");
            scanf("%f", &userNum);
            printf("%f cm = %f inch\n", userNum, cm_to_inch(userNum));
        }

        else if (userChoice == '4')
        {
            // pound to kgs
            printf("\npound to kg\nEnter pound: ");
            scanf("%f", &userNum);
            printf("%f pound = %f kg\n", userNum, pounds_to_kg(userNum));
        }

        else if (userChoice == '5')
        {
            // inches to meters
            printf("\ninch to meter\nEnter inch: ");
            scanf("%f", &userNum);
            printf("%f inch = %f m\n", userNum, inch_to_meters(userNum));
        }

        else if (userChoice == 'q')
        {
            break;
        }

        else
        {
            printf("Invalid input!\n");
        }
    }

    return 0;
}

