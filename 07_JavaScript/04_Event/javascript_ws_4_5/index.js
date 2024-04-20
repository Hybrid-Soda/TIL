// player1과 player2를 인자로 받아 게임의 결과를 반환
const playGame = function(p1, p2) {
  let win = 0

  if (p1 === 'scissors') {
    // p1 : 가위 | p2 : 바위 -> p2 win
    if (p2 === 'rock') {win = 2}
    // p1 : 가위 | p2 : 보 -> p1 win
    else if (p2 === 'paper') {win = 1}}

  else if (p1 === 'rock') {
    // p1 : 바위 | p2 : 가위 -> p1 win
    if (p2 === 'scissors') {win = 1}
    // p1 : 바위 | p2 : 보 -> p2 win
    else if (p2 === 'paper') {win = 2}}

  else if (p1 === 'paper') {
    // p1 : 보 | p2 : 바위 -> p1 win
    if (p2 === 'rock') {win = 1}
    // p1 : 보 | p2 : 가위 -> p2 win
    else if (p2 === 'scissors') {win = 2}}
    console.log(count1)
  
  // p1 win: 1
  if (win === 1) {
    count1.textContent = Number(count1.textContent) + 1
    return 1} 
  // p2 win: 2
  else if (win === 2) {
    count2.textContent = Number(count2.textContent) + 1
    return 2}
  // draw: 0
  else {return 0}
}


// choice를 인자로 받아 버튼이 클릭되었을 때의 동작 처리
const buttonClickHandler = function(choice1) {
  const modalContent = document.querySelector('.modal-content')
  const modal = document.querySelector('.modal')
  let randomIndex = 0
  let choice2 = ''
  
  // 버튼 비활성화 및 player1 사진 변경
  disableBtn()
  player1Img.src = `./img/${choice1}.png`
  
  // 선택지 배열
  const choices = ['scissors', 'rock', 'paper']
  
  // 무작위 인덱스로 상대방의 선택 결정
  const interval = setInterval(() => {
    randomIndex = Math.floor(Math.random() * choices.length)
    choice2 = choices[randomIndex]
    player2Img.src = `./img/${choice2}.png`
  }, 100)

  // 3초 후
  setTimeout(() => {
    // 무작위 인덱스 중단
    clearInterval(interval)

    // playGame 함수 호출 및 결과 도출
    const result = playGame(choice1, choice2)

    // 결과에 따른 메세지 변경
    if (result === 1) {modalContent.innerText = 'Player 1 wins!'}
    else if (result === 2) {modalContent.innerText = 'Player 2 wins!'}
    else if (result === 0) {modalContent.innerText = "It's a tie!"}

    // 버튼 활성화 및 결과 표시 활성화
    modal.style.display = 'block'
    enableBtn()
  }, 3000)

  // 결과 표시 비활성화
  setTimeout(() => {modal.style.display = 'none'}, 9000)
}

// 게임 승패 요소
let count1 = document.querySelector('.countA')
let count2 = document.querySelector('.countB')
let player1Img = document.getElementById('player1-img')
let player2Img = document.getElementById('player2-img')

// 버튼 활성화 및 비활성화
const buttons = document.querySelectorAll('button')
function disableBtn() {buttons.forEach(button => button.disabled = true)}
function enableBtn() {buttons.forEach(button => button.disabled = false)}

// 각 버튼
const rockBtn = document.getElementById('rock-button')
const scissorsBtn = document.getElementById('scissors-button')
const paperBtn = document.getElementById('paper-button')

// 각 버튼에 대한 이벤트 핸들러
rockBtn.addEventListener('click', () => buttonClickHandler('rock'))
scissorsBtn.addEventListener('click', () => buttonClickHandler('scissors'))
paperBtn.addEventListener('click', () => buttonClickHandler('paper'))