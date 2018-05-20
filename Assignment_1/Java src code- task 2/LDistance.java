public class LDistance {
//implementing LevenshteinDistance class
	
	
 public static int getLDistance(String s, String t) {
  
	 
	 	if (s == null || t == null) {
	 		throw new IllegalArgumentException("Cannot accept strings as null");
	 		}

  int lengthS = s.length(); // s length
  
  int lengthT = t.length(); //  t length
  
  
  if (lengthS == 0) {
	  return lengthT;
  	} 
  else if (lengthT == 0) {
  
	  return lengthS;
  
  }
  
  
  if (lengthS > lengthT) {
   // swap input strings to consume less memory
   String tmp = s;
   
   s = t;
   
   t = tmp;
   
   lengthS = lengthT;
   
   lengthT = t.length();
  }
  
  
  int pC[] = new int[lengthS + 1]; 
  int cH[] = new int[lengthS + 1]; 
  int _pcH[]; 
  int i; 
  int j;
  char t_j; 
  int cost; 
  for (i = 0; i <= lengthS; i++) {
   pC[i] = i;
  }
  for (j = 1; j <= lengthT; j++) {
   t_j = t.charAt(j - 1);
   cH[0] = j;
   for (i = 1; i <= lengthS; i++) {
    cost = s.charAt(i - 1) == t_j ? 0 : 1;
    
    cH[i] = Math.min(Math.min(cH[i - 1] + 1, pC[i] + 1), pC[i - 1] + cost);
   }
   
   _pcH = pC;
   pC = cH;
   cH = _pcH;
  }
  
  return pC[lengthS];
 }


 public static void main(String[] args) {
  

 }
}