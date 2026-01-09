class Outer {

	void display() {
		System.out.println("Outer Class: display called.");
		Inner inner = new Inner();
	}
	
	
	class Inner {
		void display() {
			System.out.println("Inner Class: display called.");
		}		
	}
}

public class InnerClassDemo {
	public static void main(String args[]) {
		Outer out = new Outer();
		out.display();
		
		Outer.Inner in = new Outer().new Inner();
		in.display();
		
	}
}