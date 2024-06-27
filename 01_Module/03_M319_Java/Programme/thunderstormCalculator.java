import java.util.Scanner;

public class thunderstormCalculator {
    public static void main (String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("How many seconds did it take until the thunder reached you?");
        Integer seconds = input.nextInt();

        Integer distance = (seconds * 344) / 1000;

        System.out.println("The lighting was " + distance + "km away");

        input.close();
    }
}
