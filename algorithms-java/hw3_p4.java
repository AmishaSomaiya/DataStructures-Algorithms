package cse417;

import java.util.HashMap;
import java.util.ArrayList;
import java.util.Random;


//Amisha H Somaiya
//HW3-Programming Problem 4
//Random Graph Generator using Edge Density Model

public class hw3_p4 {
	
	public static void main(String[] args) {
		
		//given values of n and p
		int n = 10;
		double p = 1;
		
		HashMap<Integer, ArrayList<Integer>> generatedGraph = new HashMap<Integer, ArrayList<Integer>>(n);
	
		
		System.out.println("For n=10, p=0.2");
		System.out.println("Generated Graph 1:");
		generatedGraph = RandomGraphGenerator(n,p);
		printGraph(generatedGraph);
		
		System.out.println(" ");
		System.out.println("Generated Graph 2:");
		generatedGraph = RandomGraphGenerator(n,p);
		printGraph(generatedGraph);		
	}

	
	//RandomGraphGenerator using Edge Density Model
	public static HashMap<Integer, ArrayList<Integer>> RandomGraphGenerator (int n, double p){
		
		HashMap<Integer, ArrayList<Integer>> generatedGraph = new HashMap<Integer, ArrayList<Integer>>(n);
		Random rd = new Random();
				
		for(int i=0; i<n-1; i++) {
			if (!generatedGraph.containsKey(i)) {
				generatedGraph.put(i, new ArrayList<Integer>());
			}			
			for (int j = i+1; j<n; j++) {
				if (!generatedGraph.containsKey(j)) {
					generatedGraph.put(j, new ArrayList<Integer>());
				}	
				if (rd.nextDouble() < p) {
					generatedGraph.get(i).add(j);
					generatedGraph.get(j).add(i);
				}
			}
		}						
		//System.out.println(generatedGraph.toString());	
		return generatedGraph;		
	}
	
	
		
	//Subroutine to print the generated graph
	public static <T extends HashMap<Integer, ArrayList<Integer>>> void printGraph (T generatedGraph) {
		System.out.println("Node \t" + "Edges");
		for(HashMap.Entry<Integer, ArrayList<Integer>> entry : generatedGraph.entrySet()) {
			System.out.println(entry.getKey() + "\t" + entry.getValue().toString());
		}		
	}	
}
