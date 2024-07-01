import React, { useState } from "react"
import TemperatureInput from "./TemperatureInput"

// 섭씨 온도가 100도 이상일 경우 '물이 끓습니다.'라는 메시지를 반환하고,
// 그렇지 않으면 '물이 끓지 않습니다.'라는 메시지를 반환
function BoilingVerdict(props) {
  if (props.celsius >= 100) {
    return <p>물이 끓습니다.</p>
  }
  return <p>물이 끓지 않습니다.</p>
}

// 화씨 온도를 섭씨 온도로 변환
function toCelsius(fahrenheit) {
  return ((fahrenheit - 32) * 5) / 9
}

// 섭씨 온도를 화씨 온도로 변환
function toFahrenheit(celsius) {
  return (celsius * 9) / 5 + 32
}

// 입력된 온도를 변환하고 소수점 세 자리로 반올림하여 문자열로 반환
// 변환할 수 없는 입력일 경우 빈 문자열을 반환
function tryConvert(temperature, convert) {
  const input = parseFloat(temperature)
  if (Number.isNaN(input)) {
    return ""
  }
  const output = convert(input)
  const rounded = Math.round(output * 1000) / 1000
  return rounded.toString()
}

// Calculator 컴포넌트: 온도 변환기의 메인 컴포넌트
// 섭씨와 화씨 입력 필드를 렌더링하고, BoilingVerdict 컴포넌트를 통해 물이 끓는지 여부를 표시
function Calculator(props) {
  // 온도와 온도 단위를 상태로 관리
  const [temperature, setTemperature] = useState("")
  const [scale, setScale] = useState("c")

  // 섭씨 온도가 변경되었을 때 호출되는 함수
  const handleCelsiusChange = (temperature) => {
    setTemperature(temperature)
    setScale("c")
  }

  // 화씨 온도가 변경되었을 때 호출되는 함수
  const handleFahrenheitChange = (temperature) => {
    setTemperature(temperature)
    setScale("f")
  }

  // 현재 온도 단위에 따라 변환된 섭씨와 화씨 값을 계산
  const celsius =
    scale === "f" ? tryConvert(temperature, toCelsius) : temperature
  const fahrenheit =
    scale === "c" ? tryConvert(temperature, toFahrenheit) : temperature

  return (
    <div>
      {/* 섭씨 온도를 입력받는 TemperatureInput 컴포넌트 */}
      <TemperatureInput
        scale="c"
        temperature={celsius}
        onTemperatureChange={handleCelsiusChange}
      />
      {/* 화씨 온도를 입력받는 TemperatureInput 컴포넌트 */}
      <TemperatureInput
        scale="f"
        temperature={fahrenheit}
        onTemperatureChange={handleFahrenheitChange}
      />
      {/* 현재 섭씨 온도가 100도 이상인지 판단하여 물이 끓는지 
      여부를 표시하는 BoilingVerdict 컴포넌트 */}
      <BoilingVerdict celsius={parseFloat(celsius)} />
    </div>
  )
}

export default Calculator
