#include <stdio.h>

int main(void){
        int up, n, cnt = 0;
        scanf("%d", &up);
        int arr[up];
        for(int k = 0; k < up; k++){
                scanf("%d", &n);
                arr[k] = n;
        }
        int max_gap = 0;
        int start = 0;
        for(int i = 0; i <= up - 2; i++){
                        if(arr[i] < arr[i+1]){
                                if (cnt < 1){
                                        start = arr[i];
                                        cnt+=1;
                                        if(i==up-2){
                                                if(max_gap <= arr[i+1] - start){
                                                        max_gap = arr[i+1] - start;
                                                }
                                        }
                                }
                                else if(cnt >= 1){
                                        cnt += 1;
                                        if(i==up-2){
                                                if(max_gap <= arr[i+1] - start){
                                                        max_gap = arr[i+1] - start;
                                                }
                                        }
                                }
                        }
                        else if((arr[i] >= arr[i+1]) && (cnt == 0)){
                                max_gap = max_gap;
                        }
                        else if((arr[i] >= arr[i+1]) && (cnt >= 1)){
                                if(max_gap <= (arr[i] - start)){
                                        max_gap = arr[i] - start;
                                }
                                else
                                        max_gap = max_gap;
                                cnt = 0;
                        }

        }
        printf("%d\n", max_gap);
        return 0;
}