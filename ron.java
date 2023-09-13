import java.util.Scanner;

public class ron{
  public static void main(String[]args){
    Scanner input = new Scanner(System.in);
    System.out.println("Enter base: ");
    int base = input.nextInt();
    
    int height = 21;
    int hypothenuse = 33;
    int perimeter = base+ height + hypothenuse;
    double area = 0.5 * base * height;

    System.out.println("-----------");
    System.out.println();
    System.out.println("Base is: " + base);
    System.out.println("Height is: " + height);
    System.out.println("Hypothenuse is: " + hypothenuse);
    System.out.println("Perimiter is: " + perimeter);
    System.out.println("Area is " + area);
    System.out.println();
    System.out.println();
  }
}
