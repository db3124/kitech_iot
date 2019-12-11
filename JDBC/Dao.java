package jdbc;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

// CRUD : 생성Create 검색Research 수정Update 삭제Delete

// Data Access Object : 데이터베이스에 있는 데이터 조작을 위한 클래스
public class Dao {
	
	// 싱글톤 패턴으로 인스턴스 생성을 제한
		
	// 1. 생성자 호출을 막아서 인스턴스 생성을 막는다.
	private Dao() { }
		
	// 2. 사용할 인스턴스를 생성
	private static Dao dao = new Dao(); // Dao.dao = null;
	
	// 3. 외부 참조용 메서드 : 인스턴스를 반환해주는 메서드
	public static Dao getInstance() {
		return dao;
	}
	
	// 부서 정보 리스트 출력
	public void listDept(Connection conn) throws SQLException {
		
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
			
			rs.close();
			stmt.close();

		}
		
	}// end of listDept
	
	// DB의 DEPT에 부서정보 입력
	public void insertDept(Connection conn, int deptno, String dname, String loc) throws SQLException {
			
		String sql = "insert into "
					+ " dept(deptno, dname, loc)"
					+ " values (?,?,?)";
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
	
	// 부서 정보 수정
	// 부서 이름, 부서위치, 부서 선택의 조건 부서번호(PK)
	public void editDept(Connection conn, int deptno, String dname, String loc) throws SQLException {
		
		String sql = "update dept set dname=?, loc=? where deptno=?";
		PreparedStatement pstmt = conn.prepareStatement(sql);
		pstmt.setString(1, dname);
		pstmt.setString(2, loc);
		pstmt.setInt(3, deptno);
		int rCNT = pstmt.executeUpdate();
			
		if(rCNT > 0) {
			System.out.println("수정되었습니다.");
		}else {
			System.out.println("찾으시는 데이터가 존재하지 않습니다.");
		}
		
	}// end of editDept
	
	// 부서 정보 삭제
	// 부서 번호로 삭제 대상 선택
	public void deleteDept(Connection conn, int deptno) throws SQLException {
		
		String sql = "delete from dept where deptno=?"+deptno;
		Statement stmt = conn.createStatement();
		
		int rCNT = stmt.executeUpdate(sql);
		
		if(rCNT > 0) {
			System.out.println("삭제되었습니다.");
		}else {
			System.out.println("삭제하고자 하는 데이터가 존재하지 않습니다.");
		}
		
		stmt.close();
		
	}// end of deleteDept
	
	// 부서 번호로 부서 정보 검색, 부서 정보를 출력
	public void searchDept(Connection conn, int deptno) throws SQLException{
		
		String sql = "select * from dept where deptno=?";
		PreparedStatement pstmt = conn.prepareStatement(sql);		
		pstmt.setInt(1, deptno);
		
		ResultSet rs = pstmt.executeQuery();
		
		if(rs.next()) {// 0 또는 1 : deptno가 PK이기 때문에
			System.out.println("찾으시는 "+deptno+"번 부서의 정보입니다.");
			System.out.println("--------------------------------");
			System.out.println(rs.getInt("deptno")+" | "+rs.getString("dname")+" | "+rs.getString("loc"));
		}else {
			System.out.println("찾으시는 부서의 정보가 존재하지 않습니다.");
		}
		
		rs.close();
		pstmt.close();
		
	}
	
}
