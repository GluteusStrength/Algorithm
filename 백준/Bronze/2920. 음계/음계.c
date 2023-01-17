#include <stdio.h>

int main(void){
        int n = 8, k, a, r, sum = 0;
        int inp_n[n];
        for(int k = 0; k < n; ++k){
                scanf("%d", &a);
                inp_n[k] = a;
        }
        for(int r = 0; r < n - 1; r++){
                if(inp_n[r] > inp_n[r+1]){
                        sum -= 1;
                }
                else if(inp_n[r] < inp_n[r+1]){
                        sum += 1;
                }
                else
                        sum += 0;
        }
        if(sum == 7){
                printf("%s\n", "ascending");
        }
        else if(sum == -7){
                printf("%s\n", "descending");
        }
        else
                printf("%s\n", "mixed");
        return 0;
}