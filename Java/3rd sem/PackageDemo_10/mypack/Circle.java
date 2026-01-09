package mypack;
public class Circle {
	int r;
	public Circle () {
		this.r = 5;
	}
	public Circle(int r){
		this.r = r;
	}
	public double area() {
		return 3.14 * r * r;
	}
}
