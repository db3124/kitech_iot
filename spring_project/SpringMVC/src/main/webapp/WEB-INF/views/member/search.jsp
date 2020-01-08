<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h1>회원 검색</h1>
	검색 : ${searchOptions}
	
	<br><br>
	
	<c:forEach items="${searchOptions}" var="option">
		${option} <br>
	</c:forEach>
</body>
</html>