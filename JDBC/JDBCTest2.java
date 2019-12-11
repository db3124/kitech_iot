package jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class JDBCTest2 {

	public static void main(String[] args) {
		
		Connection conn = null;
		
		try {
			// 드라이버 로드
			Class.forName("com.mysql.jdbc.Driver");
			System.out.println("MySQL 드라이버 로드 완료");
			
			// ?serverTimezone 8버전인 경우 서버타임을 UTC로 할 수 있도록 설정
			String jdbcUrl = "jdbc:mysql://localhost:3306/project?serverTimezone=UTC";
			String user = "kite"; // root
			String pw = "111111"; // admin
			
			conn = DriverManager.getConnection(jdbcUrl, user, pw);
			
			System.out.println("데이터베이스에 접속했습니다.");
			
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}

}

