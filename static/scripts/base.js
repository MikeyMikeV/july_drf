let title = document.querySelector('#title')
let desc = document.querySelector('#desc')
let release_date = document.querySelector('#release_date')
let poster = document.querySelector('#poster')
let duration = document.querySelector('#duration')
let studio = document.querySelector('#studio')
let rating = document.querySelector('#rating')
let submitButton = document.querySelector('#submit')
let base64_poster = null

function image_to_base64(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (param){
            base64_poster = param.target.result
        }
        reader.readAsDataURL(input.files[0])
    }
}

submitButton.onclick = function (params) {
    console.log(base64_poster)
    const url = 'http://127.0.0.1:8000/rest/movie/'
    const data = {
        "title": title.value,
        "desc": desc.value,
        "release_date": release_date.value,
        "poster": base64_poster,
        "duration": duration.value,
        "studio": studio.value,
        "rating": rating.value,
    }

    const response = fetch(
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
}

