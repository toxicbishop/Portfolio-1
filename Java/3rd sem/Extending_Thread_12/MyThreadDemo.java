class MyThread extends Thread {
	String name;
	MyThread(String name) {
		super(name);
		start();
		this.name = name;
	}
	public void run() {
		int i;
		try {
			for(i = 0; i < 5; i++) {
				System.out.println(name + ": " + i);
				Thread.sleep(1000);
			}				
		}
		catch(InterruptedException e) {
			System.out.println("InterruptedException Caught");
		}
		System.out.println("Child Thread Completed.");
	}
}
public class MyThreadDemo {
	public static void main(String[] args) {
		int i;
		new MyThread("Child Thread");
		try {
			for(i = 0; i < 5; i++) {
				System.out.println("Main Thread : " + i);
				Thread.sleep(1000);
			}				
		}
		catch(InterruptedException e) {
			System.out.println("InterruptedException Caught");
		}	
		System.out.println("Main Thread Completed.");
	} 
}