#include <stdio.h>
#define MAX(a,b) a > b ? a : b
int arr[1001];
int dp[1001]; //일단 기본적으로는 0으로 초기화
int main(void) {
	int n;
	int max = 0;
	scanf("%d", &n);
	for (int i = 1; i < n+1; i++) {
		scanf("%d", &arr[i]); //1 2 3 4 5 이렇게 입력하면 spacebar를 기준으로 하나씩 입력된다.
	}
	for (int i = 1; i < n+1; i++) {
		dp[i] = 1;
	}

	for (int i = 2; i < n+1; i++) {
		for (int j = 1; j < i; j++) {
			if (arr[i] > arr[j]) {
				dp[i] = MAX(dp[i], dp[j] + 1);
			}
		}
		max = MAX(max, dp[i]);
	}
	if(n > 1){ 
		printf("%d", max); 
	}
	else {
		printf("%d", 1);
	}
	return 0;
}