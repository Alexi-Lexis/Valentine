<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Настя Коза Богиня 👑🐐</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    overflow: hidden;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Arial, sans-serif;
    background: radial-gradient(circle at center, #ffd700, #ff9a00, #b8860b);
}

h1 {
    position: absolute;
    font-size: 8vw;
    color: white;
    text-shadow: 0 0 30px gold, 0 0 60px orange;
    z-index: 2;
    text-align: center;
}

#finalText {
    position: absolute;
    font-size: 9vw;
    color: gold;
    text-shadow: 0 0 40px white, 0 0 80px gold;
    display: none;
    animation: pulse 1.2s infinite;
    z-index: 3;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.15); }
    100% { transform: scale(1); }
}

.shake {
    animation: shake 0.15s infinite;
}

@keyframes shake {
    0% { transform: translate(2px, 2px); }
    50% { transform: translate(-2px, -2px); }
    100% { transform: translate(2px, -2px); }
}

button {
    position: absolute;
    bottom: 40px;
    padding: 16px 28px;
    font-size: 18px;
    border: none;
    border-radius: 40px;
    background: white;
    cursor: pointer;
    z-index: 5;
    font-weight: bold;
}

.goat {
    position: absolute;
    pointer-events: none;
    transition: transform 2s ease-out, opacity 2s ease-out;
}
</style>
</head>

<body>

<h1 id="title">Настя коза 🐐</h1>
<div id="finalText">БОГИНЯ 👑🐐</div>
<button id="activateBtn">АКТИВУВАТИ 👑</button>

<audio id="epicMusic" preload="auto">
    <source src="./music.mp3" type="audio/mpeg">
</audio>

<script>
const button = document.getElementById("activateBtn");
const title = document.getElementById("title");
const finalText = document.getElementById("finalText");
const music = document.getElementById("epicMusic");

let activated = false;

function createGoat(x, y, size) {
    const goat = document.createElement("div");
    goat.className = "goat";
    goat.innerHTML = "🐐";
    goat.style.left = x + "px";
    goat.style.top = y + "px";
    goat.style.fontSize = size + "px";
    document.body.appendChild(goat);

    const tx = (Math.random() - 0.5) * 1200;
    const ty = (Math.random() - 0.5) * 800;

    requestAnimationFrame(() => {
        goat.style.transform = translate(${tx}px, ${ty}px) rotate(720deg);
        goat.style.opacity = "0";
    });

    setTimeout(() => goat.remove(), 2000);
}

function explode() {
    const rect = title.getBoundingClientRect();
    title.style.visibility = "hidden";

    for (let i = 0; i < 80; i++) {
        createGoat(
            rect.left + rect.width / 2,
            rect.top + rect.height / 2,
            20 + Math.random() * 60
        );
    }
}

button.addEventListener("click", () => {
    if (activated) return;
    activated = true;

    explode();
    document.body.classList.add("shake");

    music.play().catch(()=>{});

    setTimeout(() => {
        finalText.style.display = "block";
    }, 2000);

    button.remove();

    setInterval(() => {
        createGoat(
            Math.random() * window.innerWidth,
            window.innerHeight,
            20 + Math.random() * 50
        );
    }, 300);
});
</script>

</body>
</html>
