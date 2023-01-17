#include <stdio.h>

int main(void){
    int arr[3], temp;
    for(int i = 0; i < 3; i++){
        scanf("%d", &arr[i]);
    }
    for(int i = 1; i < 3; i++){
        for(int j = 0; j < i; j++){
            if(arr[j] > arr[i]){
                temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }
        }
    }
    printf("%d\n", arr[1]);
    return 0;
}