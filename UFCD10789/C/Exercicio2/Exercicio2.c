#include <stdio.h>

int main()
{
    // Fazer um programa que analise 3 valores inteiros (atrav�s das vari�veis num1, num2 e num3),e informa qual o maior e qual o menor deles.
    int num1, num2, num3;

    printf("Primeiro Valor: ");
    scanf("%d[\n^]", &num1);

    printf("Segundo Valor: ");
    scanf("%d[\n^]", &num2);

    printf("Terceiro Valor: ");
    scanf("%d[\n^]", &num3);

    int maior = num1;
    int menor = num1;

    if (num2 > maior)
    {
        maior = num2;
    }
    if (num2 < menor)
    {
        menor = num2;
    }

    if (num3 > maior)
    {
        maior = num3;
    }
    if (num3 < menor)
    {
        menor = num3;
    }

    printf("Maior: %d\n", maior);
    printf("Menor: %d\n", menor);

    return 0;
}
