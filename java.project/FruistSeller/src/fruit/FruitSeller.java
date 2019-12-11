package fruit;

public class FruitSeller {
	
	// seller의 상탯값 : 사과의 개수, 판매금액, 사과의 가격 --> 변수
//	int numofApple = 20;		  // 사과의 개수
//	int myMoney = 0;			 // 판매금액
//	final int APPLE_PRICE = 1000;// 사과 1개의 가격
	
	private int numofApple;		  // 사과의 개수
	private int myMoney;			 // 판매금액
	final int APPLE_PRICE;
	
    // 생성자 만들기
	// 이름은 클래스이름과 동일하게, 메서드와 같이 매개변수를 정의할 수 있다.
	// return이 없다. 반환형 타입을 정의하지 않는다.
	// 인스턴스 형성 시 단 1번 실행한다. -> 멤버변수의 초기화할 때 사용한다. : 초기화 메서드
	// 디폴트 생성자는 생략 가능
	
	public FruitSeller(int numofApple, int myMoney, int price){// 파란색 인스턴스 변수, 갈색 지역 변수
		this.numofApple = numofApple;
		this.myMoney = myMoney;
		APPLE_PRICE = price;
	}
	
	public FruitSeller(FruitSeller fs) {
		this.numofApple = fs.numofApple;
		this.myMoney = fs.myMoney;
		this.APPLE_PRICE = fs.APPLE_PRICE;
	}
	
	public FruitSeller() {// this 사용 -> 중복 방지
		this(20, 0, 500);// this : 다른 생성자 호출, 호출의 기준 : (매개변수)
	}
	
	// 기능 : 판매, 판매 데이터 출력

	// 판매 기능 : 돈을 받고 -> 사과 개수 계산 -> 사과의 개수 변경 -> 돈의 수치 변경 -> 사과의 개수 반환
	int saleApple(int money) {
		// 판매할 사과의 개수
		int num = money/APPLE_PRICE;
		numofApple = numofApple - num;// 보유한 사과의 개수 변경
		myMoney = myMoney + money;// 보유한 돈의 데이터 변경
		
		return num;
	}
	
	// 판매 데이터 결과 출력
	public void showSaleResult() {//반환, 리턴 모두 없음
		System.out.println("남은 사과의 개수 : " + numofApple);//문자열+int -> 문자열+문자열
		System.out.println("판매 수익 :" + myMoney);
	}
	

}//end of class
