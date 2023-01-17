import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int t = scan.nextInt();
		long[] dp = new long[5001];
		dp[0] = 1;
		for(int i = 2; i < 5001; i+=2) {
			for(int j = 2; j < i+1; j+=2) {
				dp[i] += (dp[i-j]*dp[j-2]) % 1000000007L;
				dp[i] %= 1000000007L;
			}
		}
		for(int i = 0; i < t; i++) {
			int n = scan.nextInt();
			System.out.println(dp[n] % 1000000007L);
		}
		scan.close();
	}
}