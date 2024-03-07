import java.util.Scanner;

public class celciusfahrenheitcalculator {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        System.out.println("Enter desired unit of mesurement, c or f");
        String desiredUnit = input.nextLine(); // Take Input from User wich Unit has to be calculated

        if (desiredUnit.equals("c")) {
            System.out.println("Enter fahrenheit: ");
            Double FtoC = input.nextDouble();
            Double calculationToFahrenheit = (FtoC - 32) * 5/9;

            System.out.println("The sum is: " + calculationToFahrenheit);

        } else if (desiredUnit.equals("f")) {
            System.out.println("Enter celsius: ");
            Double CtoF = input.nextDouble();
            Double calculationToCelsius = (CtoF * 9/5) + 32;

            System.out.println("The sum is: " + calculationToCelsius);
        }
    }
}
