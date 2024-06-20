package quick.quickstart.service;

import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import quick.quickstart.dto.ItemDto;
import quick.quickstart.entity.ItemEntity;
import quick.quickstart.mapper.QuickMapper;
import quick.quickstart.repository.ItemRepository;

import java.util.HashMap;

@Service
@Slf4j
public class QuickService {

    @Autowired
    private QuickMapper quickMapper;

    @Autowired
    private ItemRepository itemRepository;

    public boolean registerItem(ItemDto itemDto) {
        // TODO: DB insert

        ItemEntity itemEntity = new ItemEntity();
        itemEntity.setId(itemDto.getId());
        itemEntity.setName(itemDto.getName());

        itemRepository.save(itemEntity);

        return true;
    }

    public ItemDto getItemById(String id) {

//        ItemEntity itemEntity = itemRepository.findById(id).get();

        ItemDto itemDto = new ItemDto();

//        itemDto.setId(itemEntity.getId());
//        itemDto.setName(itemEntity.getName());


        return itemDto;
    }
}
