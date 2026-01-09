interface Resizable {
	void resizeWidth(int width);
	void resizeHeight(int height); 
}

class Rectangle implements Resizable  {
	int width, height; 
	
	Rectangle() {
		width = height = 5;
	}
	
	Rectangle(int width, int height) {
		this.width = width;
		this.height = height;
	}
	
	public void resizeWidth(int width) {
		this.width = width;
	}

	public void resizeHeight(int height) {
		this.height = height;
	}
	
   public String toString() {
		String s = "Rectangle(width,height): (" +width+ "," +height+ ") \n";
		s += "Area: "+(width * height);
		return s; 
	}
		
}

public class InterfaceDemo {
	public static void main(String args[]) {
		Rectangle r1 = new Rectangle(2,4);
		Resizable r;
		
		r = r1;
		System.out.println(r);
		
		r.resizeWidth(10);
		r.resizeHeight(10);
		
		System.out.println(r);
				
	} //end main
} //end class
