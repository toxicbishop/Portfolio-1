import java.util.Scanner;

class Employee {
	String ID;
	String name;
	double salary;
	
	void read(Scanner scan) {
		System.out.print("ID    : ");
		ID = scan.next();
		
		System.out.print("Name  : ");
		name = scan.next();
		
		System.out.print("Salary: ");
		salary = scan.nextDouble();
	}
	
	double raiseSalary(double p) {
			
		salary += salary * p;
		return salary;
	} //End raiseSalary	

	public void display() {
		System.out.printf("%5s %10s %10.2f \n",ID, name, salary);
	}
	
} //End Employee

public class EmployeeDemo {
	public static void main(String[] args) {

		int i, j;		
		
		Scanner scan = new Scanner(System.in); 
		
		System.out.print("Enter number of employees: ");
		int n = scan.nextInt();
		Employee emp[] = new Employee[n];
		
		//Read Employee details
		System.out.print("Enter employee details: ");
		for(i = 0; i < n; i++) {
			System.out.println("\nEmployee "+ (i+1) +": ");
			
			emp[i] = new Employee();
			emp[i].read(scan);
		}
		
		//Display Employee details before Salary Raise
		System.out.println("\nEmployee details(before Salary Raise): ");
		System.out.printf("%5s %10s %10s \n","ID","Name","Salary");
		for(i = 0; i < n; i++) {
			emp[i].display();
		}
		
		//Employee Salary Raise
		System.out.println("\nEmployee Salary Raise(%): ");
		for(i = 0; i < n; i++) {
			System.out.print("Employee "+ (i+1) +": ");			
			
			double raise = scan.nextDouble();
			emp[i].raiseSalary(raise/100);
		}
		
		//Display Employee details (after Salary Raise)
		System.out.println("\nEmployee details(after Salary Raise): ");
		System.out.printf("%5s %10s %10s \n","ID","Name","Salary");
		for(i = 0; i < n; i++) {
			emp[i].display();
		}
	} //End main
} // End EmployeeDemo
