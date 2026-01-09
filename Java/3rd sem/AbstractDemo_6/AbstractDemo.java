//Abstract class
abstract class Shape {
	abstract double calculateArea() ;
	
	abstract double calculatePerimeter();
}

//class Circle
class Circle extends Shape {
	int r;
	
	Circle() 		{ r = 10;     }
	Circle(int r) 	{ this.r = r; }
		
	double calculateArea () { 
		System.out.println("Cirle class: calculateArea() called.");
		return 3.14 * r * r;	//pi * r * r
	}
	
	double calculatePerimeter() { 
		System.out.println("Cirle class: calculatePerimeter() called.");
		return 2 * 3.14 * r;	//2 * pi * r
	}
}

//class Triangle
class Triangle extends Shape {
	int a, b, c;
	int p;
	
	Triangle() 	{ a = b = c = 10;     }
	Triangle (int a, int b, int c)  { 
		this.a = a; 
		this.b = b;
		this.c = c;
	}
	
	double calculateArea () { 
		System.out.println("Triangle class: calculateArea() called.");
		p = a + b + c;		//perimeter
		
		double s = p/2;		//semi-perimeter = perimeter/2
		
		//Heron's Formula
		double area = Math.sqrt(s * (s-a) * (s-b) * (s-c));
		
		return area;		
	}
	
	double calculatePerimeter() { 
		//Perimeter = sum of all sides (a + b + c)
		System.out.println("Triangle class: calculatePerimeter() called.");
		return (a + b + c);
	}
}

public class AbstractDemo {

	public static void main(String[] args) {
		
		Shape s;
		
		Circle   c = new Circle();
		Triangle t = new Triangle();

		//Circle object
		s = c;
		System.out.printf("Circle Area      : %5.2f \n\n", s.calculateArea() );
		System.out.printf("Circle Perimeter : %5.2f \n\n", s.calculatePerimeter() );
		
		//Triangle object
		s = t;
		System.out.printf("Triangle Area      : %5.2f \n\n", s.calculateArea() );
		System.out.printf("Triangle Perimeter : %5.2f \n\n", s.calculatePerimeter() );

	} //end main
} //end InhetitanceDemo 
