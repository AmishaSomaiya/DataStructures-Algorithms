package cse417;

import java.text.DecimalFormat;
import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;


public class hw2_p5Averaging {
public static void main(String[] args) {
		
		double avgV = 0.0;		
		
		DecimalFormat dec = new DecimalFormat("#0.0000");	

		
		System.out.println(" n"+"\t\t  V"+"\t\t  V/n");
		for(int n = 200; n<4001 ; n=n+200) {
			
			double averagingV = 0.0;
			
			//loop for several tries on n
			//to decrease variance in results			
			for(int z = 0; z<10; z++) {
				averagingV += sumMinValue(n);
				
			}
				averagingV /= 10;
				avgV = averagingV/n;

				
				String formattedn = String.format("%04d", n);
				System.out.println(formattedn+"     \t"+ (int)averagingV+"     \t"+dec.format(avgV));
		}		
		 
	}

	//coupon collection with minimum value
	public static double sumMinValue(int n) {
		double V = 0.0;
		int[] checkCouponType = new int[n+1];
		//to store minimum value of each coupon type
		double[] minValue = new double[n+1]; 
		Arrays.fill(minValue, n);
		int min = 1;
		int max = n;
		int i = n;
			while (i !=0 ) {
				//coupon of random type between 1 and n
				int currentCoupon = ThreadLocalRandom.current().nextInt(min, max + 1);
				//check if coupon of this type collected
				if (checkCouponType[currentCoupon] != -1) {
					i--;
					checkCouponType[currentCoupon] = -1;
				}
				//value of coupon : random integer between 1 and n
				double couponValue = ThreadLocalRandom.current().nextInt(min, max + 1);
				//collect coupon of minimum value for each coupon type
				minValue[currentCoupon] = Math.min(minValue[currentCoupon], couponValue);	
			}			
			
			for(int j=1; j<=n; j++) {
				V += minValue[j];
			}
			
			//return value of coupons collected
			return V;
		
	}


}
