package cse417;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.concurrent.ThreadLocalRandom;
//CSE417 HW7 Problem 4 and Problem 5

//Approach : 
//For a particular interval, inserted corresponding start time, finish time, value and value density in 4 different treemaps
//Sorted treemaps of start time and finish time in ascending order
//Sorted intervals of value and value density in descending order

//Now consider problem 4b : we want to sort intervals by start time and use greedy approach on these intervals.
//EntrySet method is then used on sorted treemap with start time 
//Intervals sorted based on start time are the keys of start time tree map which are accessed by index
//This key is the interval number
//Now, accessing value from other treemaps such as finish time treemap and value treemap by this key
//This will give corresponding finish time and value for this interval.
//So, we can now access start time, finish time, value and value density of all intervals sorted by start time for problem 4b 
//These are further processed in their respective subroutines to check overlap and proceed 


//Similarly, for problem 4c, entryset on treemap sorted by value is made and same process as above is followed.
//Similarly, for problem 4d, entryset on treemap sorted by value density is made and same process as above is followed.

//Checked this approach on smaller values of n = 5 and 10, it is working correctly

//Similarly for dynamic programming approach, above accessing process for treemap sorted by FINISH TIME is working correctly
//Dynamic programming output is NOT CORRECT
//Some indexing issue in dynamic programming subroutine or predececessor calculation subroutine 
//Debugged for n = 10, unable to locate the issue. 


public class hw7_p4 {
	
	public static void main(String[] args) {
		
		int n = 10000;
		List<TreeMap<Integer, Double>> generatedIntervals = randomIntervalGenerator(n);
	
//		System.out.println(generatedIntervals.toString());
//		System.out.println(generatedIntervals.get(0).toString());
//		System.out.println(generatedIntervals.get(1).toString());
//		System.out.println(generatedIntervals.get(2).toString());
//		System.out.println(generatedIntervals.get(3).toString());
//		System.out.println(sortedByFinishTime.toString());
//		System.out.println(sortedByValue.toString());
//		System.out.println(sortedByValueDensity.toString());
		
		//problem 4b
		double[] output = greedyApproach1(generatedIntervals.get(0), generatedIntervals.get(1), generatedIntervals.get(2), n);
		System.out.println("for n = "+ n + "part b:, number of intervals: "+ output[0] + "max value " + output[1]);
		
		//problem 4c
		double[] output1 = greedyApproach2(generatedIntervals.get(0), generatedIntervals.get(1), generatedIntervals.get(2), n);
		System.out.println("for n = "+ n + "part c:, number of intervals: "+ output1[0] + "max value " + output1[1]);
		
		//problem 4d
		double[] output2 = greedyApproach3(generatedIntervals.get(0), generatedIntervals.get(1), generatedIntervals.get(2),
				generatedIntervals.get(3), n);
		System.out.println("for n = "+ n + "part d:, number of intervals: "+ output2[0] + "max value " + output2[1]);
	}
	


	
	public static List<TreeMap<Integer, Double>> randomIntervalGenerator (int n){
		
		List<TreeMap<Integer, Double>> list = new ArrayList<TreeMap<Integer,Double>>();
		TreeMap<Integer, Double> sortedByStartTime = new TreeMap<Integer, Double>();
		TreeMap<Integer, Double> sortedByFinishTime = new TreeMap<Integer, Double>();
		TreeMap<Integer, Double> sortedByValue = new TreeMap<Integer, Double>();
		TreeMap<Integer, Double> sortedByValueDensity = new TreeMap<Integer, Double>();
		
		int L = 1000000;
		int r = 2000;
		int v = 100;
		
//		int L = 1;  //testing
//		int r = 1;  //testing
//		int v = 1;  //testing	
		
//		int L = 10;  //testing
//		int r = 10;
//		int v = 10;
		
		
		int i = 0;
		
		while(i<=n) {
			double currentStartTime = ThreadLocalRandom.current().nextInt(1, L + 1);	
			//System.out.println("start =" + currentStartTime);
			double currentLength = ThreadLocalRandom.current().nextInt(1, r + 1);
			//System.out.println("length =" + currentLength);
			double currentFinishTime = currentStartTime + currentLength;
			//System.out.println("finish =" + currentFinishTime);
			double currentValue = ThreadLocalRandom.current().nextInt(1, v+1);
			double currentValueDensity = currentValue/currentLength;
			
			sortedByStartTime.put(i, currentStartTime);
			sortedByFinishTime.put(i, currentFinishTime);
			//System.out.println("finishtime put to sortedByFinishTime" + sortedByFinishTime.get(i));
			sortedByValue.put(i, currentValue);
			sortedByValueDensity.put(i, currentValueDensity);
			
			i+= 1;
		}
		
		list.add((TreeMap<Integer, Double>) valueSortAsc(sortedByStartTime));
		list.add((TreeMap<Integer, Double>) valueSortAsc(sortedByFinishTime));
		list.add((TreeMap<Integer, Double>) valueSortDsc(sortedByValue));
		list.add((TreeMap<Integer, Double>) valueSortDsc(sortedByValueDensity));
		
		
		return list;
		
	}
	
