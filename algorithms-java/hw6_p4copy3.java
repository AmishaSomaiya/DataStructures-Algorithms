package cse417;
import java.util.concurrent.ThreadLocalRandom;
import java.util.ArrayList;

//Amisha H. Somaiya
//CSE417 HW6
//Programming Problem Problem 4

public class hw6_p4copy3 {
	
	public static void main(String[] args) {
		
		ArrayList<Integer> trialArray1 = new ArrayList<Integer>();
		
		trialArray1.add(3);   //trail run
		trialArray1.add(1);
		trialArray1.add(9);
		trialArray1.add(4);
		trialArray1.add(6);
		trialArray1.add(8);
		trialArray1.add(5);
		trialArray1.add(2);
		trialArray1.add(7);
		trialArray1.add(10);
		
		
		int n = trialArray1.size();
		int k = 2;
		
		int result = findKthSmallestElement(trialArray1, n, k);
		System.out.println("Implementation of algorithm on textbook pg. 727.");
		System.out.println("Trial Array          :" + trialArray1);
		System.out.println("Testing Value of K   :" + k);
		System.out.println("Kth Smallest Element :" + result);
	}
	
	
	

	//Implementation of algorithm on pg. 727, textbook for finding Kth Smallest Element	
	public static int findKthSmallestElement (ArrayList<Integer> trailArray, int n, int k) {		
		int result = 0;
		int numberOfComparisons = 0;
		int splitter;		
		splitter = ThreadLocalRandom.current().nextInt(0, n);
		int splittingElement = trailArray.get(splitter); //Randomly generating the splitting element 
		ArrayList<Integer> Sminus = new ArrayList<Integer>();
		ArrayList<Integer> Splus = new ArrayList<Integer>();		
		for(int element : trailArray) {			
			if (element < splittingElement) {
				Sminus.add(element);	
				numberOfComparisons +=1;
			} else if (element > splittingElement) {
				Splus.add(element);
				numberOfComparisons +=1;
			}			
		}			
		int l = Sminus.size();		
		if ( l == (k-1)) {
			result = splittingElement;
			return result;
		}
		else if (l >= k) {
			result = findKthSmallestElement(Sminus, l, k);
		}		
		else if (l < (k-1)) {
			result = findKthSmallestElement(Splus, Splus.size(), k-1-l);			
		}		
		return result;			
	}
}
