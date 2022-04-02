#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *replace_word(const char *str, const char *oldWord, const char *newWord);

int main()
{
    char billTemplate[200], *genBill;
    FILE *ptr1, *ptr2;

    ptr1 = fopen("billTemplate.txt", "r");
    ptr2 = fopen("genBill", "w");

    fgets(billTemplate, 200, ptr1);
    printf("Bill template:\n%s\n", billTemplate);

    genBill = replace_word(billTemplate, "{{name}}", "karan");
    genBill = replace_word(genBill, "{{item}}", "helicopter");
    genBill = replace_word(genBill, "{{shop}}", "ABC store");

    printf("\nGenerated bill:\n%s\n", genBill);

    fprintf(ptr2, "%s", genBill);
    printf("\nThe generated bill has been written to genBill.txt\n");

    fclose(ptr1);
    fclose(ptr2);

    return 0;
}

char *replace_word(const char *str, const char *oldWord, const char *newWord)
{
    int i, count = 0;
    int oldwordLen = strlen(oldWord);
    int newwordLen = strlen(newWord);
    char *resultString;

    for (i = 0; str[i] != '\0'; i++)
    {
        if (strstr(&str[i], oldWord) == &str[i])
        {
            count++;
            i += oldwordLen - 1;
        }
    }

    resultString = (char *)malloc(i + count * (newwordLen - oldwordLen) + 1);

    i = 0;

    while (*str)
    {
        if (strstr(str, oldWord) == str)
        {
            strcpy(&resultString[i], newWord);
            i += newwordLen;
            str += oldwordLen;
        }
        else
        {
            resultString[i] = *str;
            i += 1;
            str += 1;
        }
    }

    resultString[i] = '\0';
    return resultString;
}
