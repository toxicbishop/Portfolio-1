class Shape {
	void draw() { System.out.println("Shape class: draw called."); }
	
	void erase() { System.out.println("Shape class: erase called."); }
}

class Circle extends Shape {
	
	void draw() { System.out.println("Cirle class: draw called."); }
	
	void erase() { System.out.println("Cirle class: erase called."); }	
}

class Triangle extends Shape {

	void draw() { System.out.println("Triangle class: draw called."); }
	
	void erase() { System.out.println("Triangle class: erase called."); }
}

class Square extends Shape {

	void draw() { System.out.println("Square class: draw called."); }
	
	void erase() { System.out.println("Square class: erase called."); }
}

public class InheritanceDemo {

	public static void main(String[] args) {
		
		Shape s;
		
		Circle   c = new Circle();
		Triangle t = new Triangle();
		Square  sq = new Square();

		//Circle object
		s = c;
		s.draw();
		s.erase();
		System.out.println(" ");
		
		//Triangle object
		s = t;
		s.draw();
		s.erase();
		System.out.println(" ");
		
		//Square object
		s = sq;
		s.draw();
		s.erase();
	} //end main
} //end InhetitanceDemo 
