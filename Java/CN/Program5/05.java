import java.io.*;
import java.net.*;
import java.util.Scanner;

class Sender {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter total number of frames: ");
		int totalFrames = scanner.nextInt();
		System.out.print("Enter window size: ");
		int windowSize = scanner.nextInt();
		try (Socket socket = new Socket("localhost", 5000)) {
			System.out.println("Sender connected to receiver.");
			DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
			DataInputStream dis = new DataInputStream(socket.getInputStream());
			// Send totalFrames and windowSize to receiver
			dos.writeInt(totalFrames);
			dos.writeInt(windowSize);
			dos.flush();
			int base = 0;
			int nextFrame = 0;
			while (base < totalFrames) {
				// Send frames within window
				while (nextFrame < base + windowSize && nextFrame < totalFrames) {
					System.out.println("Sender: Sending Frame " + nextFrame);
					dos.writeInt(nextFrame);
					dos.flush();
					nextFrame++;
					Thread.sleep(300); // simulate delay
				}
				try {
					socket.setSoTimeout(2000);
					int ack = dis.readInt();
					System.out.println("Sender: Received ACK for Frame " + ack);
					if (ack >= base) {
						base = ack + 1;
					}
				} catch (SocketTimeoutException e) {
					System.out.println("Sender: Timeout waiting for ACK. Resending from Frame " + base);
					nextFrame = base; // Go-Back-N retransmission
				}
			}
			System.out.println("Sender: All frames sent and acknowledged. Closing connection.");
			dos.close();
			dis.close();
			socket.close();
			scanner.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}

class Receiver {
	public static void main(String[] args) {
		try (ServerSocket serverSocket = new ServerSocket(5000)) {
			System.out.println("Receiver started. Waiting for connection...");
			Socket socket = serverSocket.accept();
			System.out.println("Sender connected.");
			DataInputStream dis = new DataInputStream(socket.getInputStream());
			DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
			// Read totalFrames and windowSize from sender
			int totalFrames = dis.readInt();
			int windowSize = dis.readInt();
			System.out.println("Receiver: Total Frames = " + totalFrames + ", Window Size = " + windowSize);
			int expectedFrame = 0;
			while (expectedFrame < totalFrames) {
				int frame = dis.readInt();
				System.out.println("Receiver: Received Frame " + frame);
				if (frame == expectedFrame) {
					System.out.println("Receiver: Frame " + frame + " is expected. Sending ACK.");
					dos.writeInt(frame);
					dos.flush();
					expectedFrame++;
				} else {
					System.out.println("Receiver: Frame " + frame + " is NOT expected. Discarding.");
					dos.writeInt(expectedFrame - 1); // resend last ACK
					dos.flush();
				}
			}
			System.out.println("Receiver: All frames received successfully. Closing connection.");
			dis.close();
			dos.close();
			socket.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}