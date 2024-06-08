package user.userManagement.repository;

import user.userManagement.domain.Member;

import java.util.*;

public class MemoryMemberRepository implements MemberRepository {

    // 회원 정보를 저장하는 HashMap, key는 회원 ID, value는 회원 객체
    private static Map<Long, Member> store = new HashMap<>();
    // 회원 ID 생성을 위한 시퀀스 변수, 회원이 추가될 때마다 증가
    private static long sequence = 0L;

    @Override
    public Member save(Member member) {
        // 회원 객체에 고유 ID 할당
        member.setId(++sequence);
        // 회원 정보를 store에 저장
        store.put(member.getId(), member);
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        // ID로 회원을 찾고, 결과를 Optional로 감싸서 반환
        return Optional.ofNullable(store.get(id));
    }

    @Override
    public Optional<Member> findByName(String name) {
        // 이름으로 회원을 찾고, 결과를 Optional로 감싸서 반환
        return store.values().stream()
                .filter(member -> member.getName().equals(name))
                .findAny();
    }

    @Override
    public List<Member> findAll() {
        // 모든 회원 정보를 List 형태로 반환
        return new ArrayList<>(store.values());
    }

    public void clearStore() {
        store.clear();
    }
}
