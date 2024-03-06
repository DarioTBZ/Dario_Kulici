import java.util.Scanner;

public class RichtigFalsch {
    public static void main(String[] args ) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Willkommen zu dieser Fragerunde! Beantworte die Fragen richtig und komme weiter!");
        int frage = 1;
        String answer = "";
        
        System.out.println("Welche Farbe hat der Himmel?");
        answer = scan.next();
        if (answer == "blau") {
            System.out.println("Das ist richtig! Nächste Frage!");
            frage = 2;
        }
        System.out.println(answer);

        // while (frage == 1) {
            
        //} 
    }
}
