package jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class JDBCTest1 {

	public static void main(String[] args) {
		
		Connection conn = null;
		
		try {
			// 1. 드라이버 로드
			Class.forName("oracle.jdbc.driver.OracleDriver");
			System.out.println("오라클 드라이버 로드 완료");
			
			// 호스트, port, db name // 오류 만들어 보기 port, xe, user, pw
			String jdbcUrl = "jdbc:oracle:thin:@localhost:1521:orcl";
			
			// 계정
			String user = "SCOTT";
			// 비밀번호
			String pw = "tiger";
			
			// 2. 데이터베이스에 접속
			conn = DriverManager.getConnection(jdbcUrl, user, pw);
			System.out.println("데이터베이스에 정상적으로 접속되었습니다.");
			
			conn.setAutoCommit(false);// default값은 true
			
			// 3. 데이터의 검색과 변경 처리 : select/DML
			
			// 3.1 insert를 통해 부서정보 입력 처리
			// PreparedStatement 객체 생성 : 객체 생성 시에 sql문을 완성
//			String sql2 = "insert into "
//					+ " dept(deptno, dname, loc)"
//					+ " values (?,?,?)";
//			
//			PreparedStatement pstmt = conn.prepareStatement(sql2);
//			// 데이터 매핑
//			pstmt.setInt(1, 50);
//			pstmt.setString(2, "DEV");
//			pstmt.setString(3, "SEOUL");
//			// insert into dept(deptno, dname, loc) values (50,DEV,SEOUL)
//			
//			int rCNT = pstmt.executeUpdate();
//			
//			if(rCNT > 0) {
//				System.out.println("데이터 입력이 정상 처리되었습니다.");
//			}else {
//				System.out.println("입력이 되지 않았습니다. 관리자에게 문의하세요.");
//			}
			
			// 입력 메서드 호출
			insertDept(conn, 60, "DESIGN", "JEJU");
			insertDept(conn, 70, "DESIGN", null);
			insertDept(conn, 80, null, null);
			
			listDept(conn);
			
			conn.commit();
			
			
					
//			// 3.2 dept 테이블의 내용 출력
//			// Statement 객체 생성
//			Statement stmt = conn.createStatement();
//			
//			String sql1 = "select * from dept";
//			
//			ResultSet rs = stmt.executeQuery(sql1);
//			
//			while(rs.next()) {
//				
////				int deptno = rs.getInt("deptno");
////				String dname = rs.getString("dname");
////				String loc = rs.getString("loc");
//				
//				int deptno = rs.getInt(1);
//				String dname = rs.getString(2);
//				String loc = rs.getString(3);
//				
//				System.out.println(deptno+" | "+dname+" | "+loc);
//				
//			}
//			
//			rs.close();
//			stmt.close();
//			pstmt.close();		
			
			conn.close();
			
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (SQLException e) {
			
			try {
				conn.rollback();
			} catch (Exception e1) {
				e1.printStackTrace();
			}
			
			e.printStackTrace();
			// System.out.println("입력 오류");
		}	
			
	}// end of main
	
	// 부서정보 리스트 출력
	
	public static void listDept(Connection conn) throws SQLException {
		
		Statement stmt = conn.createStatement();
		
		String sql1 = "select * from dept";
		
		ResultSet rs = stmt.executeQuery(sql1);
		
		System.out.println("부서(DEPT) 리스트");
		System.out.println("======================");
		
		while(rs.next()) {
			
//			int deptno = rs.getsInt("deptno");
//			String dname = rs.getString("dname");
//			String loc = rs.getString("loc");
			
			int deptno = rs.getInt(1);
			String dname = rs.getString(2);
			String loc = rs.getString(3);
			
			System.out.println(deptno+" | "+dname+" | "+loc);
			
		}
		
		System.out.println("-----------------------");
		
		rs.close();
		stmt.close();
		
	}// end of listDept
	
	// DB의 DEPT에 부서정보 입력
	public static void insertDept(
			Connection conn,
			int deptno, 
			String dname,
			String loc) throws SQLException {
		
		String sql = "insert into "
				+ " dept(deptno, dname, loc)"
				+ " values(?,?,?)";
		// PreparedStatement
		PreparedStatement pstmt = conn.prepareStatement(sql);
		// mapping
		pstmt.setInt(1, deptno);
		pstmt.setString(2, dname);
		pstmt.setString(3, loc);
		// executeUpdate
		int rCNT = pstmt.executeUpdate();
		
		if(rCNT > 0) {
			System.out.println("데이터 입력이 정상 처리되었습니다.");
		}else {
			System.out.println("입력이 되지 않았습니다. 관리자에게 문의하세요.");
		}
		// pstmt.close
		pstmt.close();
		
	}// end of insertDept
	
}// end of class