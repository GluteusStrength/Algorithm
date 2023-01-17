#include <stdio.h>

int main(void){
        int n, k, a, i, j, y;
        scanf("%d", &n);
        int numArr[n];
        int ansArr[n];
        for(int k = 0; k < n; ++k){
                scanf("%d", &a);
                numArr[k] = a;
        }
        for(int i = 0; i < n - 1; i++){
                for (int j = 0; j < n - 1; j++){
                        if(numArr[j] > numArr[j+1]){
                                int z = numArr[j];
                                numArr[j] = numArr[j+1];
                                numArr[j+1] = z;
                        }
                }
        }
        for(int y = 0; y < n; y++){
                printf("%d\n" ,numArr[y]);
        }
        return 0;
}