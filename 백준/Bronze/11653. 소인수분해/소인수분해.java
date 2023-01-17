import java.util.Scanner;
import java.lang.Math;

public class Main {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int[] array = Arr(n);
		for(int i = 2; i < n+1; i++) {
			if(array[i] == 0) {
				while(n%i == 0) {
					n /= i;
					System.out.println(i);
					}
				}
				if(n==1) {
					break;
			}
		}
	}
	public static int[] Arr(int n) {
		if(n==1) {
			return null;
		}
		double sq = Math.sqrt(n);
		int[] ARR = new int[n + 1];
		ARR[1] = 1;
		for(int i = 2; i < (int)sq + 1; i++) {
			if(ARR[i] == 0) {
				for(int j = i+i; j < n+1; j+=i) {
					ARR[j] = 1;
				}
			}
		}
		return ARR;
	}

}
