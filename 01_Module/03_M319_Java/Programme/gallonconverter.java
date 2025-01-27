public class gallonconverter {

	public static void main(String[] args) {
	
        //defining variables:
		
		double gallons;
		double litres;
        double count;
		
		gallons = 1;
        count = 1;              //assigns a value
		

        while (gallons <= 100) {
            litres = gallons / 3.7854;
            
            if (count == 10) {
                System.out.println(gallons + " gallons ist " + litres + " litres.\n");
                count = 0;
            } else {
                System.out.println(gallons + " gallons ist " + litres + " litres.");
            }
            gallons += 1;
            count += 1;
        }
	}

}
