import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		double[] arr = new double[n+1];
		for(int i = 1; i < n+1; i++) {
			arr[i] = scan.nextDouble();
		}
		double ans = 0;
		for(int i = 1; i < n; i++) {
			double flag = arr[i];
			ans = Math.max(ans, flag);
			for(int j = i + 1; j < n + 1; j++) {
				flag *= arr[j];
				ans = Math.max(ans,  flag);
			}
	
		}
		ans = Math.max(ans, arr[n]);
		System.out.printf("%.3f", ans);

		scan.close();
	}

}
