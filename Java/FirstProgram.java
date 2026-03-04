import java.util.Scanner;
public class FirstProgram {

    public static void main(String[] args) {
        // This is pythagorean theroum.
        Scanner input = new Scanner(System.in);
        System.out.println("This is the pythagorean theorum \n Please enter A: ");
        int a = input.nextInt();
        System.out.println("b= ");
        int b = input.nextInt();

        double c = Math.sqrt(Math.pow(a,2) + Math.pow(b,2));

        System.out.print("The Hypotnuse is " + c);
        input.nextLine();
        System.out.println("What is your name? : ");
        input.nextLine();
        String name = input.nextLine();
        System.out.println("welcome " + name);



        input.close();
         System.out.print(Integer.MAX_VALUE);




    }
    
}
// this is a comment.
/* yfchg

lugough/kgh:lhi

 */