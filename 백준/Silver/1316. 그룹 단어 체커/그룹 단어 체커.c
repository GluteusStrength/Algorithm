#include <stdio.h>

int main(void){
   int a, b = 0, i, j, k, sum = 0;
   char gr[101];
   
   scanf("%d", &a);
   for (i = 1; i <= a; ++i){
      scanf("%s", gr);
      for (j = 0; j <= 99; ++j){
         if (gr[j] == '\0')
            break;
         if (gr[1] == '\0')
            break;
         for (k = j + 1; k <= 99; ++k){
                if (gr[k] == '\0')
                    break;
            if (gr[j] == gr[k])
               if (gr[k] != gr[k - 1]){
                  b = 1;
                  break;
               }
            }
      }
      if (b == 0)
         sum += 1;
      b = 0;
      gr[0] = '\0';
   }
   printf("%d\n", sum);
   return 0;
}