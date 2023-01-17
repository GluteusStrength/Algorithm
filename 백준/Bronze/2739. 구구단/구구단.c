#include <stdio.h>

int main(void){
        int n;
        scanf("%d", &n);
        int k = 9;
        for(int i = 1; i <=9 ; i++){
                printf("%d %c %d %c %d\n",n, '*', i, '=', n*i);
        }
        return 0;
}