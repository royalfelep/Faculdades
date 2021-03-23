#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

void retirarPontuacao(char *palavra) {
    char pontuacao[] = {'\n', ' ', '.', ',', ';', ':', '"'};
    int tamanho = strlen(palavra);

    for(int i = 0; i < strlen(palavra); i++) { // strlen(palavra) = O(n)
        if(palavra[tamanho-1] == pontuacao[i]) {
            palavra[tamanho-1] = '\0';
            break;
        }
    }
}