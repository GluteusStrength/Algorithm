#include <stdio.h>

int main(void){
        int y;
        scanf("%d", &y);
        if(y%4==0 && y%100!=0){
                printf("%d\n", 1);
        }
        else if(y%400 == 0 && y%100 != 0){
                printf("%d\n", 1);
        }
        else if(y%400 == 0){
                printf("%d\n", 1);
        }
        else
                printf("%d\n", 0);
        return 0;
}