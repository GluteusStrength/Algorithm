import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int t = scan.nextInt();
		long mod = 1000000009L;
		long[][] dp = new long[100001][3];
		dp[1][0] = 1;
		dp[2][1] = 1;
		dp[3][0] = 1;
		dp[3][1] = 1;
		dp[3][2] = 1;
		for(int i = 4; i < 100001; i++) {
			for(int j = 0; j < 3; j++) {
				if(j==0) { // 1 붙이기
					dp[i][j] = (dp[i-1][1] + dp[i-1][2]) % mod;
				}
				else if(j==1) { // 2 붙이기
					dp[i][j] = (dp[i-2][0] + dp[i-2][2]) % mod;
				}
				else { // 3 붙이기
					dp[i][j] = (dp[i-3][0] + dp[i-3][1]) % mod;
				}
			}
		}
		for(int i = 0; i < t; i++) {
			long ans = 0L;
			int k = scan.nextInt();
			for(int j = 0; j < 3; j++) {
				ans += dp[k][j];
			}
			System.out.println(ans % mod);
		}
	}
}