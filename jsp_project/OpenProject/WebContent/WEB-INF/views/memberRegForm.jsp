<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>

<head>
	<meta charset="UTF-8">
	
    <title>회원가입</title>
        
    <script
  		src="https://code.jquery.com/jquery-1.12.4.js"
 		integrity="sha256-Qw82+bXyGq6MydymqBxNPYTaUXXq7c8v3CwiYwLLNXU="
 		crossorigin="anonymous">
    </script>
    
  
    <link rel="stylesheet" href="default.css">
    
    <style>
        
        select.byear {
            width : 200px;
            height : 30px;
            
            font-size: 1.3em;
        }
  	
  		#nav>li{
  			float : 
  		}
  		
  		.color_red {
  			color : red;
  		}
  		
  		.color_blue {
  			color : blue;
  		}
    </style>
        
</head>

<body>

    <h1 class="title">회원가입</h1>
    <hr>
    <form action="reg" method="post">
        <table class="inputBox">
            <tr>
                <td>아이디(이메일)</td>
                <td>
                	<input type="text" name="uid" id="uid">
                	<span id="idchk_msg"></span>
                </td>
            </tr>
            <tr>
                <td>비밀번호</td>
                <td>
                	<input type="password" name="pw" id="pw">
                </td>
            </tr>
            <tr>
                <td>이름</td>
                <td>
                	<input type="text" name="uname" id="uname">
                </td>
            </tr>
            <tr>
                <td>성별</td>
                <td>
                	남 <input type="radio" name="gender" value="m">
                	여 <input type="radio" name="gender" value="w">
                </td>
            </tr>
            <tr>
                <td>출생년도</td>
                <td>
                    <select id="byear" class="byear" name="byear">
                        
                    </select>
                </td>
            </tr>
            <tr>
                <td>프로필 사진</td>
                <td>
                    <input type="file" name="pfile">
                </td>
            </tr>
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="회원가입">
                </td>
            </tr>
        </table>
    </form>
    
    <script>
		
    	$(document).ready(function(){
    		
    		var selectOptions = '';
    		
    		for(var i=2019; i>=1950; i--) {
				selectOptions +='<option value="'+i+'">'+i+'</option>\n';    			
    		}
    		
    		$('#byear').html(selectOptions);
    		
    		$('#uid').focusin(function(){
    			
    			$(this).val('');
    			$('#idchk_msg').text('');
    			
    		});
    		
    		$('#uid').focusout(function(){
    			// alert("focusout 이벤트");
    			
    			var param = $(this).val();
    			
    			// 비동기 통신 : id 값을 전송 후  Y 또는 N의 값을 받는 통신 
    			$.ajax({
    				url : 'idChk', // 'op/member/idChk'
    				type : 'get',
    				data : {uid:param},
    				success : function(data){
    					// Y or N
    					// alert(data);
    					$('#idchk_msg').removeClass('color_blue');
    					$('#idchk_msg').removeClass('color_red');
    					
    					if(data=='Y'){
    						$('#idchk_msg').text('사용가능한 아이디(이메일)입니다');
    						$('#ichk_msg').addClass('color_blue');
    					}else {
    						$('#idchk_msg').text('사용 불가한 아이디(이메일)입니다');
    						$('#idchk_msg').addClass('color_red');
    					}
    				}
    			});
    			
    		});
    		
    	});
    
    </script>

</body>

</html>