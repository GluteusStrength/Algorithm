#include <stdio.h>
long long int arr[1000001];

int main(void) {
	int n, mod = 1000000007;
	scanf("%d", &n);
	arr[1] = 1;
	for (int i = 2; i < n + 1; i++) {
		arr[i] = (arr[i - 1] + arr[i - 2]) % mod;
	}
	printf("%d\n", arr[n]);
	return 0;
}