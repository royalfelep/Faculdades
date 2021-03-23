#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

void tabelaDicionario(FILE *dicionario, int *contA, int *contB) {
    char palavraD[20];
    int i = 0;
    int tamanho_palavra;

    fseek(dicionario, 0, SEEK_SET);
    do {
        fscanf(dicionario, "%s", palavraD);
        if(contA[i] != 0 || contB[i] != 0){
        printf("\n%s \t\t\t %d \t\t\t %d", palavraD, contA[i], contB[i]);    
        };
        i++;
    } while(!feof(dicionario)); // dicionario = O(n)
    printf("\n");
}