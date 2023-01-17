#include <stdio.h>
#include <string.h>
int main(void){
        int n, k, stl = 0;
        scanf("%d", &n);
        char s[21];
        int cnt = 0;
        for(int i = 0; i < n; i++){
                scanf("%d %s", &k, s);
                stl = strlen(s);
                for(int x = 0; x < stl; x++){
                        for(int j = 0; j < k; j++){
                                printf("%c",s[x]);
                        }
                }
                printf("\n");

        }
        return 0;
} 