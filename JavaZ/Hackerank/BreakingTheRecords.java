import java.util.*;

public class BreakingTheRecords {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);    
        int n = 10;//sc.nextInt();
        int [] a = {3, 4, 21, 36, 10, 28, 35, 5, 24, 42}; 
        
        List<Integer> ar = new ArrayList<>(n);
        for (int i :a) ar.add(i);
        
        int max,min,maxT=0,minT=0 ; 
        min = ar.get(0);
        max = min;
        
        for(int i=1;i<n;i++){
            int k;
            k = ar.get(i);
            
            if (max < k){
                maxT += 1;
                max = k;
            }
            if (min> k){ 
                 minT += 1; min = k;
            }
         //   System.out.printf("min:%d max:%d k:%d\n", min,max,k);
            //System.out.printf("minT:%d maxT:%d \n", minT,maxT);
	    }
	    System.out.println(maxT +" "+ minT);
    }
}