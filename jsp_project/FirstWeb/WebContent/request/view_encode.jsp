<%@page import="java.net.URLDecoder"%>
<%@page import="java.net.URLEncoder"%>
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
		
		String name = "홍길동";
		String encodedStr = URLEncoder.encode(name, "UTF-8");
	
		response.sendRedirect("view.jsp?name="+encodedStr);
		
		String decodedName = URLDecoder.decode(name, "UTF-8");

	 %>
	 
	 <%= decodedName %>


</body>
</html>