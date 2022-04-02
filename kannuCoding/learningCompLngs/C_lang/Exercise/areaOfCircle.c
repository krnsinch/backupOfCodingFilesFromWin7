#include <stdio.h>
#include <math.h>
#define PI 3.14

float EuclideanDistance(float x1, float y1, float x2, float y2)
{
    double distance = sqrt((double)(((x1-x2) * (x1-x2)) + ((y1-y2) * (y1-y2))));
    return (float) distance;
}

float areaOfCircle(float x1, float y1, float x2, float y2, float (*ptr) (float, float, float, float))
{
    float radius = (*ptr)(x1, y1, x2, y2);
    float area = PI * radius * radius;
    return area;
}


int main()
{
    float x1, y1, x2, y2;
    float (*ptr)(float, float, float, float);

    printf("x1 = ");
    scanf("%f", &x1);
    printf("y1 = ");
    scanf("%f", &y1);
    printf("x2 = ");
    scanf("%f", &x2);
    printf("y2 = ");
    scanf("%f", &y2);

    printf("distance b/w point(%f, %f) and point(%f, %f) is %f unit(s)\n", x1, y1, x2, y2, EuclideanDistance(x1, y1, x2, y2));
    ptr = EuclideanDistance;
    printf("Area of circle with the distance as radius is %f", areaOfCircle(x1, y1, x2, y2, ptr));

    return 0;
}