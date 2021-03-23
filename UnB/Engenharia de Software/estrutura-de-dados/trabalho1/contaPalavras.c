#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int contaPalavras(FILE *arquivo) {
    char c;
    int palavras = 1;
    
    while(c != EOF) { // c = O(n)
        c = fgetc(arquivo);
        if(c == '\n') {
            palavras++;
        }
    }
    return palavras;
}