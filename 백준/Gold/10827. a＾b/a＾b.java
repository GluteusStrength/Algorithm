import java.math.BigDecimal;
import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner scanner = new Scanner(System.in);
		BigDecimal a = scanner.nextBigDecimal();
		int b = scanner.nextInt();
		System.out.println(a.pow(b).toPlainString());
		scanner.close();
	}
	

}
