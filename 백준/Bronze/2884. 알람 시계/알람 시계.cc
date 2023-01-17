#include <stdio.h>

int main(void){
        int h, m;
        scanf("%d %d", &h, &m);
        if(h>0){
        if(m<45){
                h-=1;
                m+=60;
                m-=45;
                printf("%d %d",h,m);
        }
        else
                printf("%d %d\n",h,m-45);
        }
        else if(h==0){
                if(m<45){
                        h=23;
                        m+=60;
                        m-=45;
                }
                else
                        m-=45;
                printf("%d %d\n", h, m);
        }
        return 0;
}