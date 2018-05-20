import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class CSVParser {
 public ArrayList < ArrayList < String >> getData(String url) {
	 
	 
  String csvFile = url;
  String line = "";
  
  ArrayList < ArrayList < String >> data = new ArrayList < ArrayList < String >> ();
  
  int columns = 0;
  
  final Pattern p = Pattern.compile("\"([w]*)\"");
  
  try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
	  boolean isFirst = true;
	
	  while ((line = br.readLine()) != null) {
		  ArrayList < String > words = new ArrayList < > ();
    boolean start = false;
    
    
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < line.length(); i++) {
     if (!start && line.charAt(i) == '"') {
      start = true;
      continue;
     }
  
     
     if (line.charAt(i) != '"')
      sb.append(line.charAt(i));
     if (start && line.charAt(i) == '"') {
      start = false;
      words.add(sb.toString());
      continue;
     }
    }
    data.add(words);
   }
   return data;
  } 
  
  catch (IOException e) {
   return new ArrayList < ArrayList < String >> ();
  }
 }

}