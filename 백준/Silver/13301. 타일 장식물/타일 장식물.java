import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int t = scan.nextInt();
		long[] dp = new long[82];
		dp[0] = 1;
		dp[1] = 1;
		dp[2] = 1;
		long[] leng = new long[81];
		for(int i = 3; i < 82; i++) {
			dp[i] = dp[i-1] + dp[i-2];
		}
		leng[1] = 4;
		for(int i = 2; i < 81; i++) {
			leng[i] = (dp[i] + dp[i+1])*2;
		}
		System.out.println(leng[t]);
		scan.close();
	}
}