#include <stdio.h>

int main()
{
    char str[20];
    FILE * fp;

    // ***writing to a file***
    fp = fopen("this.txt", "w");
    fprintf(fp, "%s", "this_is_a txt file\n");
    fclose(fp);

    // ***appending to a file***
    fp = fopen("this.txt", "a");
    fprintf(fp, "%s", "\nappended content");
    fclose(fp);

    // ***reading to a file***
    fp = fopen("this.txt", "r");
    fscanf(fp, "%s", str);
    printf("%s", str);
    fclose(fp);

    return 0;
}