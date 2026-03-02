fetch("https://YOUR_RENDER_URL/api")
.then(res => res.json())
.then(data => {
    document.getElementById("output").innerText = data.message;
})
.catch(err => console.log(err));