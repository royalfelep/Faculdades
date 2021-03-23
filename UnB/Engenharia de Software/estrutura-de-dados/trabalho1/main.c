#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "contaPalavras.c"
#include "calculaBOW.c"
#include "tabelaDicionario.c"
#include "distanciaEuclidiana.c"

int main() {
    char nome_arquivo[30] = "";
    int *contA, *contB;
    FILE *dicionario = NULL;
    FILE *TRA = NULL;
    FILE *bowTRA = NULL;
    FILE *bowTRB = NULL;
    FILE *TRB = NULL;
    char opcao = '0';
    int num;

    while(opcao != 'S') { // opcao = O(n)
        printf("\n################## Trabalho 1 ##################");
        printf("\n");
        printf("\nD - Ler arquivo de dicionario");
        printf("\nA - Ler texto de referencia A (TRA)");
        printf("\nB - Ler texto de referencia B (TRB)");
        printf("\nE - Exibir BOWs de TRA e TRB");
        printf("\nM - Exibir distancia euclidiana");
        printf("\nS - Sair");
        printf("\nOpcao: ");
        scanf("\n%c", &opcao);
        switch(opcao) {

            case 'D':
                printf("Arquivo de dicionario: ");
                scanf("%s", nome_arquivo); // Escaneia nome do arquivo Dicionário
                if(dicionario != NULL) { // Caso o arquivo Dicionário já estiver aberto, fecha e abre outro
                    fclose(dicionario);
                }
                dicionario = fopen(nome_arquivo, "r"); // Lê o arquivo Dicionário de nome igual ao escaneado na linha 31
                if(dicionario == NULL) { // Caso falhe em localizar o arquivo Dicionário, printa o erro e volta a tela inicial.
                    printf("Nao foi possivel abrir o arquivo\n");
                } else {
                    num = contaPalavras(dicionario);
                    printf("\n%s aberto!\n", nome_arquivo);
                    contA = (int*) calloc(num, sizeof(int)); // Alocação do ponteiro A de tamanho igual a quantidade de palavras do arquivo Dicionário
                    contB = (int*) calloc(num, sizeof(int)); // Alocação do ponteiro B de tamanho igual a quantidade de palavras do arquivo Dicionário
                }
                break;

            case 'A':
                printf("Arquivo de referencia A: ");
                scanf("%s", nome_arquivo); // Escaneia nome do texto de referência A (TRA)
                if(TRA != NULL) { // Caso o TRA já esteja aberto, fecha
                    fclose(TRA);
                }
                TRA = fopen(nome_arquivo, "r"); // Abre o TRA de nome igual ao escaneado na linha 48
                if(TRA == NULL) { // Caso não seja possível abrir o arquivo TRA, printa erro
                    printf("Nao foi possivel abrir o arquivo\n");
                } else {
                    printf("\n%s aberto!\n", nome_arquivo);
                    if(dicionario == NULL) {
                        printf("Nao foi possivel abrir o arquivo\n");
                    } else {
                        bowTRA = fopen("bowA.txt", "w");
                        calculaBOW(dicionario, TRA, bowTRA, contA);
                        fclose(bowTRA);
                    }
                }
                break;

                case 'B':
                printf("Arquivo de referencia B: ");
                scanf("%s", nome_arquivo); // Escaneia nome do texto de referência A (TRA)
                if(TRB != NULL) { // Caso o TRA já esteja aberto, fecha
                    fclose(TRB);
                }
                TRB = fopen(nome_arquivo, "r"); // Abre o TRA de nome igual ao escaneado na linha 48
                if(TRB == NULL) { // Caso não seja possível abrir o arquivo TRA, printa erro
                    printf("Nao foi possivel abrir o arquivo\n");
                } else {
                    printf("\n%s aberto!\n", nome_arquivo);
                    if(dicionario == NULL) {
                        printf("Nao foi possivel abrir o arquivo\n");
                    } else {
                        bowTRB = fopen("bowB.txt", "w");
                        calculaBOW(dicionario, TRB, bowTRB, contB);
                        fclose(bowTRB);
                    }
                }
                break;
            
            case 'E':
                if (TRA == NULL || TRB == NULL || dicionario == NULL){
                    printf("Nao foi possivel relizar a operacao\n");
                }
                else{
                    printf("\nPalavras \t\t Texto A(#) \t\t Texto B(#)");
                    tabelaDicionario(dicionario, contA, contB);
                }
            break;

            case 'M':
                if (TRA == NULL || TRB == NULL){
                    printf("Nao foi possivel realizar a operacao\n");
                }
                else{
                    printf("\nDistancia Euclidiana: %.2lf\n", distanciaEuclidiana(contA, contB, num));     
                }
            break;

            case 'S':
                free(contA);
                free(contB);
                break;
        }
    }

    fclose(dicionario);
    fclose(TRA);
    fclose(TRB);
    printf("Programa encerrado\n");

    return 0;
}
