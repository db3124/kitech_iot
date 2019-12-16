package ver01;

public class PhoneInfor {
	
	// 이름             name                String
	// 전화번호       phoneNumber         String
	// 생년월일       birthday            String 
	
	public String name;
	public String phoneNumber;// 010-1234-5678
	public String birthday;// 2019-11-12
	
	// 데이터 초기화
	public PhoneInfor(String name, String phoneNumber, String birthday) {
		this.name = name;
		this.phoneNumber = phoneNumber;
	    this.birthday = birthday;
	}
	
	public PhoneInfor(String name, String phoneNumber){// 생성자에서는 오버라이딩 많이 함
		this(name, phoneNumber, null);// 오버로딩 되어 있는 다른 생성자 호출
	}
	
	// 데이터 출력하는 메서드
	public void showInfo() {
		
		System.out.println("이름 : "+name);
		System.out.println("전화번호 : "+phoneNumber);
		
		if(birthday == null) {
			System.out.println("생일 : 입력된 데이터가 없습니다.");
		}else{
			System.out.println("생일 : "+birthday);
		}
		
	}
	
}// end of class
