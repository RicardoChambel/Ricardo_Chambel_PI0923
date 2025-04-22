#include <stdio.h>

int main() {
    int num;
    int par[10];
    int impar[10];
    int i_par = 0;
    int i_impar = 0;

    for(int i=0; i!=10; i++){
        printf("Insira um número: ");
        if(scanf("%d", &num)!=1){
            printf("Valor incorreto!\n");
            while(getchar()!='\n');
            continue;
        }

        if(num%2==0){
            par[i_par++]=num;
        }else{
            impar[i_impar++]=num;
        }
    }

    printf("\nPares: ");
    for (int i = 0; i<i_par; i++){
        printf("%d ", par[i]);
    }
    printf("\n");

    printf("Impares: ");
    for(int i=0; i<i_impar; i++){
        printf("%d ", impar[i]);
    }
    printf("\n");

    return 0;
}
