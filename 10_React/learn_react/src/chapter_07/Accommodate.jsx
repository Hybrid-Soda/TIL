import React, { useState, useEffect } from "react";
import useCounter from "./useCounter";

const MAX_CAPACITY = 10;

function Accommodate(props) {
  const [isFull, setIsFull] = useState(false);
  const [count, increaseCount, decreaseCount] = useCounter(0);

  // 의존성 배열 생략 → 컴포넌트 업데이트 시마다 실행
  useEffect(() => {
    console.log("===================== ");
    console.log("useEffect() is called.");
    console.log(`isFull: ${isFull}`);
  });

  // 의존성 배열 → 값이 변경될 때마다 이펙트 함수 실행
  useEffect(() => {
    setIsFull(count >= MAX_CAPACITY);
    console.log(`Current count value: ${count}`);
  }, [count]);

  return (
    <div style={{ padding: 16 }}>
      <p>{`총 ${count}명 수용했습니다. `}</p>

      <button onClick={increaseCount} disabled={isFull}>
        입장
      </button>
      <button onClick={decreaseCount}>
        퇴장
      </button>

      {isFull && <p style={{ color: "red" }}>정원이 가득찼습니다 .</p>}
    </div>
  );
}

export default Accommodate;