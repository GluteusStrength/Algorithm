#include <stdio.h>

int main(void){
        int n;
        char in;
        scanf("%d", &n);
        int arr[n];
        int sum = 0;
        for(int i = 0; i < n+1; i++){
                scanf("%c", &in);
                arr[i] = in;
        }
        for(int j = 1; j < n+1; j++){
                sum += arr[j] - 48;
        }
        printf("%d\n", sum);
        return 0;
}