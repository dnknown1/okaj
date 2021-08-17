import java.util.*;
import java.lang.Math;

public class Sorting{
    public static int binSort(int[] arr,int key,int upper,int lower){
        int mid = Math.round((upper+lower)/2);
        if(arr[mid] == key)
            return mid;
        if(mid == arr.length-1)
            return -1;
        return (arr[mid] < key)?binSort(arr,key,upper,mid):binSort(arr,key,mid,lower);
        
    }
    
}