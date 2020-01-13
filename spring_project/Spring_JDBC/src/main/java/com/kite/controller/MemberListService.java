package com.kite.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.kite.domain.Member;
import com.kite.jdbc.dao.MemberDao;

@Service
public class MemberListService {

	@Autowired
	MemberDao dao;
	
	public List<Member> getMemberList() {
		List<Member> members = dao.getMemberList();
		
		return members;
	}
}
