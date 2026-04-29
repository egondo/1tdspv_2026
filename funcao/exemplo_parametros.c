#include<stdio.h>

int soma(int* a, int* b) {
    int res;
    res = *a + *b;
    (*a)++;
    (*b)++;
    return res;
}

int soma_valor(int a, int b) {
    int res = a + b;
    a++;
    b++;
    return res;
}

int main() {
    int x = 5;
    int y = 7;
    int resposta;

    resposta = soma_valor(x, y);
    printf("A soma_valor vale %d\n", resposta);
    printf("x=%d, y=%d\n", x, y);

    resposta = soma(&x, &y);
    printf("A soma vale %d\n", resposta);
    printf("x=%d, y=%d", x, y);
}