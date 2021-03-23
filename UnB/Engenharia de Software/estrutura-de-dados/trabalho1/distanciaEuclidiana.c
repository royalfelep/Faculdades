#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

double distanciaEuclidiana(int *contA, int *contB, int num){

    double distancia = 0;
        for(int x = 0; x < num; x++){ // num = O(n)
            distancia += pow(contA[x] - contB[x], 2);
        };
    return distancia = sqrt(distancia);
    
}