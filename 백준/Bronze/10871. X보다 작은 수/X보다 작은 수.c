#include <stdio.h>

int main(void){
        int N, X, k, j;
        scanf("%d %d", &N, &X);
        for(int k = 1; k <= N; k++){
                scanf("%d", &j);
                if(j<X){
                        printf("%d\n", j);
                }
                else
                        continue;
        }
        return 0;
}