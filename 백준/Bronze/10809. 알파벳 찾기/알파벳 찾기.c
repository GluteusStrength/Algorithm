#include <stdio.h>
#include <string.h>

int main(void){
        char s[101];
        int cnt[26];
        int alp[26];
        for(int z = 0; z < 26; z++){
                int j = 'a';
                alp[z] = j;
                z++;
        }
        scanf("%s", s);
        for(int i = 0; i < 26; i++){
                cnt[i] = -1;
        }
        for(int k = 0; k < strlen(s); k++){
                        int x = s[k];
                        int ind = x-97;
                        if(cnt[ind] == -1){
                                cnt[ind] = k;
                        }
        }
        for(int o = 0; o < 26; o++){
                printf("%d ", cnt[o]);
        }
        return 0;
}