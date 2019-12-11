package test;

public class ExceptionTest {
	
	public static void main(String[] args) {
		
		int number = 100;
		int result = 0;
		
		for(int i=0; i<10; i++) {
			
			try {
				result = number/(int)(Math.random()*10);
				System.out.println(result);
			}catch(ArithmeticException ae) {// 예외를 처리할 수 있는 인스턴스 생성 후 그곳으로 던짐
//				System.out.println("0으로 나누기를 할 수 없습니다.");
				
//				System.out.println(ae.getMessage());
				
				i--;// 예외가 발생하면 다시 한 번 연산하도록
			}catch(ArrayIndexOutOfBoundsException aie) {
				
			}catch(Exception e) {// 정의되지 않은 나머지 것들. 다형성! 가장 마지막으로 넣기.
				
			}
			
		}
		
	}

}
