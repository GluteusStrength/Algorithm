#include <stdio.h>
long long int arr[36];

int main(void) {
	int n;
	scanf("%d", &n);
	arr[0] = 1;
	for (int i = 1; i < n+1; i++) {
		for (int j = 0; j < i; j++) {
			arr[i] += arr[j] * arr[i - j - 1];
		}
	}
	printf("%lld\n", arr[n]);
	return 0;
}