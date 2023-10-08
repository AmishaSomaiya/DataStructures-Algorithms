package cse417;

public class hw8_p4copy {
	public static void main(String[] args) {
		
		
		String states[] = {"Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware",
				"District of Columbia","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky",
				"Louisiana","Maine","Maryland","Massachusetts", "Michigan","Minnesota","Mississippi","Missouri","Montana",
				"Nebraska","Nevada","New Hampshire","New Jersey","New Mexico", "New York","North Carolina","North Dakota",
				"Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee",
				"Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"};
		
		long[] electoralVotes2024 = {9,3,11,6,54,10,7,3,3,30,16,4,4,19,11,6,6,8,8,4,10,11,15,10,6,10,4,5,6,4,14,5,28,
				16,3,17,7,8,19,4,9,3,11,40,6,3,13,12,4,10,3};
		
		
		System.out.println("The number of ways for 269-269 tie: " + numberOfWaysFor269Tie(states, electoralVotes2024));
			}
	
	
	
	
	public static long numberOfWaysFor269Tie (String states[], long[] eVotes){
		
		long numberOfWays = 0;
		int n = eVotes.length;
		int K = 269;
		long[][] opt = new long[n+1][K+1];
				
//case1 : when there are no elements(states) in the set i.e. j=0 and when target sum is 0 i.e. k=0 =>
//then there is only 1 possibility of empty set resulting into 0 target so opt[j][k] = 1
//case2 : when there is a non-zero target sum(k!=0) but if there are no elements in the set i.e. j=0 =>
//then there is no possibility reaching the target sum so opt[j][k] = 0
//case3 : when there are elements present in the set but the target sum is 0 i.e. k=0 =>
//then the target sum of 0 can be achieved by 1 possibility that all elements are excluded in the solution so opt[j][k]=1
//case4 : when there are elements present in the set and the target sum is non-zero, the target sum may or may not be
//reached by the elements
		
		for(int j = 0; j < n+1; j++) {
			for(int k=0; k < K+1; k++) {			
				
				if (j==0 & k==0) opt[j][k] = 1;  //case1
				else if (j== 0) opt[j][k] = 0;   //case2
				else if (k==0) opt[j][k] = 1;    //case3
				
				else {                           //case4
					
					if (eVotes[j-1] > k) {
						opt[j][k] = opt[j-1][k];
					}
					else {
						opt[j][k] = opt[j-1][k] + opt[j-1][(int)(k-eVotes[j-1])];
					}		
					
				}	
//				System.out.println("j: "+ j + "k: " + k + "opt(j,k): " +opt[j][k]);	
		} 			
		}		
		numberOfWays = opt[n][K]; //total number of ways for 269 votes
		return numberOfWays/2;    //divide by 2 to find number of ways for 269-269 tie
	}
}
