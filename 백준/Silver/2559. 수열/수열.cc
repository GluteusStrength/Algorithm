#include <stdio.h>
#define MAX(a,b) a > b ? a : b
int arr[100001];
int psum[100001];
int main(void) {
	int n, k;
	int max = -100000001;
	scanf("%d%d", &n, &k);
	for (int i = 1; i < n + 1; i++) {
		scanf("%d", &arr[i]);
	}

	for (int i = 1; i < n + 1; i++) {
		psum[i] = psum[i - 1] + arr[i];
	}

	for (int i = k; i < n + 1; i++) {
		max = MAX(max, psum[i] - psum[i - k]);
	}

	printf("%d", max);

	return 0;
}