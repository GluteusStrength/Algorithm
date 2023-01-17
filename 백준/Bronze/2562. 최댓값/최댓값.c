#include <stdio.h>

int main(void){
        int n;
        int num_list[9];
        int renew_num_list[9];
        for(int i = 0; i < 9; ++i){
                scanf("%d", &n);
                num_list[i] = n;
                renew_num_list[i] = n;
        }
        for(int j = 0; j < 8; j++){
                if(renew_num_list[j] > renew_num_list[j+1]){
                        int t = renew_num_list[j+1];
                        renew_num_list[j+1] = renew_num_list[j];
                        renew_num_list[j] = t;
                }
        }
        for(int k = 0; k < 9; k++){
                if(num_list[k] == renew_num_list[8]){
                        printf("%d\n%d\n", renew_num_list[8], k+1);
                        break;
                }
        }
        return 0;
}