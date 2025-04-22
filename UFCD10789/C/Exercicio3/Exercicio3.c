#include <stdio.h>

int main()
{

    /*
        Crie 2 variáveis (num1 e num2) e leia o valor para cada um deles.
        Mostre os valores de forma crescente e decrescente.
    */

    int num1;
    int num2;

    printf("Valor(int) da variavel 'num1': ");
    scanf("%d[\n^]", &num1);

    printf("Valor(int) da variavel 'num2': ");
    scanf("%d[\n^]", &num2);

    if (num1 > num2)
    {
        printf("%d %d", num1, num2);
    }
    else
    {
        printf("%d %d", num2, num1);
    }

    return 1;
}
