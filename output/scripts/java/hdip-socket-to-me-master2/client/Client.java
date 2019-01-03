
import java.io.*;
import java.net.*;
public class Client {
    static String serverName = "127.0.0.1";
    static int port = 50100;
    public static void main(String[] args) throws IOException {
        Socket echoSocket = null;
        PrintWriter out = null;
        BufferedReader in = null;
        try {
            echoSocket = new Socket(serverName, port);
            out = new PrintWriter(echoSocket.getOutputStream(), true);
            in = new BufferedReader(new InputStreamReader(
                    echoSocket.getInputStream()));
            System.out.format("ECHO client now connected to %s  on port %d %n",serverName,port);
        } catch (UnknownHostException e) {
            System.err.format("Don't know about host: %s.",serverName);
            System.exit(1);
        } catch (IOException e) {
            System.err.format("Couldn't get I/O for the connection to: %s.", serverName);
            System.exit(1);
        }

        BufferedReader stdIn = new BufferedReader(
                new InputStreamReader(System.in));
        String userInput;
        while ((userInput = stdIn.readLine()) != null) {
            out.println(userInput);
            System.out.println("echo: " + in.readLine());
        }
        out.close();
        in.close();
        stdIn.close();
        echoSocket.close();
    }
}
