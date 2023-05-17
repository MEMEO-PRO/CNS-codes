import java.util.Scanner;
import java.util.Vector;

public class Main {
    public static void main(String[] args) {
        Vector<String> studentNames = new Vector<>();
        
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Enter student names (type 'exit' to stop):");
        
        String name;
        do {
            name = scanner.nextLine();
            if (!name.equalsIgnoreCase("exit")) {
                studentNames.add(name);
            }
        } while (!name.equalsIgnoreCase("exit"));
        
        System.out.println("Student names entered:");
        for (String studentName : studentNames) {
            System.out.println(studentName);
        }
        
        scanner.close();
    }
}
