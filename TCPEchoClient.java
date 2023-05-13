import java.io.*;
import java.net.*;

public class TCPEchoClient {
    public static final String SERVER_HOST = "localhost";
    public static final int SERV_TCP_PORT = 5035;

    public static void main(String[] args) {
        try {
            Socket clientSocket = new Socket(SERVER_HOST, SERV_TCP_PORT);
            System.out.println("Connected to server: " + SERVER_HOST);

            BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            PrintWriter outToServer = new PrintWriter(clientSocket.getOutputStream(), true);

            String messageToSend = "Hello from client";
            System.out.println("Sending to server: " + messageToSend);
            outToServer.println(messageToSend);

            String serverResponse = inFromServer.readLine();
            System.out.println("Received from server: " + serverResponse);

            clientSocket.close();
            System.out.println("Disconnected from server: " + SERVER_HOST);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
