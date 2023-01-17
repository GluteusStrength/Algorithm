#include <stdio.h>
int arr[3];

int main(void){
    int temp;
    for(int i = 0; i < 3; i++){
        scanf("%d", &arr[i]);
    }
    for(int i = 1; i < 3; i++){
        temp = 0;
        for(int j = 0; j < i; j++){
            if(arr[j] > arr[i]){
                temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }
        }
    }
    for(int i = 0; i < 3; i++){
        if(i < 2){
            printf("%d ", arr[i]);
        }
        else{
            printf("%d\n", arr[i]);
        }
    }
    return 0;
}


