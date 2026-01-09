import java.util.Scanner;
class CustomException extends Exception {
	public String toString() {
		return "CustomException: Denominator is Zero";
	}
}
public class CustomExceptionDemo {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int a, b, c;
		System.out.printf("Enter a: ");
		a = scan.nextInt();
		System.out.printf("Enter b: ");
		b = scan.nextInt();
		try {
			if(b == 0)
				throw new CustomException();
			c = a / b;
			System.out.println("c = "+c);
		}
		catch (CustomException e) {
			b = 1;
			c = a / b;
			System.out.println("DivideByZero Exception caught and handled:  ");
			System.out.println("c = " + c);
		}
		finally {
			System.out.println("Finally block.");
		}
	}
}