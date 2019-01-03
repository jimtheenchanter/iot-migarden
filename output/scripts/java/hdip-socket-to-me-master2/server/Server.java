import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class Server extends Thread{

    static int port=50100;
    static ServerSocket echo;

    public static void main( String args[] ) throws IOException{
        echo = new ServerSocket(port);
        Thread t = new Server();
        t.start();
    }

    public void run() {
        System.out.format("ECHO server now running (on port %d)%n",port);
        while(true)
        {
            Socket connection = null;
            try {
                connection = echo.accept();
            } catch (IOException e) {
                System.err.println("Cannot accept connection");
                return;
            }
            try {
                System.out.println("Connection from client");
                BufferedReader in =
                        new BufferedReader(
                                new InputStreamReader(connection.getInputStream()));
                PrintWriter out =
                        new PrintWriter(connection.getOutputStream(),true);
                String data;
                while ((data = in.readLine()) != null){
                    out.println(data);
                }
                in.close();
            } catch ( IOException e ) {
                System.err.println("Communication Error");
            } finally {
                try {
                    connection.close();
                } catch (IOException e) {
                }
            }
        }
    }
}
