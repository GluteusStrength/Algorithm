#include <stdio.h>

int main(void){
        int n, a, x, y, z;
        scanf("%d", &n);
        int li[n];
        for(int k = 0; k < n; k++){
                scanf("%d", &a);
                li[k] = a;
        }
        x = li[0];
        y = li[0];
        for (int i = 0; i <= n - 1; ++i){
                if(li[i] > x){
                        x = li[i];
                }
                if(li[i] < y){
                        y = li[i];                                                                                                      }                                                                                                               }
        printf("%d %d\n", y, x);
        return 0;
}