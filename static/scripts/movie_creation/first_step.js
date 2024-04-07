let title = document.querySelector('#title')
let release_date = document.querySelector('#release_date')
let studio = document.querySelector('#studio')
let submitButton = document.querySelector('#submit')

submitButton.onclick = async function (params) {
    const url = 'http://127.0.0.1:8000/rest/first-step/'
    const data = {
        "title": title.value,
        "release_date": release_date.value,
        "studio": studio.value,
    }

    const response = await fetch(
        url,
        {
            method: 'POST',
            mode: 'cors',
            headers: {
                Accept: "application/json",
                'Content-Type': 'application/json',
            },
            credentials: "same-origin",
            body: JSON.stringify(data)
        }
    )

    rez = await response.json()
    console.log(rez.film_id)
    window.location.pathname = "/second/"+rez.film_id
}