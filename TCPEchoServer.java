import java.io.*;
import java.net.*;

public class TCPEchoServer {
    public static final int SERV_TCP_PORT = 5035;

    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(SERV_TCP_PORT);
            System.out.println("TCP Echo Server started. Listening on port " + SERV_TCP_PORT);

            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Client connected: " + clientSocket.getInetAddress().getHostAddress());

                BufferedReader inFromClient = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                PrintWriter outToClient = new PrintWriter(clientSocket.getOutputStream(), true);

                String clientMessage = inFromClient.readLine();
                System.out.println("Received from client: " + clientMessage);

                outToClient.println("Server: " + clientMessage);

                clientSocket.close();
                System.out.println("Client disconnected: " + clientSocket.getInetAddress().getHostAddress());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

