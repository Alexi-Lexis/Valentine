html_content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Valentine 💕</title>

<style>
body {
    margin: 0;
    background: linear-gradient(to bottom, #ff758c, #ff7eb3);
    overflow: hidden;
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    text-align: center;
}

h1 {
    color: white;
    font-size: 60px;
    animation: fadeIn 3s ease-in-out;
    z-index: 2;
}

@keyframes fadeIn {
    from { opacity: 0; transform: scale(0.7); }
    to { opacity: 1; transform: scale(1); }
}

.heart {
    position: absolute;
    color: red;
    font-size: 24px;
    animation: float 6s linear infinite;
}

@keyframes float {
    0% { transform: translateY(100vh); opacity: 1; }
    100% { transform: translateY(-10vh); opacity: 0; }
}

iframe {
    position: absolute;
    bottom: 20px;
    width: 300px;
    height: 170px;
    border-radius: 15px;
}
</style>
</head>

<body>

<h1>THANK YOU FOR ALL,<br>MY DEAR ❤️</h1>

<!-- YouTube music -->
<iframe src="https://www.youtube.com/embed/5n9Z3aF0G6c?autoplay=1&loop=1&playlist=5n9Z3aF0G6c"
allow="autoplay">
</iframe>

<script>
function createHeart() {
    const heart = document.createElement("div");
    heart.classList.add("heart");
    heart.innerHTML = "❤️";
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.fontSize = Math.random() * 30 + 20 + "px";
    heart.style.animationDuration = Math.random() * 3 + 3 + "s";
    document.body.appendChild(heart);

    setTimeout(() => {
        heart.remove();
    }, 6000);
}

setInterval(createHeart, 300);
</script>

</body>
</html>
"""

with open("valentine_music.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Файл valentine_music.html створено 💕")