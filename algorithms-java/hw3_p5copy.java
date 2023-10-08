package cse417;

import java.util.AbstractQueue;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Queue;
import java.util.LinkedList;
import java.lang.Math;


import cse417.hw3_p4;


//Amisha H Somaiya
//HW3-Programming Problem 5


public class hw3_p5copy {

	public static void main(String[] args) {
		
		int n = 10;
		double p = 0.9;
		double[] output = new double[3];
		
		HashMap<Integer, ArrayList<Integer>> inputGraph = new HashMap<Integer, ArrayList<Integer>>(n);
			
		
		inputGraph = hw3_p4.RandomGraphGenerator(n,p);
		hw3_p4.printGraph(inputGraph);
		
		
		output = graphDiameter(n, inputGraph);
		System.out.println("For n:" +n+ " p:" +p+ " Graph Diameter:" + output[0] +
				" Finite Diameter:" + output[1] + "Largest Connected Component: " + output[2]);
				
			

	}
	
	public static double[] graphDiameter (int n, HashMap<Integer, ArrayList<Integer>> inputGraph ) {
		Queue<Integer> queue = new LinkedList<Integer>();	
		int[] checkVisited = new int[n];	
		int u = 0, level = 0, connectedComponent = 0;
		double finiteDiameter = 0.0;
		double graphDiameter = 0.0;
		int largestConnectedComponent = 0;
		double[] output = new double[3];
		
		for (int i = 0; i<n; i++) {
			queue.add(i);
			checkVisited[i] = 1;
			
			while(!queue.isEmpty()) {
				 u = queue.poll();
				 if (checkVisited[u] == -1) {
					 ArrayList<Integer> currentNeighbors = inputGraph.get(u);
					 level += 1;
//					 System.out.println("level");
					 for (int neighbor : currentNeighbors) {
						 if(checkVisited[neighbor] == -1) {
							 queue.add(neighbor);
							 connectedComponent += 1;
							 checkVisited[neighbor] = 1;
						 }
					 }
				 }
				 
				 finiteDiameter = level;
				 if (connectedComponent == 0) {
					 finiteDiameter = Double.POSITIVE_INFINITY;
				 }
				 largestConnectedComponent = Math.max(largestConnectedComponent, connectedComponent);
			}
		
			graphDiameter = Math.max(graphDiameter, finiteDiameter);
		}
		
		output[0] = graphDiameter;
		output[1] = finiteDiameter;
		output[2] = largestConnectedComponent;
		
		return output;
		
	}

}
