#include <stdio.h>

int main(void)
{
    int n, a, b, gcd;
    long int ans;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        scanf("%d %d\n", &a, &b);
        gcd = 0;
        for(int j = 1; j <= a && j <= b; j++){
            if(a % j == 0 && b % j == 0){
                gcd = j;
            }
        }
        ans = (a / gcd) * (b / gcd) * gcd;
        printf("%ld\n", ans);
        
    }
    return 0;
}