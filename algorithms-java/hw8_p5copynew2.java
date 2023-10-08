package cse417;

import java.util.ArrayList;
import java.util.Arrays;

public class hw8_p5copynew2 {
	public static void main(String[] args) {	
		String states[] = {"Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware",
				"District of Columbia","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky",
				"Louisiana","Maine","Maryland","Massachusetts", "Michigan","Minnesota","Mississippi","Missouri","Montana",
				"Nebraska","Nevada","New Hampshire","New Jersey","New Mexico", "New York","North Carolina","North Dakota",
				"Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee",
				"Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"};
		
		int[] electoralVotes2024 = {9,3,11,6,54,10,7,3,3,30,16,4,4,19,11,6,6,8,8,4,10,11,15,10,6,10,4,5,6,4,14,5,28,
				16,3,17,7,8,19,4,9,3,11,40,6,3,13,12,4,10,3};
		
		ArrayList<String> smallestSubset = fewestNumberOfStates(electoralVotes2024, states);
		System.out.println("The fewest states that a candidate could win to reach exactly 269 electoral votes = " 
							+ smallestSubset.size());
		System.out.println("The " + smallestSubset.size() + " states that make the smallest subset leading to 269 votes "
				+ "are as follows: ");
		System.out.println(smallestSubset);
	
	}
		
	
	public static ArrayList<String> fewestNumberOfStates(int[] electoralVotes, String states[]) {
		int K = 269;
		int n = electoralVotes.length;
		long[] opt = new long[K+1];
		boolean[][] use = new boolean[n+1][K+1];
		
		//initialize opt and use arrays
		for(int i =0; i<=n; i++) {      		
			Arrays.fill(use[i], false);	
			Arrays.fill(opt, Integer.MAX_VALUE-1);			
		}
		
		use[0][0] = true;  //base cases
		opt[0] = 0;
	        
	        
        for (int i = 0; i < n; i++) {
            for (int j = K; j >= 1; j--) {
                if (j >= electoralVotes[i]) {   
	                	//System.out.println("i: "+i+" j: "+j+" opt[j] :"+opt[j]+" opt[j-electoralVotes[i]]: 
                				//"+opt[j-electoralVotes[i]]);
                	opt[j] = Math.min(opt[j-electoralVotes[i]]+1, opt[j]);
                	if (opt[j-electoralVotes[i]] < opt[j] ) { //Si element included
                		use[i][j] = true;
                	}
                	//System.out.println("use[i][j]: "+ use[i][j]);
                }
            }
        }

	    int countOfStates = 0;
		int currentSum = 0;  	
		ArrayList<String> subSet = new ArrayList<String>();  
		//beginning from the last cell of boolean tabulation done above	
		int k=K;		
		for(int j=n; j>1; j--) {			
			if(use[j-1][k]) {				
				subSet.add(states[j-1]);
				countOfStates +=1;
				currentSum += electoralVotes[j-1];
//				System.out.println(states[j-1] + electoralVotes[j-1]);
//				System.out.println("currentSum: "+currentSum);
				k-= electoralVotes[j-1];
			}
		}
		
//		System.out.println(currentSum);
		System.out.println(" ");
		return subSet;
		
	}	
}
