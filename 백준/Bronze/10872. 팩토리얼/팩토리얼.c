#include <stdio.h>

int main(void){
        int n, ans = 1;
        scanf("%d", &n);
        while(n>0){
                ans *= n;
                n--;
                }
        printf("%d\n", ans);
        return 0;
}