#include <stdio.h>

int main(void){
        int arr[3], n, cnt[10];
        for(int k = 0; k < 3; k++){
                scanf("%d", &n);
                arr[k] = n;
        }
        int a = arr[0];
        int b = arr[1];
        int c = arr[2];
        int total = (a*b*c);
        for(int j = 0; j < 10; j++){
                cnt[j] = 0;
        }
        int s_0 = 0, s_1 = 0, s_2 = 0, s_3 = 0, s_4 = 0, s_5 = 0, s_6 = 0, s_7 = 0, s_8 = 0, s_9 = 0;
        while(total != 0){
                if((total % 10) == 0){
                        s_0 += 1;
                        cnt[0] = s_0;
                        total /= 10;
                }
                else if((total % 10) == 1){
                        s_1 += 1;
                        cnt[1] = s_1;
                        total /= 10;
                }
                else if((total % 10) == 2){
                        s_2 += 1;
                        cnt[2] = s_2;
                        total /= 10;
                }
                else if((total % 10) == 3){
                        s_3 += 1;
                        cnt[3] = s_3;
                        total /= 10;
                }
                else if((total % 10) == 4){
                        s_4 += 1;
                        cnt[4] = s_4;
                        total /= 10;
                }
                else if((total % 10) == 5){
                        s_5 += 1;
                        cnt[5] = s_5;
                        total /= 10;
                }
                else if((total % 10) == 6){
                        s_6 += 1;
                        cnt[6] = s_6;
                        total /= 10;
                }
                else if((total % 10) == 7){
                        s_7 += 1;
                        cnt[7] = s_7;
                        total /= 10;
                }
                else if((total % 10) == 8){
                        s_8 += 1;
                        cnt[8] = s_8;
                        total /= 10;
                }
                else if((total % 10) == 9){
                        s_9 += 1;
                        cnt[9] = s_9;
                        total /= 10;
                }
        }
        for(int p = 0; p < 10; p++){
                printf("%d\n", cnt[p]);
        }
        return 0;
}
                                                                                                                                         