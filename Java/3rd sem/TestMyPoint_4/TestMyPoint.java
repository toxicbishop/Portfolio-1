class MyPoint{
	int x, y;
	
	//Zero argument constructor
	MyPoint () {
		x = y = 0;
	}
	
	//Parameterized constructor
	MyPoint (int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	//Set x and y
	void setXY (int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	//Return x and y as an array
	int[] getXY () {
		int p[] = new int[2];
		p[0] = x;
		p[1] = y;
		return p;
	}
	
	//Display point in format (x,y)
	public String toString() {
		return "(" +x+ ", " +y+ ")";
	}

	//Calculate distance between two points
	double distance(int x2, int y2) {
		double d;
		
		d = Math.sqrt(Math.pow((x2-x),2) + Math.pow((y2-y),2) );
		return d;
	}
	
	double distance(MyPoint p) {
		double d;

		d = Math.sqrt(Math.pow((p.x-x),2) + Math.pow((p.y-y),2) );
		return d;
	}
	
	double distance() {
		double d;

		d = Math.sqrt(Math.pow((x-0),2) + Math.pow((y-0),2) );
		//d = Math.sqrt(Math.pow((x),2) + Math.pow((y),2) );
		return d;
	}
	
} //end class Point

public class TestMyPoint {

	public static void main(String[] args) {

		MyPoint p1 = new MyPoint();			//using default constructor
		MyPoint p2 = new MyPoint();			//using default constructor
		MyPoint p3 = new MyPoint(2,3);		//using parameterized constructor
		
		int [] pa1, pa2, pa3;				//point array
		double dist; 
		
		p2.setXY(2, 4);						//using setxy()
		
		//1. Find distance between two points
		dist = p2.distance(1, 2);
		
		pa2 = p2.getXY();					//using getXY()
		System.out.printf("1. Distance between (%d, %d) to (1, 2): %5.2f \n", pa2[0], pa2[1], dist);
		
		//2. Find distance between current point and other point object
		dist = p2.distance(p3);
		
		pa2 = p2.getXY();
		pa3 = p3.getXY();
		System.out.printf("2. Distance between (%d, %d) to (%d, %d): %5.2f \n", pa2[0], pa2[1], pa3[0], pa3[1], dist);
		
		//3. Find distance between current point and origin
		dist = p2.distance();
		
		System.out.print("3. Distance between "+ p2 +" to "+ p1 + ": ");
		System.out.printf("%5.2f \n", dist);

	} //end main
}