let desc = document.querySelector('#desc')
let poster = document.querySelector('#poster')
let duration = document.querySelector('#duration')
let submitButton = document.querySelector('#submit')
let base64_poster = null
let film_id = window.location.pathname.slice(8,-1)
function image_to_base64(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (param){
            base64_poster = param.target.result
        }
        reader.readAsDataURL(input.files[0])
    }
}

submitButton.onclick = async function (params) {
    console.log(base64_poster)
    const url = 'http://127.0.0.1:8000/rest/movie/create/second-step/'
    const data = {
        "pk":film_id,
        "desc":desc.value,
        "poster": base64_poster,
        "duration": duration.value,
    }

    const response = await fetch(
        url,
        {
            method: 'POST',
            mode: 'cors',
            headers: {
                Accept: "application/json",
                'Content-Type': 'application/json'
            },
            credentials: "same-origin",
            body: JSON.stringify(data)
        }
    )
    rez = await response.json()
    console.log(rez.film_id)
    window.location.pathname = "/third/"+rez.film_id
}
