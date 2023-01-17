#include <stdio.h>

int main(void){
    int a, b;
    scanf("%d %d", &a, &b);
    if(a > b){
        printf("%s\n", ">");
    }
    else if(a < b){
        printf("%s\n", "<");
    }
    else{
        printf("==\n");
    }
    return 0;
}