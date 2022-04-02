#include <stdio.h>
#include <stdlib.h>

int main()
{
    // printf(" __\t__\n|\t  |\n|\t  |\n|__\t__|\n");
    int mtx1_m, mtx1_n, mtx2_m, mtx2_n, pdt_mtx_m, pdt_mtx_n,
        szof_mtx1, szof_mtx2, szof_pdt_mtx, *mtx1, *mtx2, *pdt_mtx;

    // dynamically allocating memory for matrix1
    printf("size of first matrix-\n");
    printf("no. of rows: ");
    scanf("%d", &mtx1_m);
    printf("no. of columns: ");
    scanf("%d", &mtx1_n);
    szof_mtx1 = mtx1_m * mtx1_n;
    mtx1 = (int *)malloc(sizeof(int) * szof_mtx1);

    // dynamically allocating memory for matrix2
    mtx2_m = mtx1_n; // rows of matrix2 = columns of matrix1
    printf("\nsize of second matrix-\n");
    printf("no. of rows = no. of columns of first matrix: %d\n", mtx2_m);
    printf("no. of columns: ");
    scanf("%d", &mtx2_n);
    szof_mtx2 = mtx2_m * mtx2_n;
    mtx2 = (int *)malloc(sizeof(int) * szof_mtx2);

    // printf("size of mtx1 is %d\n", szof_mtx1);
    // printf("size of mtx2 is %d\n", szof_mtx2);

    // taking input in mtrx1
    printf("Enter first martix:\n");
    for (int i = 0; i < mtx1_m; i++)
    {
        for (int j = 0; j < mtx1_n; j++)
        {
            scanf("%d", mtx1 + (mtx1_n * i) + j);
        }
    }

    // taking input in mtrix2
    printf("Enter second martix:\n");
    for (int i = 0; i < mtx2_m; i++)
    {
        for (int j = 0; j < mtx2_n; j++)
        {
            scanf("%d", mtx2 + (mtx2_n * i) + j);
        }
    }

    // allocating product matrix
    pdt_mtx_m = mtx1_m;
    pdt_mtx_n = mtx2_n;
    szof_pdt_mtx = pdt_mtx_m * pdt_mtx_n;
    pdt_mtx = (int *)malloc(sizeof(int) * szof_pdt_mtx);

    // nested loops for calculating product matrix
    for (int i = 0, mtx1_el, mtx2_el; i < mtx1_m; i++)  // to switch rows in mtx1
    {
        for (int j = 0, sum = 0; j < mtx2_n; j++)  // to switch columns in mtx2
        {
            for (int k = 0; k < mtx1_n; k++)  // to switch rows of each column in mtx2
            {
                mtx1_el = *(mtx1 + (mtx1_n * i) + k);
                mtx2_el = *(mtx2 + (mtx2_n * k) + i);
                sum += (mtx1_el * mtx2_el);
            }
            *(pdt_mtx + (pdt_mtx_n * i) + j) = sum;
            sum = 0;
        }
    }

    // printing product matrix
    printf(" __\t__");
    for (int i = 0; i < pdt_mtx_m; i++)
    {
        printf("\n|");
        for (int j = 0; j < pdt_mtx_n; j++)
        {
            printf("%d\t", *(pdt_mtx + (pdt_mtx_n * i) + j));
        }
        printf("\b\b\b\b\b\b\b\b\b\b\b\b\b\b|");
    }
    printf("\n|__\t__|");

    // asking for exit
    char ask = '1';
    while (ask != '0')
    {
        printf("\n\nenter '0' to exit...");
        scanf(" %c", &ask);
    }
    return 0;
}
