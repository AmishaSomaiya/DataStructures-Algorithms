package cse417;

import java.util.Random;
import java.text.DecimalFormat;

//Amisha H Somaiya
//CSE417 HW9 Problem 1

public class hw9_p1 {

	public static void main(String[] args) {
		
		int k = 2; 	
		int n = 1000;
		System.out.println("Output value of Chvatal-Sankoff constant across multiple runs of same n:");
		for (int i = 3; i>=0; i--) {			
			System.out.println("For n = " + n);
			System.out.println(" k"+"\t     LCS-length \t  Chvatal-Sankoff Constant");
			findingChvatalSankoffConst(n,k);
		}
		
		System.out.println(" ");
		System.out.println(" ");
		
		System.out.println("Output value of Chvatal-Sankoff constant across multiple runs of different n:");		
		n = 500;
		System.out.println("For n = " + n);
		System.out.println(" k"+"\t     LCS-length \t  Chvatal-Sankoff Constant");
		findingChvatalSankoffConst(n,k);
		n = 2000;
		System.out.println("For n = " + n);
		System.out.println(" k"+"\t     LCS-length \t  Chvatal-Sankoff Constant");
		findingChvatalSankoffConst(n,k);
		n = 3000;
		System.out.println("For n = " + n);
		System.out.println(" k"+"\t     LCS-length \t  Chvatal-Sankoff Constant");
		findingChvatalSankoffConst(n,k);	
		n = 5000;
		System.out.println("For n = " + n);
		System.out.println(" k"+"\t     LCS-length \t  Chvatal-Sankoff Constant");
		findingChvatalSankoffConst(n,k);	
		System.out.println(" ");
		System.out.println(" ");
		
		System.out.println("Output value of Chvatal-Sankoff constant for sufficiently large n:");		
		n = 10000;
		System.out.println("For n = " + n);
		System.out.println(" k"+"\t     LCS-length \t  Chvatal-Sankoff Constant");
		findingChvatalSankoffConst(n,k);	

		
    }
		
	
		
	//Subroutine 1: two n-length strings A and B from the same k-symbol alphabet
	public static String chooseAandB(int n, int k) {
		 
		 Random rand = new Random();
		 StringBuilder newstring = new StringBuilder();
		 int i = 0;
		 while(i<n) {
			 int charac = rand.nextInt(k);
			 newstring.append((char)('a' + charac));
			 i+=1;
		 }		 
		 return newstring.toString();		 
		 
	}
	
	
	//Subroutine 2: finding length of the longest common subsequence of A and B
	public static double longestCommonSubSequence(String A, String B) {
		
        int nA = A.length();
        int nB = B.length();
        
        int[][] opt = new int[nA+1][nB+1];
        
        for (int i = opt.length-2; i >=0 ; i--) {
            for (int j = opt[0].length-2; j >=0 ; j--) {
                if (A.charAt(i) == B.charAt(j)) {
                    opt[i][j] = opt[i+1][j+1] + 1;
                } else {
                	opt[i][j] = Math.max(opt[i+1][j], opt[i][j+1]);
                }
            }
        }
        return (double) opt[0][0];
    }
	
	
	//Subroutine 3: findingChvatalSankoffConst
	public static void findingChvatalSankoffConst(int n, int k) {
		DecimalFormat dec = new DecimalFormat("#0.0000");	
		double lambda = 0.0;
		double ChvatalSankoffConst=1.0;
		double expectation=1.0;
		int averaging = 500;
		int output = 0;
		while (ChvatalSankoffConst >= 2.0/5.0) {
	        double totalLambda = 0.0;
	        for (int i = 0; i < averaging; i++) {
	            String A = chooseAandB(n, k);
	            String B = chooseAandB(n, k);
	            lambda = longestCommonSubSequence(A, B);
	            totalLambda += lambda;
	        }
   
        expectation = totalLambda/averaging;
        ChvatalSankoffConst = expectation / n;
        System.out.println(" " + k + "\t\t" + expectation + "\t\t" + dec.format(ChvatalSankoffConst));
        k+=1;
    }
		output = k-1;
    System.out.println("From the above table, the smallest value of k such that Chvatal-Sankoff Constant < 2/5 is : " +  output);
	}
		
	}
	
	
	

