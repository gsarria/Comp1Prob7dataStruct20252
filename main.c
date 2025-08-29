#include <stdio.h>
#include <stdlib.h>
struct alumno 
{ 
    char nombre[64]; 
    float n1, n2, n3; 
};
typedef struct alumno Alumno;
int main(void){
    int n; 
    scanf("%d",&n);
    // TODO: malloc de n Alumno, leer, calcular promedio, encontrar mejor, imprimir "<nombre> <prom>"
    // TODO: free
    return 0;
}
