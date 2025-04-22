#include <stdio.h>

int main()
{
    // Desenvolva um programa que assuma uma entrada em Segundos e transforme em Horas, Minutos e Segundos.
    int entrada;

    printf("Insira um valor de segundos: ");
    scanf("%d", &entrada);

    int horas;
    int minutos;
    int segundos;

    horas = entrada / 3600;
    minutos = (entrada % 3600) / 60;
    segundos = entrada % 60;

    printf("\nInserido: %d segundos \n\nTransformado:\n%d hora(s) \n%d minuto(s)\n%d segundo(s)\n", entrada, horas, minutos, segundos);

    return 0;
}
