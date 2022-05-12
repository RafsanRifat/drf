const loginform = document.getElementById('login-form')
const baseEndpoint = "http://localhost:8000/api"


if (loginform) {
    loginform.addEventListener("submit", handleLogin)
}


function handleLogin(event) {
    console.log(event)
    event.preventDefault()
}