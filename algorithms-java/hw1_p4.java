package cse417;

import java.util.Stack;
import java.util.Arrays;

public class hw1_p4 {
	
	public static void main(String[] args) {
		
			//Test Case 1: 
			//int[][] M = {{2, 0, 1}, {2, 0, 1}, {2, 1, 0}};
			//int[][] W = {{2, 0, 1}, {0, 2, 1}, {2, 0, 1}};
			
			//Test Case 2: 
			//int[][] M = {{3, 1, 0, 2}, {3, 0, 1, 2}, {3, 1, 2, 0}, {0, 3, 2, 1}};
			//int[][] W = {{3, 0, 2, 1}, {3, 1, 2, 0}, {0, 1, 3, 2}, {3, 0, 2, 1}};	
			
			//Test Case 3: 
		    //int[][] M = {{1, 3, 0, 2}, {3, 0, 2, 1}, {2, 3, 1, 0}, {2, 0, 3, 1}}			
		    //int[][] W = {{1, 2, 0, 3}, {0, 3, 2, 1}, {1, 2, 3, 0}, {0, 1, 2, 3}};	
			
			//Test Case 4: 
			//int[][] M = {{4, 2, 0, 1, 3}, {0, 1, 4, 2, 3}, {4, 0, 1, 3, 2}, {1, 4, 3, 0, 2}, {0, 1, 3, 4, 2}};
			//int[][] W = {{2, 3, 4, 0, 1}, {2, 4, 0, 3, 1}, {1, 4, 2, 3, 0}, {3, 0, 1, 4, 2}, {0, 3, 1, 2, 4}};	
			
			//Test Case for HW1-P4
			int[][] M = {{2, 1, 3, 0}, {0, 1, 3, 2}, {0, 1, 2, 3}, {0, 1, 2, 3}};
			int[][] W = {{0, 2, 1, 3}, {2, 0, 3, 1}, {3, 2, 1, 0}, {2, 3, 1, 0}};
			
			//Pre-processing Step 
			//to have O(1) lookup of ms in w's preference list during algorithm processing
			int[][] WPreferenceLookup = RevereseMatching(W); 
		
			int[] output = GaleShapleyAlgorithm(M, W, WPreferenceLookup);
			
			System.out.println(" "		);	
			System.out.println("Output:" + Arrays.toString(output));	
			int size = output.length;
			String finalMatching = " ";
			for (int i = 0; i<size; i++) {
				finalMatching += "m"+i+"w"+output[i]+" ";				
			}
			System.out.println("Final Matching:" + finalMatching);
			
		
	}
	
		
	public static int[] GaleShapleyAlgorithm( int[][] M, int[][] W, int[][]WPreferenceLookup) {
		
		int[][] Mdash = new int[M.length][M.length]; //to keep track of proposed ws in m's preference list
		
		Stack<Integer> stack = new Stack<Integer>(); //to keep track of free ms
		int k=0;  //pointer for top priority unproposed w in m's preference list
		int w;    //top priority unproposed w
		int size = M[0].length;
		
		
		//Declaring arrays for algorithm processing		
		int[] finalOutput =  new int[size];              
		int[] matchingForW = new int[size];              
		int[] isWFree =  new int[size];                  
		
		//initializing above declared arrays with -1 to indicate not yet matched    
		for (int i=0; i<size; i++) {
			finalOutput[i] = -1;        
			matchingForW[i] = -1;       
			isWFree[i] = -1;           
		}


//		INITIAL CASE: all m in M are free: push all m in M to stack 
//		System.out.println("Initial Stack contents:");
		for(int i = 0; i<M.length; i++) {
			stack.push(i);
//			System.out.print(stack.peek());			
		}
	
		int currentM = 0;
		int previousM = 0;
		
//		System.out.println("List of Proposals performed by the algorithm:");
		//Algorithm terminates when stack is empty i.e. all m in M are perfectly matched 
		while(!stack.isEmpty()) {
			
				int i = stack.pop();  //pop m_i to be matched
				k = 0;
				
				//M[i][k] == -2 indicates visited w_i, so go to next w in m's list
				while (Mdash[i][k] == -2) {   
					k++;
				}
				
				w = M[i][k];    //top priority, unproposed w in m_i's list
				Mdash[i][k] = -2;   //mark this w in m_i's preference list as visited
				if (isWFree[w] == -1) {  //if this w is free i.e. unmatched, then match it with m_i
//					System.out.println(i + " proposes to " + w + " [" + w +",-1] Accepted");
					isWFree[w] = 1;      //mark this w as matched 
					finalOutput[i] = w;  //put this w in index i i.e. (m,w) pair
					matchingForW[w] = i; //intermediate matching for W
				} else { 
					//compare priority of current m to previously matched m in w_i's preference list
					currentM = i;
					previousM = matchingForW[w];
					if (WPreferenceLookup[w][currentM] < WPreferenceLookup[w][previousM]) {	
						//current m accepted
						//previous m unmatched, push to stack
						if(!stack.contains(matchingForW[w])) {//							
							stack.push(matchingForW[w]);
						}
						
//						System.out.println(i + " proposes to " + w + " [" + w +","+matchingForW[w]+ "] Accepted");
						matchingForW[w] = i;
						finalOutput[i] = w;
						Mdash[i][k] = -2; //mark this w in m_i's preference list as visited		
						
						
					} else {
						//previous matching remains
						//current m rejected, push to stack
//						System.out.println(i + " proposes to " + w + " [" + w +","+matchingForW[w]+ "] Rejected");
						Mdash[i][k] = -2;            //mark this w in m_i's preference list as visited
						if(!stack.contains(i)) { //push unmatched m to stack
							stack.push(i);
						}
																	
					}
					
				}
				
				
		}
		
		
		
		//Algorithm terminates when all m in M are perfectly matched i.e. when stack is empty
		//The final matching is perfectly matched and stable, return the final matching:		
		return finalOutput;
		
	}

	
	
	public static int[][] RevereseMatching (int[][] W) {
		int size = W.length;
		int[][] WPreferenceLookup = new int [size][size];
		
		for (int i = 0; i < size; i++) {
			for(int j=0; j<W[0].length; j++) {
				int temp = W[i][j];
				WPreferenceLookup[i][temp] = j;				
			}					
		}
		return WPreferenceLookup;
		
	}
	

}	

