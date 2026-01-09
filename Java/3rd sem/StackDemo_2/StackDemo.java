import java.util.Scanner;
class Stack {

	int a[]; 
	int top; 
	int size;

	Stack() {
		size = 3;
		top = -1;
		a = new int[3];
	}
	
	Stack(int size) { 
		this.size = size; 
		top = -1;
		a = new int[size];
	}
	
	void push(int item) { 
		if(top == size-1) {
			System.out.println("Stack Overflow.");
			return;
		}
		a[++top] = item;
	}
	
	int pop() {
		int item;
	
		if(top == -1) {
			System.out.println("Stack Underflow."); 
			return -1;
		}
		
		item = a[top]; 
		top--;
		
		return item;
	}
	 
	void display() { 
		int i;
	
		if(top == -1) {
			System.out.println("Stack Underflow."); 
			return;
		}
		
		System.out.println("Stack: "); 
		for(i = 0; i <= top; i++)
			System.out.print("	"+a[i]);
		
		System.out.println("	"); 
		return;
	}
} //end Stack class
 
public class StackDemo {

	public static void main(String[] args) { 
		Scanner scan = new Scanner(System.in); 
		
		Stack stk = new Stack(10);
		int ch; int item;
		
		for(;;) {
			System.out.println("\n1.Push	2.Pop 3.Display 4.Exit"); 
			System.out.print("Choice: ");
			ch = scan.nextInt();
			
			switch(ch) {
				case 1: System.out.print("Enter item: "); 
						item = scan.nextInt(); 
						stk.push(item);
						break;
				
				case 2: item = stk.pop();
						if(item != -1)
							System.out.println("Item poped : "+ item);
						break;
						
				case 3: stk.display(); 
						break;
				
				default: System.out.println("Thank You "); 
						scan.close();
						return;
			
			} //end switch
		} //end for
		
	}	//end main
} //end StackDemo
