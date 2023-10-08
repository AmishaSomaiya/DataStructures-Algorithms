package cse417;
import java.util.concurrent.ThreadLocalRandom;
import java.util.ArrayList;
//Amisha H. Somaiya
//CSE417 HW6
//Programming Problem Problem 5

public class hw6_p5 {
	public static void main(String[] args) {		
		ArrayList<Integer> nValuesForPlot = new ArrayList<Integer>();
		ArrayList<Double> cValuesForPlot = new ArrayList<Double>();
		double cEstimate = 0.0;
		int countOfn = 0;		
//		for (int i = 50; i<= 1001; i = i+ 50) {     //trial
		for (int i = 50000; i<= 500001; i = i+ 50000) {
			ArrayList<Integer> inputArray = generateS(i);
			int inputSize = inputArray.size();			
			nValuesForPlot.add(i);			
			int k = 0;
			double c = 0.0;
			if (inputSize%2 == 0) {   //n is even
				k = inputSize/2;			}
			else { k = (inputSize+1)/2;}    //n is odd
			for (int j = 0; j<= 500; j++) { //loop for averaging number of comparisons
				int numberOfComparisons=0;
				int comparison = findKthLargestElement(inputArray, inputSize, k, numberOfComparisons);
//				System.out.println("numberOfComparisons : "+ comparison);
				c += comparison;				
			}			
			c/= 500;
			cValuesForPlot.add(c);
			cEstimate += (c/i);
			countOfn += 1;
		}	
		
		
		//output
		System.out.println("n values                     = " + nValuesForPlot );
		System.out.println("Corresponding # Comparisons  = " + cValuesForPlot );
		cEstimate /= countOfn;
		System.out.println("C Estimate                   = " + cEstimate );
	}
	
	//generate S
	public static ArrayList<Integer> generateS (int n){
		ArrayList<Integer> inputArray = new ArrayList<Integer>();
		
		while(inputArray.size() != n) {
			int value = ThreadLocalRandom.current().nextInt(0, 100*n);
			if (! inputArray.contains(value) ) {
				inputArray.add(value);
			}
		}
		return inputArray;		
	}
	
	
	//find median and return number of comparisons
public static int findKthLargestElement (ArrayList<Integer> trailArray, int n, int k, int numberOfComparisons) {
		
		int result = 0;		
		int splitter;
//		System.out.println("Input---"+trailArray.size() + " n:"+n+ " K:"+k);
		splitter = ThreadLocalRandom.current().nextInt(0, n);
//		System.out.println("Splitter: " + splitter);		
		int splittingElement = trailArray.get(splitter);
//		System.out.println("splittingElement: " + splittingElement);
		
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
			return numberOfComparisons;
//			System.out.println("Kth largest element: " + result);
			//break;
		}
		else if (l >= k) {
			return findKthLargestElement(Sminus, l, k,numberOfComparisons);
		}		
		else if (l < (k-1)) {
			return findKthLargestElement(Splus, Splus.size(), k-1-l,numberOfComparisons);			
		}		
		
		return numberOfComparisons;		
			}	
	
}
