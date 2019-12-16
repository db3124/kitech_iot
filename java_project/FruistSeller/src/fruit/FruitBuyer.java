package fruit;

public class FruitBuyer {
	// 상탯값 : 보유금액, 사과의 개수
//	int myMoney = 10000;	// 보유금액 : 초기값 10000
//	int numofApple = 0;		// 보유한 사과의 개수 : 기본값 0 
	int myMoney;	// 보유금액 : 초기값 10000
	private int numofApple;		// 보유한 사과의 개수 : 기본값 0 
	
	public FruitBuyer(int money){
		myMoney = money;
//		numofApple = 0;
	}
	
	// 기능 : 구매, 구매 현황
	
	// 구매 : 구매할 셀러, 구매할 금액 -> 셀러에게 판매 요청(금액) -> 반환 받은 사과의 개수로 사과의 개수 변경 -> 보유 금액 변경
	public void buyApple(FruitSeller seller, int money) {
		// 구매한 사과의 개수
		int num = seller.saleApple(money);
		//numofApple = numofApple + num;
		numofApple += num; // 사과의 개수 변경 처리
		myMoney -= money;  // 보유 금액 변경
	}
	
	// 구매 현황
	public void showBuyResult() {
		System.out.println("현재 보유금액 : " + myMoney);
		System.out.println("사과의 개수 : " + numofApple);
	}

}// end of class
