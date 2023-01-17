// 처음에 문제를 잘못 생각함
import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int[] dp = new int[1000001];
		int[] two = new int[21];
		for(int i = 0; i < 21; i++) {
			two[i] = (int) Math.pow(2, i);
		}
		dp[1] = 1;
		dp[2] = 2;
		for(int i = 3; i < n+1; i++) {
			if(i%2 != 0) {
				dp[i] = dp[i-1];
			}
			else {
				dp[i] = (dp[i-1] + dp[i/2]);
			}
			dp[i] = dp[i] % 1000000000;
		}
		System.out.println(dp[n]%1000000000);
	}
}
