package cse417;

import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

//Amisha H Somaiya
//CSE417 - HW4-Problem4
//GraphColoring using Greedy Algorithm

public class hw4_p4 {

	public static void main(String[] args) {
		
		DecimalFormat dec = new DecimalFormat("#0.000");	
		
		int n = 1000;
//		int n = 10;      //testing
//		double p = 0.5;  //testing
//		System.out.println("for n: "+ n + " p: " + p + " numberofcolors used: " + numberOfColors);
		
		int numberOfColors = 0;
		int k = 0;
		HashMap<Integer, ArrayList<Integer>> generatedGraph = new HashMap<Integer, ArrayList<Integer>>(n);		
		System.out.println("Graph Coloring for n = 1000 using Greedy Algorithm:");
		System.out.println(" ");
		System.out.println("Results with normalization: ");
		System.out.println("  p \t\t" + "MaxDepth:k \t" + "#ColorsUsed");
		for(double p = 0.002; p<0.022; p=p+0.002) {	
			int sum = 0;
			for (int norm=0; norm<=10; norm++) {
				generatedGraph = hw3_p4.RandomGraphGenerator(n,p);
				k = preprocessingFindK(n, generatedGraph);
				numberOfColors = graphColoringUsingGreedy(n, generatedGraph, k);
				sum+=numberOfColors;
			}			
			sum/=10;			
			System.out.println(dec.format(p) + "\t\t" + k + "\t\t" + sum);		
		}
		
		
		
		
	}
	
	
	
	//Graph Coloring using Greedy Algorithm
	public static <T extends HashMap<Integer, ArrayList<Integer>>> int graphColoringUsingGreedy(int n, T generatedGraph, int k) {
		int numberOfColors = 0;
		int[] colors = new int[k+1];            //total number of colors available = k+1
		int[] markVerticesColored = new int[n];	
		int u = 0;
		int assignColor = 0;
		
		Arrays.fill(colors, -1);   //colors used will be mark as +1, unused colors are marked as -1
		Arrays.fill(markVerticesColored, -1); //vertices yet to be colored are marked as -1
		                                      //after a vertex is colored, the color number is assigned as value 
		                                      //index of markVerticesColored = vertex number = assigned value of color
		
//		for(int i = 0; i< n; i++) {
		for(int i:generatedGraph.keySet()) {
			
			Queue<Integer> queue = new LinkedList<Integer>();
			queue.add(i);			
			
			while (!queue.isEmpty()) {
				
				u = queue.poll();
				ArrayList<Integer> currentNeighhbors = generatedGraph.get(u);  //neighbors of current node
				if(currentNeighhbors != null) {
					
					ArrayList<Integer> colorsOfNeighbors = new ArrayList<Integer>(currentNeighhbors.size());
					//changed to list to use .contains()
					
					for (int e : currentNeighhbors) {
						colorsOfNeighbors.add(markVerticesColored[e]);     //find colors of current neighbors
						
					}
					
					for (int z=0; z<k+1; z++) {                         //assign first color unused by neighbors
						if (!colorsOfNeighbors.contains(z)){
							assignColor = z;
							break;					
						}
					}			
				}else {
					assignColor = 0;
				}
				markVerticesColored[i] = assignColor;
				colors[assignColor] = 1;
				
				
			}
			

			
		}	
		
		for (int l : colors) {    //total count of colors used
			if (l != -1) {
				numberOfColors +=1;
			}
		}
		
		return numberOfColors;		
	}
	
	//pre-processing subroutine to calculate k: maximum depth of graph
	public static <T extends HashMap<Integer, ArrayList<Integer>>> int preprocessingFindK (int n, T generatedGraph) {
	int k =0;
	int currentDepth = 0;
	for(int i = 0; i<n; i++) {
		currentDepth = generatedGraph.get(i).size();
//		System.out.println("currentDepth" +  currentDepth);
//		System.out.println("current k" +  k);
		if (currentDepth > k) {
			k = currentDepth;
		}				
	}
	
//	System.out.println("final k before returning" +  k);
	 return k;
	}
	
}
