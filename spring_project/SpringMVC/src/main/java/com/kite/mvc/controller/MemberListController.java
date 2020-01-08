package com.kite.mvc.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class MemberListController {

	@RequestMapping("/member/list")
	public String list() {
		return "member/list";
	}
	
	@RequestMapping("/member/search")
	public String search() {
		return "member/search";
	}
	
	@ModelAttribute("searchOptions")
	public List<String> optionList(){
		
		List<String> options = new ArrayList<String>();
		
		options.add("아이디");
		options.add("이름");
		options.add("아이디+이름");
		
		return options;
	}
	
}
