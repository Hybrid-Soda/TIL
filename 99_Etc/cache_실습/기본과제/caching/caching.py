import csv
import time
import threading
import os

class CafeMenuCache:
    def __init__(self, filename):
        self.filename = filename
        self.cache = None
        self.last_updated = None
        self.lock = threading.Lock()
        self.initialize_file()

    def initialize_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='', encoding='UTF-8') as file:
                writer = csv.writer(file)
                writer.writerow(["아메리카노"])  # 초기 데이터 저장
        print(f"{self.filename} 파일이 초기화되었습니다.")

    def read_from_file(self):
        time.sleep(3)  # 3초 지연
        with open(self.filename, 'r', encoding='UTF-8') as file:
            reader = csv.reader(file)
            for row in reader:
                return row[0]

    def cache_menu(self):
        while True:
            time.sleep(3600)  # 매시간마다 갱신
            with self.lock:
                self.cache = self.read_from_file()
                self.last_updated = time.time()

    def get_menu(self, from_cache=False):
        start_time = time.time()
        if from_cache and self.cache is not None:
            menu = self.cache
        else:
            menu = self.read_from_file()
            with self.lock:
                self.cache = menu
                self.last_updated = time.time()
        end_time = time.time()
        print(f"추천 메뉴: {menu} (응답 시간: {end_time - start_time:.2f}초)")
        return menu

    def update_menu(self, new_menu):
        with self.lock:
            with open(self.filename, 'w', newline='', encoding='UTF-8') as file:
                writer = csv.writer(file)
                writer.writerow([new_menu])
            self.cache = new_menu
            self.last_updated = time.time()
        print(f"메뉴가 {new_menu}(으)로 변경되었습니다.")


filename = 'menu_hour.csv'
cafe_menu_cache = CafeMenuCache(filename)

# 초기 캐싱 스레드 시작
cache_thread = threading.Thread(target=cafe_menu_cache.cache_menu)
cache_thread.daemon = True
cache_thread.start()

while True:
    print("메뉴를 선택하세요: 1) 원본 파일에서 읽기 2) 캐시에서 읽기 3) 메뉴 변경")
    choice = input("선택: ")

    if choice == '1':
        cafe_menu_cache.get_menu(from_cache=False)
    elif choice == '2':
        cafe_menu_cache.get_menu(from_cache=True)
    elif choice == '3':
        new_menu = input("새 메뉴를 입력하세요: ")
        cafe_menu_cache.update_menu(new_menu)
    else:
        print("잘못된 선택입니다. 다시 시도하세요.")
