#include <stdio.h>

int main(void){
        int n;
        scanf("%d", &n);
        if(90 <= n && n <=100){
                printf("%c\n", 'A');
        }
        else if(80 <= n && n < 90){
                printf("%c\n", 'B');
        }
        else if(70<=n && n<80){
                printf("%c\n", 'C');
        }
        else if(60 <= n && n < 70){
                printf("%c\n", 'D');
        }
        else
                printf("%c\n", 'F');
        return 0;
}