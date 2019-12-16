package shop;

public class Product {
	
	int price;
	int bonusPoint;
	
	public Product(int price) {
		this.price = price;
		this.bonusPoint = (int)(price/10f);
	}
	
	public static void main(String[] args) {
		
		Buyer b = new Buyer();
		
		Tv tv = new Tv(100);
		Product p1 = tv;
		
		Computer com = new Computer(300);
		Product p2 = com;
		
		Audio aud = new Audio(50);
		Product p3 = aud;
		
		b.buy(tv);
		b.buy(com);
		b.buy(aud);
		
		b.summary();
		
		System.out.println("================================");
		System.out.println("현재 남은 돈 : "+b.money);
		System.out.println("현재 보너스 포인트 : "+b.bonusPoint);
		
	}
	
}

class Audio extends Product{

	public Audio(int price) {
		super(price);
	}

	@Override
	public String toString() {
		return "Audio";
	}
	
}

class Tv extends Product{

	public Tv(int price) {
		super(price);
	}

	@Override
	public String toString() {// @Override<-어노테이션 Java의 문법은X. 부수적인 의미 부여. Spring 등 특정 프레임워크에서는 추가적인 속성 정의 등등 가능
		return "Tv";
	}
	
}

class Computer extends Product{

	public Computer(int price) {
		super(price);
	}

	@Override
	public String toString() {
		return "Computer";
	}
	
}

class Buyer {
	
	int money = 1000;
	int bonusPoint = 0;
	
	// 장바구니
	Product[] cart = new Product[10];
	// 구매 상품의 개수, 배열에 입력할 때 index 값으로 사용, 반복문 사용 시 반복의 조건 
	int cnt = 0;
	
	void buy(Product p) {
		
		if(money<p.price) {
			System.out.println("잔액이 부족해 구매할 수 없습니다.");
			return;// 메서드의 종료
		}
		
		money = money - p.price;
		bonusPoint = bonusPoint + p.bonusPoint;
		
		// 바구니에 추가
		cart[cnt++] = p;
		// 구매 상품의 개수1 증가
//		cnt++;
		
		System.out.println(p+"을/를 구입했습니다.");
		
	}
	
	void summary(){
		// 구매 상품의 총 금액
		int sum = 0;
		// 구매 제품 리스트
		String productList ="";
		
		for(int i=0; i<cnt; i++) {
			// 제품 가격을 더한다.
			sum += cart[i].price;
			// 제품리스트
			productList += cart[i] +", ";
		}
		
		System.out.println("구입한 제품의 총 금액 : "+sum+"만원입니다.");
		System.out.println("구입한 제품의 목록 : " +productList+"입니다.");
	}
	
}// end of buyer
