const loginform = document.getElementById('login-form')
const baseEndpoint = "http://localhost:8000/api"


if (loginform) {
    loginform.addEventListener("submit", handleLogin)
}


function handleLogin(event) {
    console.log(event)
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginform)
    let loginObjectData = Object.fromEntries(loginFormData)
    console.log(loginObjectData)
    console.log(loginFormData)
    const options = {
        method: "POST",
        headers: {
            "ContentType": "application/json"
        },
        body: ""
    }
    fetch(loginEndpoint, options)
}