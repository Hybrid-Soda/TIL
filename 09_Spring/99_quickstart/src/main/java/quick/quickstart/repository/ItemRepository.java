package quick.quickstart.repository;

import org.springframework.stereotype.Repository;
//import org.springframework.data.jpa.repository.JpaRepository;
import quick.quickstart.entity.ItemEntity;

@Repository
public interface ItemRepository {

    void save(ItemEntity itemEntity);

    ThreadLocal<Object> findById(String id);
}
