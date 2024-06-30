import React from "react"
import ReactDOM from "react-dom/client"
import "./index.css"
import reportWebVitals from "./reportWebVitals"
import LandingPage from "./chapter_09/LandingPage"

// chapter_06
const root = ReactDOM.createRoot(document.getElementById("root"))
root.render(
  <React.StrictMode>
    <LandingPage />
  </React.StrictMode>
)

// chapter_08
//    <ConfirmButtonFunc />

// chapter_07
//    <Accommodate />

// chapter_06
//    <NotificationList />

// chapter_05
//    <CommentList />

// chapter_04
// setInterval(() => {
//       <Clock />
// }, 1000)

// chapter_03
//    <Library />


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals()
