import java.util.Arrays; 
import java.util.Random; 
class GoBackNProtocol { 
private final int WINDOW_SIZE;  // Window size 
private final int TOTAL_FRAMES;  // Total number of frames 
private int nextFrameToSend = 0;  // Index of the next frame to send 
private int frameExpectedByReceiver = 0;  // The frame that the receiver expects next
public GoBackNProtocol(int totalFrames, int windowSize) { 
this.TOTAL_FRAMES = totalFrames; 
this.WINDOW_SIZE = windowSize; 
} 
public void sendFrames() { 
Random random = new Random(); 
while (nextFrameToSend < TOTAL_FRAMES) { 
// Simulate sending frames in the current window 
for (int i = 0; i < WINDOW_SIZE && nextFrameToSend < TOTAL_FRAMES; i++) { 
System.out.println("Sender: Sending frame " + nextFrameToSend); 
nextFrameToSend++; 
} 
// Simulate receiving an ACK with some random loss 
if (random.nextBoolean()) { 
frameExpectedByReceiver += WINDOW_SIZE; 
System.out.println("Receiver: ACK received for frames up to " + frameExpectedByReceiver); 
} else { 
System.out.println("Receiver: ACK lost, resending frames from " + 
(frameExpectedByReceiver)); 
nextFrameToSend = frameExpectedByReceiver;  // Go back to the unacknowledged frame 
} 
} 
System.out.println("All frames sent and acknowledged successfully."); 
} 
public static void main(String[] args) { 
int totalFrames = 10;  // Total number of frames to send 
int windowSize = 4;  // Window size 
GoBackNProtocol protocol = new GoBackNProtocol(totalFrames, windowSize); 
protocol.sendFrames(); 
} 
} 
/*Output: 
Sender: Sending frame 0 
Sender: Sending frame 1 
Sender: Sending frame 2 
Sender: Sending frame 3 
Receiver: ACK received for frames up to 4 
Sender: Sending frame 4 
Sender: Sending frame 5 
Sender: Sending frame 6 
Sender: Sending frame 7 
Receiver: ACK lost, resending frames from 4 
Sender: Sending frame 4 
Sender: Sending frame 5 
Sender: Sending frame 6 
Sender: Sending frame 7 
Receiver: ACK received for frames up to 8 
Sender: Sending frame 8 
Sender: Sending frame 9 
Receiver: ACK received for frames up to 12 
All frames sent and acknowledged successfully.*/ 