	//problem 4b
	public static double[] greedyApproach1 (TreeMap<Integer, Double> sortedByStartTime, 
			TreeMap<Integer, Double> sortedByFinishTime, 
			TreeMap<Integer, Double> sortedByValue, int n){
		
		
		Set<Map.Entry<Integer, Double> > entrySet = sortedByStartTime.entrySet();
		Map.Entry<Integer, Double>[] entryArray = entrySet.toArray(new Map.Entry[entrySet.size()]);
		
				
		double[] output = new double[2];
		int countOfIntervals = 1;  //adding the first interval
		Integer test = entryArray[0].getKey();
		
		//HashMap<Integer, Double> sortedByValueMap = sortedByValue;
		double maximizedValue = getValueFromMap(sortedByValue,test);; //adding the value of the first interval
		//double maximizedValue = 0;
		
	
		int i = 2;	//start checking if intervals are overlapping or not from second interval
		//non-overlapping condition: current interval start time is more than previous interval finish time 
		//AND
		//current interval finish time is less than next interval start time
		
		
		while (i < n+1) {
			
			if (i==n-1) {
				
				//if ((entryArray[i].getValue() > sortedByFinishTime.get(entryArray[i-1].getKey()))){
				  if ((entryArray[i].getValue() > getValueFromMap(sortedByFinishTime,entryArray[i-1].getKey()))){
					countOfIntervals +=1;
					//maximizedValue += sortedByValue.get(entryArray[i].getKey());
					maximizedValue += getValueFromMap(sortedByValue,entryArray[i].getKey());
				}
				
			}else {
//				if ((entryArray[i].getValue() > sortedByFinishTime.get(entryArray[i-1].getKey())) && 
//						((sortedByFinishTime.get(entryArray[i].getKey()) < entryArray[i+1].getValue()))){
				if (entryArray[i].getValue() > getValueFromMap(sortedByFinishTime,entryArray[i-1].getKey())){
					countOfIntervals +=1;
					//maximizedValue += sortedByValue.get(entryArray[i].getKey());
					maximizedValue += getValueFromMap(sortedByValue,entryArray[i].getKey());
				}			
			}	
			
			i+=1;
			
		}
		
		
		output[0] = countOfIntervals; //number of intervals
		output[1] = maximizedValue;
		
		return output;	
		
	}
	
