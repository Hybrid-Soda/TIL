-- 거래(transactions) 테이블 생성
CREATE TABLE transactions (
    id INT PRIMARY KEY,
    user_id INT NOT NULL,
    amount INT NOT NULL,
    transaction_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- 거래 데이터 삽입
INSERT INTO transactions (id, user_id, amount, transaction_date) VALUES (1, 1, 500, '2024-03-15');
INSERT INTO transactions (id, user_id, amount, transaction_date) VALUES (2, 2, 700, '2024-03-16');
INSERT INTO transactions (id, user_id, amount, transaction_date) VALUES (3, 1, 200, '2024-03-17');
INSERT INTO transactions (id, user_id, amount, transaction_date) VALUES (4, 3, 1000, '2024-03-18');

-- user 테이블의 각 user별 first_name, last_name, amount, transaction_date를 조회
SELECT u.first_name, u.last_name, t.amount, t.transaction_date
FROM users u
JOIN transactions t ON t.user_id = u.id;

-- users 테이블의 각 user별 거래 일자가 '2024-03-16' 이후인 데이터의 first_name, last_name, amount, transaction_date를 조회
SELECT u.first_name, u.last_name, t.amount, t.transaction_date
FROM users u
JOIN transactions t ON t.user_id = u.id
WHERE t.transaction_date > '2024-03-16';

-- users 테이블의 각 user별 first_name, last_name, 총 거래량 (total_amount)를 조회
SELECT u.first_name, u.last_name, SUM(t.amount) AS total_amount
FROM users u
JOIN transactions t ON t.user_id = u.id
GROUP BY u.id;