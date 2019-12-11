package ver01;

public class PhoneBookMain {
	
	public static void main(String[] args) {
		
		// 데이터 저장 : 인스턴스 생성
		PhoneInfor pi_1 = new PhoneInfor("김연아", "010-1212-4545", "1990-12-12");
		pi_1.showInfo();
		
		System.out.println("==========================");
		
		PhoneInfor pi_2 = new PhoneInfor("수지", "010-8269-7868");
		pi_2.showInfo();

	}

}
