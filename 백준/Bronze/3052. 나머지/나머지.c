#include <stdio.h>

int main(void){
        int n = 10, k;
        int r[10];
        int cnt = 0;
        for(int i = 0; i < 10; i++){
                scanf("%d", &k);
                r[i] = (k % 42);
        }
        for(int y = 0; y < n -1; y++){
                for(int j = 0; j < n - 1; j++){
                        if(r[j] > r[j+1]){                                                                                                              int t = r[j+1];
                                r[j+1] = r[j];
                                r[j] = t;
                        }
                }
        }
        for(int x = 0 ; x < n - 1 ; x++){
                if(r[x] != r[x+1]){
                        cnt += 1;
                }
        }
        printf("%d\n", cnt+1);
        return 0;
}