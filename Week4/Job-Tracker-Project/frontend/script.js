fetch("https://axilex-internship-1.onrender.com/api")
.then(res => res.json())
.then(data => {
document.getElementById("output").innerText = data.message
})
.catch(err => console.log(err))