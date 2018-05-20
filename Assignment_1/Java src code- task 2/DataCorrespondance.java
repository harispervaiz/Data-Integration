import java.util.ArrayList;

public class DataCorrespondance {
 public static void main(String[] url) {
	 
	 CSVParser csvparser = new CSVParser();
	 LDistance distanceCalculator = new LDistance();
	 
	 
  ArrayList < ArrayList < String >> imdb = csvparser.getData("C:\\Users\\Nabeel\\Downloads\\Documents\\TU Berlin Lectures\\DI\\Assignment 1\\imdb.csv");
  ArrayList < ArrayList < String >> rotten = csvparser.getData("C:\\Users\\Nabeel\\Downloads\\Documents\\TU Berlin Lectures\\DI\\Assignment 1\\rotten_tomatoes.csv");
  
  int[] minimum = new int[imdb.get(0).size()];
  
  	for (int i = 0; i < imdb.size(); i++) { 
  		for (int j = 0; j < imdb.get(i).size(); j++) { 
  			if (j > minimum.length) break;
  				int minimumDistance = Integer.MAX_VALUE;
    for (int k = 0; k < rotten.size(); k++) {
    	//rotten rows
    	for (int l = 0; l < rotten.get(l).size(); l++) { 
    			
    		int distance =
    				distanceCalculator.getLDistance(imdb.get(i).get(j), rotten.get(k).get(l));
    		if (distance < minimumDistance) {
    			minimumDistance = distance;
    			minimum[j] = l;
    		}
     }
    	
     break;
    }
    
   }
   break;
  }
  
  	double sameColumns = 0;
  	double total = minimum.length;
  
  for (int i = 0; i < minimum.length; i++) {
   System.out.println("column in imdb - " + i + ", column in RottenTOmatoes -  " + minimum[i]);
   if (i == minimum[i])
    sameColumns++;
  }
  
  
  	double precision = sameColumns / total;
  	double recall = sameColumns / 10;
  
  	System.out.println("Calculated Precision - " + precision);
  
  	System.out.println("Calculated Recall -  " + recall);
 }
}