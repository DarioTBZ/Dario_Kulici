import java.util.Arrays;
import java.util.InputMismatchException;
import java.util.Scanner;
 
public class D3_Zahlensort {
 
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
 
       
        System.out.println("Vier Wörter eingeben:");
        String[] words = new String[4];
        for (int i = 0; i < words.length; i++) {
            words[i] = input.next();
        }

        Arrays.sort(words);

        System.out.println("Wörter alphabetisch sortiert:");
        for (String word : words) {
            System.out.println(word);
        }
 
        System.out.println("Gib vier Zahlen mit Nachkommastelle ein:");
        double[] numbers = new double[4];
        for (int i = 0; i < numbers.length; i++) {
            try {
                numbers[i] = input.nextDouble();
            } catch (InputMismatchException e) {
                System.err.println("Ungültige Eingabe!");
                input.next();
                i--;
            }
        }
 
        
        Arrays.sort(numbers);
 
        
        System.out.println("Zahlen von klein nach gross sortiert:");
        for (double number : numbers) {
            System.out.println(number);
        }
 
        
        System.out.println("Gebe vier Zahlen ein:");
        int[] numbersInt = new int[4];
        for (int i = 0; i < numbersInt.length; i++) {
            try {
                numbersInt[i] = input.nextInt();
            } catch (InputMismatchException e) {
                System.err.println("Ungültige Eingabe!");
                input.next();
                i--;
            }
        }
 
        
        Arrays.sort(numbersInt);
        for (int i = 0, j = numbersInt.length - 1; i < j; i++, j--) {
            int temp = numbersInt[i];
            numbersInt[i] = numbersInt[j];
            numbersInt[j] = temp;
        }

        
        System.out.println("Zahlen nach von gross nach klein sortiert:");
        for (int number : numbersInt) {
            System.out.println(number);
        }

        input.close();
    }
}