<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%@ page trimDirectiveWhitespaces="true" %>
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
	
	
	<!--
		memberInfo member = (memberInfo)request.getAttribute("member");
		
		memberInfo member = new memberInfo(); 
		request.setAttribute("member", member);
	-->
	
	<jsp:useBean id="member" class="member.MemberInfo" scope="request"/>
	<jsp:setProperty property="*" name="member"/>
	
	<%= member %>
	
	<%-- <%
		member.setUname("kim");
	%>
	
	<%= member.getByear() %> : <%= member.getUname() %> --%>
	
	<jsp:useBean id="loginInfo" class="member.LoginInfo" scope="session"/>
	
	<%
		loginInfo.setId("queen@naver.com");
	%>
	
	<%= loginInfo %>
	
</body>
</html>