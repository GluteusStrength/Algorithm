#include <stdio.h>
int dp[10000001];

int main(void) {
	int n;
	scanf("%d", &n);
	dp[0] = 1;
	dp[1] = 1;

	for (int i = 2; i < n + 1; i++) {
		dp[i] = (dp[i - 2] + dp[i - 1]) % 10;
	}
	printf("%d", dp[n]);
	return 0;
}