#include <stdio.h>

int main(void){
        int n;
        double s;
        scanf("%d", &n);
        double max = 0;
        float s_arr[n];
        for(int i = 0; i < n; i++){
                scanf("%lf", &s);
                if(max <= s){
                        max = s;
                }
                s_arr[i] = s;
        }
        for(int j = 0; j < n; j++){
                s_arr[j] = (s_arr[j]/max)*100;
        }
        double new_mean = 0;
        for(int k = 0; k < n; k++){
                new_mean += s_arr[k];
        }
        printf("%lf\n", new_mean/(float)n);
        return 0;
}
