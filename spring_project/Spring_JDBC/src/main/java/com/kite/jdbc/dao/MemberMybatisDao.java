package com.kite.jdbc.dao;

import java.util.List;

import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.kite.jdbc.domain.Member;
import com.kite.jdbc.domain.RequestMemberReg;

@Repository
public class MemberMybatisDao implements Dao{
	
	@Autowired
	SqlSessionTemplate session;
	
	private String ns = "com.kite.jdbc.mapper.mybatis.MemberMapper";
	
	public List<Member> selectMemberList() {
		// com.kite.jdbc.mapper.mybatis.MemberMapper.selectList
		//List<Member> members = session.selectList(ns + ".selectList");
		
		//return members;
		
		return session.selectList(ns + ".selectList");
	}

	public Object insertMember(RequestMemberReg request) {
		
		return session.insert(ns + ".insertMember", request);
		
	}
	
}
