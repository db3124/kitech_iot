<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
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

	<%
		String uid = request.getParameter("uid");
		String pw = request.getParameter("pw");
		
		if(uid != null && pw != null && uid.equals(pw)){
			response.sendRedirect("../index.html");
		} else {
	%>
		<h1>아이디 또는 비밀번호가 틀렸습니다. 확인해주세요.</h1>
	<% } %>


</body>
</html>