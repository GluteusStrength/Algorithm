import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		char s = '*';
		char t = ' ';
		for(int i = 1; i <= n; i++) {
			for(int j = 0; j < i-1; j++) {
				System.out.print(t);
			}
			for(int k = n; k > i-1; k--) {
				System.out.print(s);
			}
			System.out.print('\n');
		}
	}

}
