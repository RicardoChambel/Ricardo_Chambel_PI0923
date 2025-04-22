#include <stdio.h>

int main()
{
    float notas[10];
    float soma, media;
    int alunosMedia = 0;

    for (int i = 0; i < 10; i++)
    {
        printf("Insira a nota do aluno %d (0 a 20): ", i + 1);
        scanf("%f", &notas[i]);

        if (notas[i] < 0 || notas[i] > 20)
        {
            printf("Nota inválida! Digite a nota do aluno %d (0 a 20): ", i + 1);
            scanf("%f", &notas[i]);
        }

        soma += notas[i];
    }

    media = soma / 10;

    for (int i = 0; i < 10; i++)
    {
        if (notas[i] >= media)
        {
            alunosMedia++;
        }
    }

    printf("Media das notas: %.2f\n", media);
    printf("Numero de alunos com nota igual ou acima desta media: %d\n", alunosMedia);

    return 0;
}
