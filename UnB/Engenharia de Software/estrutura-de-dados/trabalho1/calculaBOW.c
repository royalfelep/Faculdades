#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "retirarPontuacao.c"

void calculaBOW(FILE *dicionario, FILE *TR, FILE *bowTR, int *cont) {
    char palavraD[40] = "";
    char palavraTR[40] = "";
    int i = 0;
    int tamanho_palavra;

    fseek(dicionario, 0, SEEK_SET);
    fprintf(bowTR, "Ocorrencias:\n");
    do {
        fseek(TR, 0, SEEK_SET);
        fscanf(dicionario, "%s", palavraD);
        while(!feof(TR)) { // TR = O(m)
            fscanf(TR, "%s", palavraTR);
            retirarPontuacao(palavraTR);

            for(int x = 0; x < strlen(palavraD); x++){ // strlen(palavraD) = O(d)
                palavraD[x] = tolower(palavraD[x]);
            }

            for(int x = 0; x < strlen(palavraTR); x++){ // strlen(palavraTR) = O(tr)
                palavraTR[x] = tolower(palavraTR[x]);
            }

            if(strcmp(palavraD, palavraTR) == 0) {
                cont[i]++;    
            };
        }
        fprintf(bowTR,"%s --> %d\n", palavraD, cont[i]);
        i++;
    } while(!feof(dicionario)); // O(n)
}