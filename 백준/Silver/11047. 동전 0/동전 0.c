#include <stdio.h>
int arr[1000001];

int main(void) {
	int n, k, cnt = 0;
	scanf("%d%d\n", &n, &k);
	for (int i = 1; i < n + 1; i++) {
		scanf("%d", &arr[i]);
	}
	for (int i = n; i > 0; i--) {
		if (k / arr[i] >= 1) {
			cnt += k / arr[i];
			k %= arr[i];
		}
		if (k == 0) {
			break;
		}
	}
	printf("%d\n", cnt);
	return 0;
}