	//problem 4c
	public static double[] greedyApproach2 (TreeMap<Integer, Double> sortedByStartTime, 
			TreeMap<Integer, Double> sortedByFinishTime, 
			TreeMap<Integer, Double> sortedByValue, int n){
		
		
		Set<Map.Entry<Integer, Double> > entrySet = sortedByValue.entrySet();
		Map.Entry<Integer, Double>[] entryArray = entrySet.toArray(new Map.Entry[entrySet.size()]);
		
				
		double[] output = new double[2];
		int countOfIntervals = 1;  //adding the first interval
		Integer test = entryArray[0].getKey();
		
		double maximizedValue = getValueFromMap(sortedByValue,test); //adding the value of the first interval
		//double maximizedValue = 0;
		
	
		int i = 2;	//start checking if intervals are overlapping or not from second interval
		//non-overlapping condition: current interval start time is more than previous interval finish time 
		//AND
		//current interval finish time is less than next interval start time
		
		
		while (i < n) {
			

				
				//if ((entryArray[i].getValue() > sortedByFinishTime.get(entryArray[i-1].getKey()))){
				  if (getValueFromMap(sortedByStartTime,entryArray[i].getKey()) > getValueFromMap(sortedByFinishTime,entryArray[i-1].getKey())){
					countOfIntervals +=1;
					//maximizedValue += sortedByValue.get(entryArray[i].getKey());
					maximizedValue += getValueFromMap(sortedByValue,entryArray[i].getKey());
				}
				
		
			i+=1;
			
		}
		
		
		output[0] = countOfIntervals; //number of intervals
		output[1] = maximizedValue;
		
		return output;	
		
	}
	
	//problem 4d
		public static double[] greedyApproach3 (TreeMap<Integer, Double> sortedByStartTime, 
				TreeMap<Integer, Double> sortedByFinishTime, 
				TreeMap<Integer, Double> sortedByValue, TreeMap<Integer, Double> sortedByMaxValue,  int n){
			
			
			Set<Map.Entry<Integer, Double> > entrySet = sortedByMaxValue.entrySet();
			Map.Entry<Integer, Double>[] entryArray = entrySet.toArray(new Map.Entry[entrySet.size()]);
			
					
			double[] output = new double[2];
			int countOfIntervals = 1;  //adding the first interval
			Integer test = entryArray[0].getKey();
			
			double maximizedValue = getValueFromMap(sortedByValue,test); //adding the value of the first interval
			//double maximizedValue = 0;
			
		
			int i = 2;	//start checking if intervals are overlapping or not from second interval
			//non-overlapping condition: current interval start time is more than previous interval finish time 
			//AND
			//current interval finish time is less than next interval start time
			
			
			while (i < n) {
				
					//if ((entryArray[i].getValue() > sortedByFinishTime.get(entryArray[i-1].getKey()))){
					  if (getValueFromMap(sortedByStartTime,entryArray[i].getKey()) > getValueFromMap(sortedByFinishTime,entryArray[i-1].getKey())){
						countOfIntervals +=1;
						//maximizedValue += sortedByValue.get(entryArray[i].getKey());
						maximizedValue += getValueFromMap(sortedByValue,entryArray[i].getKey());
					}
	
				
				i+=1;
				
			}
			
			
			output[0] = countOfIntervals; //number of intervals
			output[1] = maximizedValue;
			
			return output;	
			
		}
	
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


	public static <K, V extends Comparable<V>> Map<K, V> valueSortAsc(final Map<K, V> map) {
		// Static Method with return type Map and
		// extending comparator class which compares values
		// associated with two keys
		Comparator<K> valueComparator = new Comparator<K>() {

			// return comparison results of values of
			// two keys
			public int compare(K k1, K k2) {
				int comp = map.get(k1).compareTo(map.get(k2));
				if (comp == 0)
                    return 1;
                else
                    return comp;
			}

		};

		// SortedMap created using the comparator
		Map<K, V> sorted = new TreeMap<K, V>(valueComparator);
		
		sorted.putAll(map);
		//System.out.println(sorted.size());
		return sorted;
	}
	
	public static <K, V extends Comparable<V>> Map<K, V> valueSortDsc(final Map<K, V> map) {
		// Static Method with return type Map and
		// extending comparator class which compares values
		// associated with two keys
		Comparator<K> valueComparator = new Comparator<K>() {

			// return comparison results of values of
			// two keys
			public int compare(K k1, K k2) {
				int comp = map.get(k2).compareTo(map.get(k1));
				if (comp == 0)
                    return 1;
                else
                    return comp;
			}

		};

		// SortedMap created using the comparator
		Map<K, V> sorted = new TreeMap<K, V>(valueComparator);
		sorted.putAll(map);
		return sorted;
	}

}
