package com.kite.domain;

import java.sql.Date; // 1970.01.01 00:00:00 ~ 현재 시간까지의 시간 : long타입의 밀리초 반환

public class Member {
	
	private int id;
	private String email;
	private String password;
	private String name;
	private Date regdate;
	
	public Member() {
		
	}
	
	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Date getRegdate() {
		return regdate;
	}

	public void setRegdate(Date regdate) {
		this.regdate = regdate;
	}

	@Override
	public String toString() {
		return "Member [id=" + id + ", email=" + email + ", password=" + password + ", name=" + name + ", regdate="
				+ regdate + "]";
	}
	
	
	
	
}
