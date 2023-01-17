#include <stdio.h>

int main(void){
    int binary[30];
    int n, x, flag;
    scanf("%d", &n);
    int idx = 1;
    int ans[4];
    int pref[11] = {1,2,4,6,9,12,15,18,22,26,30};
    int id;
    int len;
    for(int i = 1; i <= 10; i++){
        flag = i;
        id = 0;
        len = 0;
        while(flag != 0){
            x = flag % 2;
            ans[id] = x;
            id += 1;
            flag /= 2;
            len += 1;
        }
        for(int j = len - 1; j >= 0; j--){
            binary[idx] = ans[j];
            idx += 1;
        }
    }
    for(int k = 0; k < pref[n]; k++){
        printf("%d", (char)binary[k]);
    }
    return 0;
}