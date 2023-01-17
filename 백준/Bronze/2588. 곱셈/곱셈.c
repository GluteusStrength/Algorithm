#include <stdio.h>

int main(void){
    int a, b, i, j, k, l;
    
    scanf("%d%d", &a, &b);
    i = (((b % 100) % 10) * a);
    j = (((b % 100) / 10) * a);
    k = ((b / 100) * a);
    l = i + (j * 10) + (k *100);
    printf("%d\n%d\n%d\n%d\n", i, j, k, l);
    return 0;
}