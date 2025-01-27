import java.util.Scanner;

/**
 * @apiNote Whoever reads this is dump. 
 * @author Dario Kulici
 */
public class HarassBerechnung {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Integer Flaschen = 0;
        Integer Harasse = 0;
        Integer HarassGrösse = 6;
        Boolean active = true;
        String again = "";
        Integer counter = 1;

        do {
            System.out.println("Anzahl Flaschen?");
            Flaschen = input.nextInt();

            if (Flaschen <= 0 || Flaschen == 99) {
                System.out.println("Sie brauchen keine Harass!");
            }
            else if (Flaschen > 0) {
                while (Flaschen > 0) {
                    Flaschen = Flaschen - HarassGrösse;
                    Harasse ++;
                }
                System.out.println("Sie brauchen " + Harasse + " Harasse.\n");
            }
            System.out.println("Nochmal berechnen? (yes/no)");
            again = input.next();
            switch (again) {
                
                case "yes":
                    active = true;
                    counter++;
                    Flaschen = 0;
                    Harasse = 0;
                    break;
                
                case "no" :
                    active = false;
                    break;
                
                default:
                    System.err.println("Wrong input. Closing programm...\n");
                    active = false;
                    break;
            }
        
        } while (active == true && counter <= 3);

        input.close();
    }
}