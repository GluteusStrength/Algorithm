import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		long[] arr = new long[117];
		arr[1] = 1;
		arr[2] = 1;
		arr[3] = 1;
		for(int i = 4; i < n + 1; i++) {
			arr[i] = arr[i-3] + arr[i-1];
		}
		System.out.println(arr[n]);
		scan.close();
	}

}
