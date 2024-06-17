package user.userManagement.repository;

import user.userManagement.domain.Member;

import jakarta.persistence.EntityManager;
import java.util.List;
import java.util.Optional;

public class JpaMemberRepository implements MemberRepository{

    private final EntityManager em;

    public JpaMemberRepository(EntityManager em) {
        this.em = em;
    }

    @Override
    public Member save(Member member) {
        // Member 엔티티를 데이터베이스에 저장함
        em.persist(member);
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        // ID로 Member 엔티티를 찾음
        Member member = em.find(Member.class, id);
        // 결과를 Optional로 감싸서 반환함
        return Optional.ofNullable(member);
    }

    @Override
    public List<Member> findAll() {
        // 모든 Member 엔티티를 찾는 쿼리를 실행하고 결과 리스트를 반환함
        return em.createQuery("select m from Member m", Member.class)
                .getResultList();
    }

    @Override
    public Optional<Member> findByName(String name) {
        List<Member> result = em.createQuery("select m from Member m where m.name = :name", Member.class)
                // 이름으로 Member 엔티티를 찾는 쿼리를 생성함
                .setParameter("name", name)
                // 쿼리 실행 후 결과 리스트를 받음
                .getResultList();

        // 결과 리스트에서 첫 번째 요소를 Optional로 감싸서 반환함
        return result.stream().findAny();
    }
}
