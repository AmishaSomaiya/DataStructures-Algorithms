package cse417;

import java.text.DecimalFormat;
import java.util.concurrent.ThreadLocalRandom;

public class hw2_p4Averaging {

public static void main(String[] args) {		
		
		double avgc = 0.0;
		
		DecimalFormat dec = new DecimalFormat("#0.0000");
		
		System.out.println(" n"+"\t  C"+"\t  C/n");
		for(int n = 200; n<4001 ; n=n+200) {     
			
			double averagingC = 0.0;	
			
			//loop for several tries on n
			//to decrease variance in results
			for(int z = 0; z<10; z++) {    
				averagingC += checkCoupon(n);
				
			}		
				averagingC /= 10;
				avgc = averagingC/n;

				String formattedn = String.format("%04d", n);
				System.out.println(formattedn+"\t"+ (int)averagingC+"\t"+dec.format(avgc));
		}
	}

	//coupon collection
	public static double checkCoupon (int n) {
		int min = 1;
		int max = n;
		int i = n;
		double c = 0.0;
		int[] checkCouponType = new int[n+1];
		
		while (i !=0 ) {
			//coupon of random type between 1 and n
			int currentCoupon = ThreadLocalRandom.current().nextInt(min, max + 1);
				
			if (checkCouponType[currentCoupon] != -1) {
				i--;
				checkCouponType[currentCoupon] = -1;
				c+=1;
				
			}else {
				c+=1; //
				}					
		}
		
		//return total coupons collected		
		return c;
		
	}

}

