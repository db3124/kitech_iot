package jdbc;

import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;

public class Loader extends HttpServlet {

	@Override
	public void init(ServletConfig config) throws ServletException {
		
		String jdbcDriver = config.getInitParameter("jdbcDriver");
		
		/* 데이터베이스 드라이버 로드 */
		try {
			Class.forName(jdbcDriver);
			System.out.println("데이터베이스 드라이버 로드 성공");
		} catch (ClassNotFoundException cne) {
			System.out.println("데이터베이스 드라이버 로드 실패");
			cne.printStackTrace();
		}
	}

}// end of class
