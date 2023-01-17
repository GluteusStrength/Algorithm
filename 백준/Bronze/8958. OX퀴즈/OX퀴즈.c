#include <stdio.h>
#include <string.h>

int main(void){
        int n;
        scanf("%d", &n);
        int a[81];
        int z = 0;
        char s[81];
        for(int x = 0; x < n; x++){
                scanf("%s", s);
                int sum = 0;
                int cnt = 0;
                for(int i = 0; i < strlen(s); i++){
                        if(s[i] == 79){
                                a[i] = 1;
                        }
                        else
                                a[i] = 0;
                }
                for(int j = 0; j < strlen(s) - 1; j++){
                        if(s[j] == s[j+1] && s[j] == 79 && s[j+1] == 79){
                                        a[j+1] += a[j];
                        }
                }
                for(int k = 0; k < strlen(s); k++){
                        sum += a[k];
                }
                printf("%d\n", sum);

        }
        return 0;

}