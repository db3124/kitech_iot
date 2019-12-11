package test;

public class MyRullet {
	
	public static void main(String[] arg) {
		String[] name = {
				"고현주","구자윤","김난형","김동진","김주연","문영기","박준섭","박지은"
				,"방창용","양햇살","엄예빈","위은주","이용재","황다울","이진형","이택수"
				,"장한솔","정엄지","정용기","조성빈","조지윤","최찬영","하재운","홍지수"	
		};
		
		String temp = "";
		
		for(int i = 0; i<=10000; i++) {
			int ran1 = (int)(Math.random()*24);
			int ran2 = (int)(Math.random()*24);
			
			temp = name[ran1];
			name[ran1] = name[ran2];
			name[ran2] = temp;
		}

		System.out.println(temp+" 이/가 반장입니다.");

	}// end of main
	
}// end of class
