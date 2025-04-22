#include <stdio.h>

int main()
{

    /*
        Fazer um algoritmo que leia o saldo inicial de cliente do banco e leia também um cheque que entrou e ANALISE se
        o cheque poderá ser descontado ou não, já que este cliente não possui limite.
        Se o cheque não poderá ser descontado, mostre essa informação, caso contrário, desconte o cheque e informe o saldo.
    */

    int saldo;
    int cheque;
    int verificar;

    printf("Insira o saldo inicial(int): ");
    scanf("%d[\n^]", &saldo);
    printf("Insira o valor do cheque(int): ");
    scanf("%d[\n^]", &cheque);

    verificar = saldo - cheque;

    if (verificar < 0)
    {
        printf("O valor do cheque nao pode ser descontado do saldo inserido!\n");
    }
    else
    {
        printf("Cheque descontado!\n");
        saldo = saldo - cheque;
        printf("Saldo apos desconto: %d\n", saldo);
    }

    return 1;
}
