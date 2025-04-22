#include <stdio.h>

int main()
{

    /*
        O sistema de avaliação de determinada disciplina, é composto por três provas Nota (0 a 10).
        A primeira prova tem peso 2, a Segunda tem peso 3 e a terceira prova tem peso 5.
        Faça um algoritmo para calcular a média final de um aluno desta disciplina e se a media for maior ou igual a 6, mostrar APROVADO, senão, mostrar REPROVADO.
    */
    float nota1, nota2, nota3, media;
    int peso1 = 2, peso2 = 3, peso3 = 5;
    int somaPesos = peso1 + peso2 + peso3;

    printf("Insira a primeira nota (0 a 10): ");
    scanf("%f", &nota1);
    printf("Insira a segunda nota (0 a 10): ");
    scanf("%f", &nota2);
    printf("Insira a terceira nota (0 a 10): ");
    scanf("%f", &nota3);

    media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / somaPesos;

    printf("Media final: %.2f\n", media);

    if (media >= 6)
    {
        printf("APROVADO\n");
    }
    else
    {
        printf("REPROVADO\n");
    }

    return 0;
}