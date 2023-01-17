int main(void){
        int n , j;
        double x;
        double sum, score;
        scanf("%d", &n);
        float arr[1002];
        double pt;
        for(int k = 0; k < n; k++){
                scanf("%d", &j);
                sum = 0;
                pt = 0;
                for(int i = 0; i < j; i++){
                        scanf("%lf", &x);
                        sum+=x;
                        arr[i] = x;
                }
                score = sum/j;
                for(int h = 0; h < j; h++){
                        if(arr[h] > score){
                                pt += 1;
                        }
                        else
                                pt += 0;
                }
                printf("%.3lf%c\n", (pt/j)*100,'%');
        }
        return 0;
}