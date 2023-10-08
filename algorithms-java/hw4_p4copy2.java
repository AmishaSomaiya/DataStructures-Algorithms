package cse417;

import static java.util.Comparator.comparingInt;
import static java.util.stream.Collectors.toMap;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

//Amisha H Somaiya
//CSE417 HW4-Problem5

public class hw4_p4copy2 {
	
	public static void main(String[] args) {
//      trial			
//		int n = 10; 	
//		double p = 0.5;	
		
		DecimalFormat dec = new DecimalFormat("#0.000");		

		int n = 1000;	
		int numberOfColors = 0;
		int numberOfColorsInc = 0;
		int numberOfColorsDec = 0;		
		int k = 0;
		HashMap<Integer, ArrayList<Integer>> generatedGraph = new HashMap<Integer, ArrayList<Integer>>(n);	
		HashMap<Integer, ArrayList<Integer>> decreasing = new HashMap<Integer, ArrayList<Integer>>(n);	
		HashMap<Integer, ArrayList<Integer>> sorted = new LinkedHashMap<Integer, ArrayList<Integer>>();
		
		
		System.out.println("  p \t\t" + "MaxDepth:k \t" + "#ColorsUsed \t" + "#ColorsUsed \t\t" + "#ColorsUsed");
		System.out.println("                              OriginalOrder\t" + "IncreasingOrder \t" + "DecreasingOrder");
		
//		for(double p = 0.1; p<=0.9; p=p+0.1) {	//testing
		for(double p = 0.002; p<0.022; p=p+0.002) {	
			int sum = 0;
			int sumInc = 0;
			int sumDec = 0;
			
			for (int norm=0; norm<=10; norm++) {
				generatedGraph = hw3_p4.RandomGraphGenerator(n,p);
//				hw3_p4.printGraph(generatedGraph);
				k = hw4_p4.preprocessingFindK(n, generatedGraph);
//				System.out.println(" K:" +k);
				sorted = makeIncreasing(generatedGraph);	
//				hw3_p4.printGraph(sorted);
//				increasing = (HashMap<Integer, ArrayList<Integer>>)sorted;
				decreasing = makeDecreasing(sorted);
				
//				hw3_p4.printGraph(decreasing);
				
				numberOfColors = hw4_p4.graphColoringUsingGreedy(n, generatedGraph, k);
				numberOfColorsInc = hw4_p4.graphColoringUsingGreedy(n, sorted, k);
				numberOfColorsDec = hw4_p4.graphColoringUsingGreedy(n, decreasing, k);
				
					
				sum += numberOfColors;
				sumInc += numberOfColorsInc;
				sumDec += numberOfColorsDec;
			}
			
		
			System.out.println(dec.format(p) + "\t\t" + k + "\t\t" + sum/10 + "\t\t" + sumInc/10 + "\t\t\t" 
					+ sumDec/10);
		}
		
			
	}
	
	
	
	
	
	
	
		//version1: graph in increasing order of vertex depth
	public static HashMap<Integer, ArrayList<Integer>> makeIncreasing (HashMap<Integer, ArrayList<Integer>> generatedGraph ){
	HashMap<Integer, ArrayList<Integer>> sorted = generatedGraph.entrySet().stream()
			    .sorted(comparingInt(e -> e.getValue().size()))
			    .collect(toMap(
			        Map.Entry::getKey,
			        Map.Entry::getValue,
			        (a, b) -> { throw new AssertionError(); },
			        LinkedHashMap::new
			    )); 
		
		return sorted;
	}
	
	//version2: graph in decreasing order of vertex depth
	public static HashMap<Integer, ArrayList<Integer>> makeDecreasing (Map<Integer, ArrayList<Integer>> sorted ){
		// convert to ArrayList of key set
        List<Integer> allKeys = new ArrayList<Integer>(sorted.keySet());
  
        // reverse order of keys
        Collections.reverse(allKeys);
        
        HashMap<Integer, ArrayList<Integer>> reverseSorted = new LinkedHashMap<Integer, ArrayList<Integer>>();
        // iterate sorted using reverse order of keys
        for (Integer currKey : allKeys) {
        	reverseSorted.put(currKey, sorted.get(currKey));
        }
		
		return reverseSorted;
	}

}
