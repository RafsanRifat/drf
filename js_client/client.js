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
    let bodyStr = JSON.stringify(loginObjectData)
    console.log(loginObjectData)
    console.log(loginFormData)
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: bodyStr
    }
     fetch(loginEndpoint, options) //  Promise
    .then(response=>{
        return response.json()
    })
        .then(x =>{
            console.log(x)
        })
        .catch(err=> {
            console.log('err', err)
    })
}