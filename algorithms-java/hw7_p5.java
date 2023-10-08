package cse417;

import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;

public class hw7_p5 {
	
	public static void main(String[] args) {
		
		int n = 10000;
		
		for(int i = 1; i<11; i++) {
		//problem 4
		System.out.println("For n = 10,000, L = 1,000,000, r  = 2,000, v = 100");	
		System.out.println("For run number : " + i);
		List<TreeMap<Integer, Double>> generatedIntervals = hw7_p4.randomIntervalGenerator(n);
		
		
		double[] output1 = hw7_p4.greedyApproach1(generatedIntervals.get(0), generatedIntervals.get(1), generatedIntervals.get(2), n);
		System.out.println("        Algorithm 4b: number of intervals: "+ output1[0] + " max value " + output1[1]);
		
		double[] output2 = hw7_p4.greedyApproach2(generatedIntervals.get(0), generatedIntervals.get(1), generatedIntervals.get(2), n);
		System.out.println( "        Algorithm 4c: number of intervals: "+ output2[0] + " max value " + output2[1]);
		
		double[] output3 = hw7_p4.greedyApproach3(generatedIntervals.get(0), generatedIntervals.get(1), generatedIntervals.get(2),
				generatedIntervals.get(3), n);
		System.out.println( "        Algorithm 4d: number of intervals: "+ output3[0] + " max value " + output3[1]);
		
		
		//problem 5
		int[] P = calculatePredecessor(generatedIntervals,n);
//		for(int i:p) {
//			System.out.println("i: "+i);
//		}
		
		double[] output4 = dpApproach(generatedIntervals.get(0), generatedIntervals.get(1), generatedIntervals.get(2),
		generatedIntervals.get(3), P , n);
		System.out.println("        Algorithm DP: number of intervals: "+ output4[0] + "max value " + output4[1]);
		
		}
		
	}
	
	//pre-processing: predecessor calculation
	public static int[] calculatePredecessor(List<TreeMap<Integer, Double>> generatedIntervals, int n) {
		
		TreeMap<Integer, Double> sortedByStartTime = generatedIntervals.get(0);
		TreeMap<Integer, Double> sortedByFinishTime = generatedIntervals.get(1);
		Set<Map.Entry<Integer, Double> > entrySet = sortedByFinishTime.entrySet();
		Map.Entry<Integer, Double>[] entryArray = entrySet.toArray(new Map.Entry[entrySet.size()]);
						
		Integer test = entryArray[0].getKey();
		
		int[] P = new int[n+1]; // predecessor array
		P[test] = 0;

		// for current interval i:
		// if finish time of previous interval (i-1) is < start time of interval i
		// then predecessor of interval i = interval (i-1)
		// else check if interval (i-2) is the predecessor
		// repeat till predecessor set for current interval

		int i = 1;
		boolean gotPred = false;
		while (i < n) {
			gotPred = false;
			int j=1;
			while (!gotPred) {				
				if (getValueFromMap(sortedByFinishTime,entryArray[i - j].getKey()) < getValueFromMap(sortedByStartTime,entryArray[i].getKey())) {
					P[i] = entryArray[i - j].getKey();
					gotPred = true;
					break;
				}else {
					j++;
					if(i-j <0) {
						P[i] = 0;
						gotPred = true;
						break;
					}
				}
			}
			i += 1;
		}
		return P;
		}	
		
//		while (i < n) {
//
//			int j = 0;
//			gotPred = false;
//
//			while (!gotPred) {
//
//				if (i == 0) {
//					P[0] = 0;
//					gotPred = true;
//				}
//
//				else {
//					j = i - 1;
//					if ((j - 1) >= 0) {
//					//if (generatedIntervals[1][i - 1] < generatedIntervals[0][i]) {
//						if (getValueFromMap(sortedByFinishTime,i - 1) < getValueFromMap(sortedByStartTime, test)) {
//							P[i] = i - 1;
//							gotPred = true;
//							break;
//						}
//					}else {
//						P[i] = 0;
//						gotPred = true;
//					}
//					
//				}	
//			}
//
//			i += 1;
//		}

	
	
	private static Double getValueFromMap(TreeMap<Integer, Double> map, Integer test) {
        // Get an iterator
        Iterator i = map.entrySet().iterator();	  
        while (i.hasNext())
        {
            Map.Entry mp = (Map.Entry)i.next();
            if(mp.getKey().equals(test)) {
            	return (Double) mp.getValue();
            }
        }
        
        return 0.0;
	
}
	

	//dynamic programming sub-routine
	public static double[] dpApproach(TreeMap<Integer, Double> sortedByStartTime, 
			TreeMap<Integer, Double> sortedByFinishTime, 
			TreeMap<Integer, Double> sortedByValue, TreeMap<Integer, Double> sortedByMaxValue, int[] P, int n){
		
		Set<Map.Entry<Integer, Double>> entrySet = sortedByFinishTime.entrySet();
		Map.Entry<Integer, Double>[] entryArray = entrySet.toArray(new Map.Entry[entrySet.size()]);
		
				
		double[] output = new double[2];
		int countOfIntervals = 1;  //adding the first interval
		Integer test = entryArray[0].getKey();
		
		double[] M = new double[n+1];
		M[0] = getValueFromMap(sortedByValue,test); //adding the value of the first interval
//		double maximizedValue = M[0];
		
		
		//M[0] = 0;
		double v1 = 0;
		double v2 = 0;
		
		for (int j = 1; j< n+1; j++) {
			
			
			v1 = M[entryArray[j-1].getKey()];
			v2 = getValueFromMap(sortedByValue,entryArray[j].getKey()) + M[P[entryArray[j].getKey()]];
			
			if (v1>v2) {
				M[entryArray[j].getKey()] = v1;
			}else {
				M[entryArray[j].getKey()] = v2;
				countOfIntervals +=1;
			}
		}
		output[0] = countOfIntervals;
		output[1] = M[n]; 
		return output;
	}
			
		

	
}
