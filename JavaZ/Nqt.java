import java.util.*;
//import java.lang.Math;
public class Nqt{
    public static void main(String [] arg){
        int n=9;
        int x = 0;
        int [] a = new int[n];
        Scanner sc = new Scanner(System.in);
        
        try {for(int i=0;i<n;i++) a[i] = sc.nextInt();}
        catch (Exception e){
            System.out.println("Invalid Input");
            return;
        }
       
        a[0] = Math.round((a[0]+a[3]+a[6])/3);
        a[1] = Math.round((a[1]+a[4]+a[7])/3);
        a[2] = Math.round((a[2]+a[5]+a[8])/3);
         
         
         x = a[0]>a[1]?0:1;
         x =x>a[2]?x:2;
         x = (int) x;
         
         if(x<70) System.out.println("all weak");
         else{
             for(int i=0;i<3;i++){
                 if (a[i] == a[x]) System.out.println("winner:"+(i+1));
             }
        }
    }    
}