package ver04;

import java.util.Scanner;

// 기능 클래스
public class PhoneBookManager {

	// 객체 100개를 저장 : PhoneInfor 타입의 배열 생성, 사이즈 : 100개
	// 객체 생성 -> 배열에 객체 저장
	//        -> 대학친구 객체, 회사친구 객체 : 메뉴 구성
	// 배열에서 검색 -> 검색 결과 출력
	// 배열에서 검색 -> 객체 삭제
	// 배열에서 전체 리스트 출력
	
	// 배열 생성
	PhoneInfor[] pBook;
	
	// 추가한 데이터의 개수
	int cnt;
	
	// 콘솔 입력
	Scanner sc; 
	
	// ★★싱글톤 패턴 : 인스턴스를 단 1개만 생성하여 사용하도록 처리 <--------- 기능만 갖고 있는 클래스의 경우 보통 싱글콘 패턴
	// 1. 다른 객체에서 인스턴스 생성을 막는다. -> 생성자에 private 적용
	// 2. 인스턴스 자신이 인스턴스를 생성해준다.
	// 3. 외부에서 생성된 참조변수를 호출할 수 있는 메서드를 생성
	
	public static PhoneBookManager getInstance(){// 3.
		
		if(m == null) {
			return new PhoneBookManager();
		}else {
			return m;
		}
		
	}
	
	private static PhoneBookManager m = new PhoneBookManager();// 1. private 2.
	private PhoneBookManager(){
		pBook = new PhoneInfor[100];// 생성자 이용해서 배열 생성. 수정, 구조 바꿀 때 유연하게 대처 가능
		sc = new Scanner(System.in);
	}
	
	// 입력 -> 대학 or 회사
	// 대학친구 입력 -> 1, 회사친구 입력 -> 2
	// 검색 -> 3, 삭제 -> 4
	void insertInfor(int select) {
		
		if(!(select == 1 || select == 2)) {
			System.out.println("올바른 메뉴 선택이 아닙니다. 다시 선택해 주세요");
			return;
		}
		
		// 기본 정보 입력받고
		System.out.println("이름을 입력해주세요.");
		String name = sc.nextLine();
		System.out.println("전화번호를 입력해주세요.");
		String phoneNumber = sc.nextLine();
		System.out.println("이메일을 입력해주세요.");
		String email = sc.nextLine();
		
		// 1 또는 2에 따라 입력 받고 ->인스턴스 생성 -> 배열에 저장
		
		// 배열에 저장될 참조변수
		PhoneInfor pi = null;
		
		if(select == 1) {
			
			System.out.println("주소를 입력해주세요.");
			String address = sc.nextLine();
			System.out.println("전공을 입력해주세요.");
			String major = sc.nextLine();
			System.out.println("학년을 입력해주세요.");
			String year = sc.nextLine();
			
			pi = new PhoneUnivInfor(name, phoneNumber, email, address, major, year);
			
		}else{
			
			System.out.println("회사를 입력해주세요.");
			String company = sc.nextLine();
			
			pi = new PhoneCompanyInfor(name, phoneNumber, email, company);
			
		}
		
		pBook[cnt++] = pi;
		
		System.out.println("저장되었습니다.");
		
//		pBook[cnt-1].showBasicInfor();
//		System.out.println("======================");
//		pBook[cnt-1].showInfor();
		 
		
	}// end of insertInfor
	
	// 이름을 기준으로 개별에서 index 찾아 반환
	int searchIndex(String name) {
		
		int index = -1;// 찾지 못했을 때 반환값은 -1로 정의
		
		// 배열을 통해 이름 검색 : 반복문 이용
		
		for(int i=0; i<cnt; i++) {
			if(pBook[i].name.equals(name)) {
				index = i;
				break;
			}
		}
		
		return index;
	}

	// 이름을 통해 검색한 결과의 정보를 출력
	void searchInfor() {
		
		System.out.println("검색하고자 하는 이름을 입력해주세요.");
		String name = sc.nextLine();
		
		// index 검색
		int index = searchIndex(name);
		
		if(index<0) {
			
			System.out.println("찾으시는 이름의 정보가 없습니다.");
			
		}else{
			
			pBook[index].showInfor();
			
		}
		
	}

	void deleteInfor() {
		System.out.println("삭제하고자 하는 이름을 입력해주세요.");
		String name = sc.nextLine();
		
		// index 검색
		int index = searchIndex(name);
		
		try {
			for(int i=index; i<cnt-1; i++) {
				pBook[i] = pBook[i+1];
			}
		// 전채 개수에서 -1
			cnt--;
			System.out.println("삭제되었습니다.");
		}catch(ArrayIndexOutOfBoundsException e){
			System.out.println("찾으시는 이름의 정보가 존재하지 않습니다.");
		}
	}
	
	// 배열에 저장된 전체 데이터 출력
	void showAll() {
		
		System.out.println("친구 리스트");
		System.out.println("---------------------");
		
		for(int i=0; i<cnt; i++) {
			pBook[i].showBasicInfor();
			System.out.println("---------------------");
		}
		
	}
	
}// end of class

