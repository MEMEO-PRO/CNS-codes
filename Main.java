import java.util.Scanner;
import java.util.Vector;

public class Main{
    public static void main(String[] args){
        Vector<String> stringVector = new Vector<>();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of strings to add: ");
        int n = sc.nextInt();
        for(int i = 0; i<n; i++){
            String str = sc.nextLine();
            stringVector.add(str);

        }
        System.out.print("Enter a new string to check: ");
        String newString = sc.nextLine();

        if(stringVector.contains(newString)){
            stringVector.remove(newString);
            System.out.println("deleted");

        }

        System.out.println("Updated vector: ");
        for(String str : stringVector){
            System.out.println(str);
        }
        sc.close();
    }

    
}