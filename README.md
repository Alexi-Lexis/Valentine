<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8">
<title>Настя Коза Богиня 👑🐐</title>

<style>
body {
    margin: 0;
    overflow: hidden;
    background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #ffd1ff, #fff0ac);
    background-size: 400% 400%;
    animation: gradientBG 8s ease infinite;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    font-family: Arial, sans-serif;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

h1 {
    position: absolute;
    font-size: 9vw;
    color: white;
    text-align: center;
    text-shadow: 0 0 40px gold;
    z-index: 2;
    cursor: pointer;
}

#finalText {
    position: absolute;
    font-size: 10vw;
    color: gold;
    text-shadow: 0 0 40px white;
    display: none;
    animation: pulse 1.5s infinite;
    z-index: 3;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.15); }
    100% { transform: scale(1); }
}

.shake {
    animation: shakeScreen 0.2s infinite;
}

@keyframes shakeScreen {
    0% { transform: translate(2px, 2px); }
    50% { transform: translate(-2px, -2px); }
    100% { transform: translate(2px, -2px); }
}

button {
    position: absolute;
    bottom: 30px;
    padding: 15px 25px;
    font-size: 18px;
    border: none;
    border-radius: 30px;
    background: white;
    cursor: pointer;
    z-index: 4;
}
.goat {
    position: absolute;
    font-size: 30px;
    animation: float linear infinite;
}

@keyframes float {
    from {transform: translateY(100vh) rotate(0deg);}
    to {transform: translateY(-10vh) rotate(360deg);}
}
</style>
</head>

<body>

<h1 id="title">Настя коза 🐐</h1>
<div id="finalText">БОГИНЯ 👑🐐</div>
<button onclick="activateGoddess()">АКТИВУВАТИ КОЗУ-БОГИНЮ 👑🐐</button>

<audio id="goatSound">
<source src="https://www.soundjay.com/animal/goat-bleating-01.mp3" type="audio/mpeg">
</audio>

<script>
function createGoat(x, y, size) {
    const goat = document.createElement("div");
    goat.classList.add("goat");
    goat.innerHTML = "🐐";
    goat.style.left = x + "px";
    goat.style.top = y + "px";
    goat.style.fontSize = size + "px";
    document.body.appendChild(goat);

    setTimeout(() => {
        goat.remove();
    }, 8000);
}

function explodeText() {
    const title = document.getElementById("title");
    const rect = title.getBoundingClientRect();
    const text = title.innerText;

    title.style.visibility = "hidden";

    for (let i = 0; i < text.length; i++) {
        for (let j = 0; j < 15; j++) {
            const x = rect.left + rect.width/2;
            const y = rect.top + rect.height/2;
            const size = 20 + Math.random() * 50;
            createGoat(x, y, size);

            const goat = document.querySelectorAll(".goat");
            const lastGoat = goat[goat.length-1];
            const tx = (Math.random() - 0.5) * 1000;
            const ty = (Math.random() - 0.5) * 600;
            lastGoat.style.transition = "transform 2s ease-out";
            setTimeout(() => {
                lastGoat.style.transform = translate(${tx}px, ${ty}px) rotate(720deg);
            }, 10);
        }
    }
}

function activateGoddess() {
    explodeText();
    document.body.classList.add("shake");

    const sound = document.getElementById("goatSound");
    setInterval(() => {
        sound.currentTime = 0;
        sound.play();
    }, 2000);

    // Показуємо фінальний текст через 2 секунди
    setTimeout(() => {
        document.getElementById("finalText").style.display = "block";
    }, 2000);

    document.querySelector("button").remove();

    // Постійні козочки хаотично
    setInterval(() => {
        createGoat(Math.random()*window.innerWidth, window.innerHeight, 20 + Math.random()*50);
    }, 300);
}
</script>

</body>
</html>
