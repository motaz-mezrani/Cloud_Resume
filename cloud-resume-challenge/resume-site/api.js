  fetch('https://8ckue7tfqk.execute-api.us-east-1.amazonaws.com/Prod/put')
        .then(() => fetch('https://8ckue7tfqk.execute-api.us-east-1.amazonaws.com/Prod/get'))
        .then(response => response.json())
        .then((data) => {
            document.getElementById('count').innerText = data.count
        })
