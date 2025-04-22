#include <stdio.h>

int main()
{

    /*
        Uma loja oferece para os seus clientes, um determinado desconto de acordo com o valor da compra efetuada.
        O desconto é de:
        10% se o valor da compra for até 200.00€.
        15% se for maior que  200€ e menor ou igual a 500,00€.
        20% se for acima de 500,00€.

        Crie um algoritmo que leia o nome do cliente e o valor da compra. Mostre ao final o nome do cliente,
        o valor da compra, o percentual de desconto e o seu valor e valor total a pagar deste cliente. (só fazer duas Contas)
    */
    char nome[50];
    float valorCompra, valorCompra_desconto, percentual;

    printf("Insira o seu nome: ");
    scanf("%[^\n]", nome);
    printf("Insira o valor da compra (float): ");
    scanf("%f", &valorCompra);

    if (valorCompra > 200)
    {
        percentual = 0.1;
    }
    else if (valorCompra > 200 && valorCompra < 500)
    {
        percentual = 0.15;
    }
    else if (valorCompra > 500)
    {
        percentual = 0.2;
    }

    valorCompra_desconto = valorCompra - (valorCompra * percentual);

    printf("Nome: %s\n\n", nome);
    printf("Valor da compra orginalmente: %.2f\n", valorCompra);
    printf("Percentual: %.2f \n", percentual, (valorCompra * percentual));
    printf("Valor da compra com desconto: %.2f\n", valorCompra_desconto);
}
