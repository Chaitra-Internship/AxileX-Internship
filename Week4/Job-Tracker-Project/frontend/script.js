fetch("https://your-render-url.onrender.com/api")
.then(res => res.json())
.then(data => {
document.getElementById("output").innerText = data.message
})
.catch(err => console.log(err))