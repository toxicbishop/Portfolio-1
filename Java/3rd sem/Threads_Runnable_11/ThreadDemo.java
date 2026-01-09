class Counter implements Runnable {
	Thread t;
	String name = null;
	Counter(){
		this.name = "Counter";
		t = new Thread(this, name);
		System.out.println("Thread Created: " + name);
	}
	Counter(String name) {
		this.name = name;
		t = new Thread(this, name);
		System.out.println("Thread Created: " + name);
	}
	void start() {
		t.start();
	}
	public void run() {
		int i;
		try {
			for(i = 0; i < 5; i++) {
				System.out.println(name + ": " + i);
				Thread.sleep(500);
			}				
		}
		catch(InterruptedException e) {
			System.out.println("InterruptedException Caught");
		}
	}
} 
public class ThreadDemo {
	public static void main(String args[]) {
		Counter c1 = new Counter("Counter1");
		Counter c2 = new Counter("Counter2");
		Counter c3 = new Counter("Counter3");
		c1.start();
		c2.start();
		c3.start();
	}
}