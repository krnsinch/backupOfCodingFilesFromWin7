#include <stdio.h>
#include <string.h>

void print_arr(char arr[]);
void html_parser(char *arr);

int main()
{
    char html[100] = "<p>  This is a paragraph   </p>";
    int szOf_html = sizeof(html) / sizeof(char);

    puts("Parsed html is:");
    html_parser(html);
    printf("~~~");
    print_arr(html);
    printf("~~~");

    return 0;
}

void print_arr(char arr[])
{
    for (int i = 0; i < strlen(arr); i++)
    {
        printf("%c", arr[i]);
    }
}

void html_parser(char *arr)
{
    int inTag, index = 0;

    for (int i = 0; i < strlen(arr) + 1; i++)
    {
        if (arr[i] == '<')
        {
            inTag = 1;
            continue;
        }
        else if (arr[i] == '>')
        {
            inTag = 0;
            continue;
        }
        else if (inTag == 0)
        {
            arr[index] = arr[i];
            index++;
        }
    }

    while (arr[0] == ' ')
    {
        for (int i = 0; i < strlen(arr) + 1; i++)
        {
	        arr[i] = arr[i + 1];
        }
    }

    while (arr[strlen(arr) - 1] == ' ')
    {
        arr[strlen(arr) - 1] == '\0';
    }

}
