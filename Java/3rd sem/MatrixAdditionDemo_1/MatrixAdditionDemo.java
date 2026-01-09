import java.util.Scanner;

public class MatrixAdditionDemo {

	public static void main(String[] args) {

		int row1, col1, row2, col2, i, j;
		Scanner in = new Scanner(System.in);
		 
		//Read order of matrix 1
		System.out.println("Enter order of Matrix 1: ");
		System.out.print("Enter number of rows: ");
		row1 = in.nextInt();
		 
		System.out.print("Enter number of columns: ");
		col1 = in.nextInt();
		 
		//Read order of matrix 2
		System.out.println("\nEnter order of Matrix 2: ");
		System.out.print("Enter number of rows: ");
		row2 = in.nextInt();
		 
		System.out.print("Enter number of columns: ");
		col2 = in.nextInt();

		int mat1[][] = new int[row1][col1];
		int mat2[][] = new int[row2][col2];
		
		//Check matrix addition compatibility
		if(row1 != row2 || col1 != col2) {
			System.out.println("\nCan't add matrices.");
			System.exit(0);
		}
		
		int res[][]  = new int[row1][col1];
		 
		//Read matrix 1
		System.out.println("Enter the elements of matrix 1: ");
		for ( i = 0 ; i < row1; i++ )
			for ( j= 0 ; j < col1 ;j++ )
				mat1[i][j] = in.nextInt();
				
		//Read matrix 2
		System.out.println("Enter the elements of matrix 2: ");
		for ( i = 0 ; i < row2; i++ )
		 	for ( j= 0 ; j < col2 ;j++ )
		 		mat2[i][j] = in.nextInt();
	
		//Addition of two matrices
		for ( i= 0 ; i < row1 ; i++ )
			for ( j= 0 ; j < col1 ;j++ )
				res[i][j] = mat1[i][j] + mat2[i][j] ; 
		 
		//Display Result
		System.out.println("Sum of matrices:");		 
		for ( i= 0 ; i < row1 ; i++ )
		{ 
			for ( j= 0 ; j < col1 ;j++ )
				System.out.print(res[i][j]+"\t");
		 	System.out.println();
		}		 
	} //end main
} //end class
