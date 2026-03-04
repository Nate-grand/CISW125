import java.util.Scanner;
public class FirstProgram {

    public static void main(String[] args) {
        // This is pythagorean theroum.
        Scanner input = new Scanner(System.in);
        System.out.println("This is the pythagorean theorum \n Please enter");
        int a = input.nextInt();
        System.out.println("b= ");
        int b = input.nextInt();

        double c = Math.sqrt(Math.pow(a,2) + Math.pow(b,2));

        System.out.print("The Hypotnuse is " + c);

        input.close();
         System.out.print(Integer.MAX_VALUE);




    }
    
}
// this is a comment.
/* yfchg

lugough/kgh:lhi

 */