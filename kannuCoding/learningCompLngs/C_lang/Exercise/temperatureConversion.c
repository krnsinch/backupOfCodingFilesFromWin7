#include <stdio.h>

int cel_to_fah(int celcius);
int fah_to_cel(int fahrenheit);

int main()
{
    char user_choose;
    int temperature;

    printf("________Temperature Conversion________\n");

    while (1)
    {
        printf("\n\n[1]. Celcius To Fahrenheit\n[2]. Fahrenheit to Celcius\n");
        scanf(" %c", &user_choose);

        if (user_choose == '1')
        {
            printf("\nCelcius: ");
            scanf("%d", &temperature);
            getchar();
            printf("fahrenheit of %d%cC = %d%cF\n", temperature, 248, cel_to_fah(temperature), 248);
        }
        else if (user_choose == '2')
        {
            printf("\nFahrenheit: ");
            scanf("%d", &temperature);
            getchar();
            printf("celcius of %d%c = %d%cC\n", temperature, 248, fah_to_cel(temperature), 248);
        }
        else if (user_choose == 'q')
        {
            break;
        }
        else
        {
            printf("choose and enter from opt 1, opt 2 or q to quit\n");
        }
    }

    return 0;
}

// formula: (0°C × 9/5) + 32 = 32°F

int cel_to_fah(int celcius)
{
    int fahrenheit = (celcius * 9 / 5) + 32;
    return fahrenheit;
}

int fah_to_cel(int fahrenheit)
{
    int celcius = (fahrenheit - 32) * (5 / 9);
    return celcius;
}
