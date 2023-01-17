import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int[] fib = new int[51];
		int mod = 1000000007;
		fib[0] = 1;
		fib[1] = 1;
		fib[2] = 3;
		for(int i = 3; i <= n; i++) {
			fib[i] = (fib[i-1] + fib[i-2] + 1) % mod;
		}
		System.out.println(fib[n]);
	}
}