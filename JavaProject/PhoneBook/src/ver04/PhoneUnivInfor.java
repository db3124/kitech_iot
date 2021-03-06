package ver04;

public class PhoneUnivInfor extends PhoneInfor {

//	주소            address                String
//	전공            major                  String
//	학년            year                   String
	
	String address;
	String major;
	String year; 
	
	/*
	 * public PhoneUnivInfor(String name, String phoneNumber, String email) {
	 * super(name, phoneNumber, email); }
	 */

	public PhoneUnivInfor(String name, String phoneNumber, String email, String address, String major, String year) {
		super(name, phoneNumber, email);
		this.address = address;
		this.major = major;
		this.year = year;
	}

	@Override
	void showInfor() {
		super.showBasicInfor();
		System.out.println("주소 : "+this.address+" 전공 : "+this.major+" 학년 : "+this.year);
	}
	
}
