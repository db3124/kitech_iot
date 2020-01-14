package com.kite.jdbc.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.kite.jdbc.dao.MemberDao;
import com.kite.jdbc.dao.MemberMybatisDao;
import com.kite.jdbc.domain.RequestMemberReg;

@Service
public class MemberRegService {
	
	@Autowired	
	MemberDao dao;
	
	@Autowired
	MemberMybatisDao mDao;
	
	public int regMember(RequestMemberReg request) {
		return dao.insertMember(request);
		//return dao.insert(request);
	}

	public Object registMember(RequestMemberReg request) {

		return mDao.insertMember(request);
	}

}
