<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>회원 가입 폼에서 전송한 파라미터 출력</title>
<script
  src="https://code.jquery.com/jquery-1.12.4.js"
  integrity="sha256-Qw82+bXyGq6MydymqBxNPYTaUXXq7c8v3CwiYwLLNXU="
  crossorigin="anonymous">
</script>
<style>

	* {
		margin : 0;
		padding : 0;
	}
	
</style>
</head>
<body>

	<h1>회원 가입 폼에서 전송한 파라미터 값</h1>
	<%
		
		// 한글 인코딩 : 데이터 베이스에 전송할 때 애초에 데이터가 깨져있으면 안 됨!
		request.setCharacterEncoding("UTF-8");
	
		// 데이터 받아 출력하기
		// 데이터 받기 : 무조건 내장객체 request
		
		String uid = request.getParameter("uid");
		String pw = request.getParameter("pw");
		String uname = request.getParameter("uname");
		String gender = request.getParameter("gender");
		String byear = request.getParameter("byear");
		
	%>
	
	아이디 : <%= uid %> <br>
	비밀번호 : <%= pw %> <br>
	이름 : <%= uname %> <br>
	성별 : <%= gender.equals("w") ? "여자" : "남자" %> <br>
	출생년도 : <%= byear %>

</body>
</html>