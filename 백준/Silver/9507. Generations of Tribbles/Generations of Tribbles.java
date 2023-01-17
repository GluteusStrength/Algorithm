import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		long[] arr = new long[68]; // long int형 배열 선언
		for(int i = 0; i < 68; i++) {
			if (i < 2) {
				arr[i] = 1;
			}
			else if(i == 2) {
				arr[i] = 2;
			}
			else if(i == 3) {
				arr[i] = 4;
			}
			else {
				arr[i] = arr[i-4] + arr[i-3] + arr[i-2] + arr[i-1];
			}
		}
		for(int i = 0; i < n; i++) {
			int t = scan.nextInt();
			System.out.println(arr[t]);
		}
		scan.close();
	}

}
