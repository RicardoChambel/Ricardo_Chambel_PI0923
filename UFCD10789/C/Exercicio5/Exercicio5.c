#include <stdio.h>

int main()
{

    /*
        Ler 3 valores INTEIROS para as variáveis Num1, Num2, Num3.
        Apresentar os valores dispostos em ordem crescente e decrescente.
        
    */

    int Num1, Num2, Num3;

    printf("Valor para a variavel 'Num1' (int): ");
    scanf("%d", &Num1);
    printf("Valor para a variavel 'Num2' (int): ");
    scanf("%d", &Num2);
    printf("Valor para a variavel 'Num3' (int): ");
    scanf("%d", &Num3);

    printf("Ordem crescente: ");
    if (Num1 <= Num2 && Num1 <= Num3)
    {
        printf("%d ", Num1);
        if (Num2 <= Num3)
        {
            printf("%d %d\n", Num2, Num3);
        }
        else
        {
            printf("%d %d\n", Num3, Num2);
        }
    }
    else if (Num2 <= Num1 && Num2 <= Num3)
    {
        printf("%d ", Num2);
        if (Num1 <= Num3)
        {
            printf("%d %d\n", Num1, Num3);
        }
        else
        {
            printf("%d %d\n", Num3, Num1);
        }
    }
    else
    {
        printf("%d ", Num3);
        if (Num1 <= Num2)
        {
            printf("%d %d\n", Num1, Num2);
        }
        else
        {
            printf("%d %d\n", Num2, Num1);
        }
    }

    printf("Ordem decrescente: ");
    if (Num1 >= Num2 && Num1 >= Num3)
    {
        printf("%d ", Num1);
        if (Num2 >= Num3)
        {
            printf("%d %d\n", Num2, Num3);
        }
        else
        {
            printf("%d %d\n", Num3, Num2);
        }
    }
    else if (Num2 >= Num1 && Num2 >= Num3)
    {
        printf("%d ", Num2);
        if (Num1 >= Num3)
        {
            printf("%d %d\n", Num1, Num3);
        }
        else
        {
            printf("%d %d\n", Num3, Num1);
        }
    }
    else
    {
        printf("%d ", Num3);
        if (Num1 >= Num2)
        {
            printf("%d %d\n", Num1, Num2);
        }
        else
        {
            printf("%d %d\n", Num2, Num1);
        }
    }

    return 0;
}