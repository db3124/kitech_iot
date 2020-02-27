<%@page import="java.net.URL"%>
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
	
		String resourcePath = "/message/notice/notice.txt";
	
	%>
	
	자원의 실제 경로 :
	<%= application.getRealPath(resourcePath) %>
	
	<%
		URL url = application.getResource(resourcePath);
	%>
	
	자원의 참조 URL : <%= url %> <%-- <% url.getHost() %> --%>
	
</body>
</html>