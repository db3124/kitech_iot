package member;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Repository;

//@Component(value = "memberDao")
@Repository(value = "memberDao")
public class MemberDao { // 위 () 안에 쓰지 않으면 memberDao로 자동등록됨

	private static long nextId = 0;
	private Map<String, Member> map = new HashMap<String, Member>();

	public Member selectByEmail(String email) {
		return map.get(email);
	}

	public void insert(Member member) {
		member.setId(++nextId);
		map.put(member.getEmail(), member);
	}

	public void update(Member member) {
		map.put(member.getEmail(), member);
	}

	public Collection<Member> selectAll() {
		return map.values();
	}

}
