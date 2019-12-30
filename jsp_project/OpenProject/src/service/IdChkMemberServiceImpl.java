package service;

import java.io.IOException;
import java.sql.Connection;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import dao.MemberDao;
import jdbc.ConnectionProvider;

@WebServlet("/IdChkMemberServiceImpl")
public class IdChkMemberServiceImpl extends HttpServlet {
	
	String viewPage = "/WEB-INF/views/idChk.jsp";
	
	String uid = ;
	
	String result = "Y";
	
	// DB -> id로 검색한 결과가 있다면  result="N"
	
	MemberDao dao = new MemberDao();
	
	Connection conn = null;
	
	try {
		
		conn= ConnectionProvider.getConnection();
		
		boolean chk = dao.selectCheckId(conn, uid);
		
		if(!chk) {
			result = "N";
		}
		
	} catch(SQLException e) {
		e.printStackTrace();
	}
	
	request.setAttribute("result", result);
	
	return viewPage;
		
}
