import java.util.Scanner;

public class Notenrechner {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Double note = 0.0;
        Boolean active = true;
        String frage = "yes";


        while (active == true) {
            note = 0.0;
            System.out.println("How many tests?");
            Integer tests = scan.nextInt();

            if (tests < 3) {
                System.out.println("\nThe minimum amount of tests is 3.\n");
                continue;
            }
        
        
            for (Integer i = 1; i != tests + 1; i++) {
                System.out.println("Enter the " + i + ". mark:");
                Double new_note = scan.nextDouble();

                if (new_note < 1 || new_note > 6) {
                    break;
                }

                note += new_note;
            }
            
            Double resultat = note / tests;

            System.out.println("Your average mark is: " + resultat);

            if (resultat >= 5.5) {
                System.out.println("Bravo, gut gemacht!");
            }
    
            System.out.println("\nDo you want other marks? (yes/no)");
                frage = scan.next();
    
            switch (frage) {
                case "yes":
                    active = true;                 
                    break;
                case "no":
                    System.out.println("Okay, goodbye!");
                    active = false;
                    break;
                default: 
                    System.out.println("Error: wrong syntax");
                    return;
                }
        }
        scan.close();
    }
}
