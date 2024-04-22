### 동기 Synchronous
- 코드가 작성된 순서대로 한 줄씩 차례대로 실행
- 한 작업이 완료되어야 다음 작업으로 넘어갈 수 있다
- 코드의 실행 순서가 명확하고 예측하기 쉽다
- 긴 처리 시간이 필요한 작업은 전체 코드의 실행을 방해한다
- 예시
  ```js
  console.log('첫 번째 작업 완료')
  alert('긴 작업 수행 중...')
  console.log('두 번째 작업 완료')
  ```

### 비동기 Asynchronous
- 특정 코드의 완료를 기다리지 않고 다음 코드를 계속 실행
- 코드의 실행 순서가 비선형적이고 예측하기 어려움
- 리소스를 효율적으로 사용하고 응답성을 높일 수 있다
- 예시
  ```js
  const slowRequest = function(callBack) {
    console.log('1. 오래 걸리는 작업 시작')
    setTimeout(function () {
      callBack()
    }, 3000)
  }

  const myCallBack = function () {
    console.log('2. 콜백함수 실행')
  }

  slowRequest(mycallBack)
  console.log('3. 다른 작업 진행')
  ```