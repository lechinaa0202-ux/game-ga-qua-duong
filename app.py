import streamlit as st

st.set_page_config(page_title="Siêu Game Gà Qua Đường", page_icon="🐔", layout="centered")
st.title("🐔 Siêu Game Gà Qua Đường Pro")
st.write("Sử dụng các phím mũi tên hoặc **W-A-S-D** để điều khiển chú gà nhé!")

game_source_code = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body { text-align: center; font-family: Arial, sans-serif; background: #f0f2f6; margin: 0; padding: 0; }
        #gameCanvas { background: #87CEEB; border: 4px solid #333; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2); }
        select, button { padding: 10px 20px; font-size: 16px; font-weight: bold; border-radius: 5px; cursor: pointer; border: 1px solid #ccc; margin: 5px; }
        button { background-color: #4CAF50; color: white; border: none; }
        button:hover { background-color: #45a049; }
        #winScreen { display: none; position: absolute; top: 160px; left: 50%; transform: translateX(-50%); background: rgba(255, 255, 255, 0.95); border: 5px solid #FFD700; padding: 25px 40px; border-radius: 15px; box-shadow: 0px 10px 20px rgba(0,0,0,0.3); text-align: center; z-index: 10; animation: pop 0.4s ease-out; }
        @keyframes pop { 0% { transform: translateX(-50%) scale(0.5); } 100% { transform: translateX(-50%) scale(1); } }
        h1 { color: #d32f2f; margin: 5px 0; font-size: 28px; }
        p { color: #388e3c; font-size: 18px; font-weight: bold; }
    </style>
</head>
<body>
    <div>
        <label for="difficulty" style="font-weight:bold; font-size:16px;">Cấp độ: </label>
        <select id="difficulty" onchange="changeDifficulty()">
            <option value="easy">Dễ (Xe chạy chậm)</option>
            <option value="medium" selected>Bình thường</option>
            <option value="hard">Khó (Thử thách siêu tốc!)</option>
        </select>
        <button onclick="toggleMusic()" id="musicBtn">🎵 Bật Nhạc Chill</button>
        <button onclick="resetGame()" style="background-color: #008CBA;">🔄 Chơi Lại</button>
    </div>
    <div style="position: relative; display: inline-block; margin-top: 10px;">
        <canvas id="gameCanvas" width="500" height="550"></canvas>
        <div id="winScreen">
            <h1>🎉 XUẤT SẮC CHIẾN THẮNG! 🎉</h1>
            <p>Chú gà đã vượt qua muôn vàn bão táp để về đích an toàn!</p>
            <button onclick="resetGame()" style="background:#FF9800; font-size:18px;">Tiếp tục màn sau ➡️</button>
        </div>
    </div>
    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");
        const winScreen = document.getElementById("winScreen");
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        let musicInterval = null; let isMusicPlaying = false;

        function playSound(type) {
            try {
                let osc = audioCtx.createOscillator(); let gain = audioCtx.createGain();
                osc.connect(gain); gain.connect(audioCtx.destination);
                if (type === 'chicken') {
                    osc.type = 'sawtooth'; osc.frequency.setValueAtTime(400, audioCtx.currentTime);
                    osc.frequency.exponentialRampToValueAtTime(800, audioCtx.currentTime + 0.1);
                    gain.gain.setValueAtTime(0.3, audioCtx.currentTime); gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.15);
                    osc.start(); osc.stop(audioCtx.currentTime + 0.15);
                } else if (type === 'car') {
                    osc.type = 'square'; osc.frequency.setValueAtTime(550, audioCtx.currentTime);
                    gain.gain.setValueAtTime(0.08, audioCtx.currentTime); gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.08);
                    osc.start(); osc.stop(audioCtx.currentTime + 0.08);
                } else if (type === 'win') {
                    let notes = [523.25, 659.25, 783.99, 1046.50];
                    notes.forEach((f, i) => {
                        let o = audioCtx.createOscillator(); let g = audioCtx.createGain();
                        o.connect(g); g.connect(audioCtx.destination);
                        o.frequency.setValueAtTime(f, audioCtx.currentTime + i*0.08);
                        g.gain.setValueAtTime(0.15, audioCtx.currentTime + i*0.08); g.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + i*0.08 + 0.15);
                        o.start(audioCtx.currentTime + i*0.08); o.stop(audioCtx.currentTime + i*0.08 + 0.15);
                    });
                }
            } catch(e) {}
        }

        function playChillMusic() {
            if(!isMusicPlaying) return;
            let baseNotes = [261.63, 329.63, 392.00, 440.00, 523.25]; 
            let note = baseNotes[Math.floor(Math.random() * baseNotes.length)];
            let osc = audioCtx.createOscillator(); let gain = audioCtx.createGain();
            osc.type = 'sine'; osc.frequency.setValueAtTime(note, audioCtx.currentTime);
            gain.gain.setValueAtTime(0.04, audioCtx.currentTime); gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.9);
            osc.connect(gain); gain.connect(audioCtx.destination);
            osc.start(); osc.stop(audioCtx.currentTime + 0.9);
        }

        function toggleMusic() {
            if(audioCtx.state === 'suspended') audioCtx.resume();
            isMusicPlaying = !isMusicPlaying;
            document.getElementById("musicBtn").innerText = isMusicPlaying ? "⏸️ Dừng Nhạc Chill" : "🎵 Bật Nhạc Chill";
            if(isMusicPlaying) { if(!musicInterval) musicInterval = setInterval(playChillMusic, 900); }
            else { clearInterval(musicInterval); musicInterval = null; }
        }

        let chicken = { x: 235, y: 490, width: 30, height: 30, speed: 40 };
        let cars = []; let gameStatus = "PLAYING"; let speedMultiplier = 1.5; let carSpawnRate = 0.02;
        const lanes = [{ y: 150, speed: -1.4, dir: -1 }, { y: 220, speed: 1.8, dir: 1 }, { y: 290, speed: -2.3, dir: -1 }, { y: 360, speed: 1.6, dir: 1 }];

        function changeDifficulty() {
            let diff = document.getElementById("difficulty").value;
            if(diff === "easy") { speedMultiplier = 0.8; carSpawnRate = 0.01; }
            else if(diff === "medium") { speedMultiplier = 1.6; carSpawnRate = 0.02; }
            else if(diff === "hard") { speedMultiplier = 3.2; carSpawnRate = 0.04; }
            resetGame();
        }

        let clouds = [{ x: 40, y: 30, size: 18 }, { x: 220, y: 55, size: 24 }, { x: 400, y: 25, size: 16 }];

        function draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = "#87CEEB"; ctx.fillRect(0, 0, canvas.width, 100);
            ctx.fillStyle = "#FFD700"; ctx.beginPath(); ctx.arc(430, 40, 22, 0, Math.PI * 2); ctx.fill();
            ctx.fillStyle = "rgba(255, 255, 255, 0.85)";
            clouds.forEach(c => {
                ctx.beginPath(); ctx.arc(c.x, c.y, c.size, 0, Math.PI * 2);
                ctx.arc(c.x + c.size*0.6, c.y - c.size*0.3, c.size*0.8, 0, Math.PI * 2);
                ctx.arc(c.x + c.size*1.2, c.y, c.size*0.6, 0, Math.PI * 2); ctx.fill();
                c.x += 0.25; if(c.x > canvas.width + 50) c.x = -60;
            });
            ctx.fillStyle = "#4CAF50"; ctx.fillRect(0, 100, canvas.width, 40);
            ctx.fillStyle = "#FFF"; ctx.font = "bold 14px Arial"; ctx.fillText("🌾 BÃI CỎ AN TOÀN (ĐÍCH) 🌾", 160, 125);
            ctx.fillStyle = "#444444"; ctx.fillRect(0, 140, canvas.width, 280);
            ctx.strokeStyle = "#FFFFFF"; ctx.lineWidth = 2;
            for(let i = 1; i < lanes.length; i++) { ctx.beginPath(); ctx.moveTo(0, 140 + i * 70); ctx.lineTo(canvas.width, 140 + i * 70); ctx.stroke(); }
            ctx.fillStyle = "#8bc34a"; ctx.fillRect(0, 420, canvas.width, 130);
            ctx.fillStyle = "#3e2723"; ctx.font = "bold 14px Arial"; ctx.fillText("🏡 ĐIỂM XUẤT PHÁT (NHÀ CỦA GÀ)", 150, 455);

            cars.forEach(car => {
                ctx.fillStyle = car.color; ctx.fillRect(car.x, car.y, car.w, car.h);
                ctx.fillStyle = "#111"; ctx.fillRect(car.x + 5, car.y + car.h, 10, 4); ctx.fillRect(car.x + car.w - 15, car.y + car.h, 10, 4);
                ctx.fillStyle = "#E0F7FA";
                if(car.dir > 0) ctx.fillRect(car.x + car.w - 12, car.y + 4, 8, car.h - 8);
                else ctx.fillRect(car.x + 4, car.y + 4, 8, car.h - 8);
                car.x += car.speed * speedMultiplier;
                if(Math.random() < 0.0008) playSound('car');
            });

            cars = cars.filter(car => car.x > -100 && car.x < canvas.width + 100);
            lanes.forEach(lane => {
                if(Math.random() < carSpawnRate) {
                    let carWidth = 52 + Math.random()*18; let colors = ["#e53935", "#1e88e5", "#fdd835", "#8e24aa", "#fb8c00"];
                    cars.push({ x: lane.dir > 0 ? -carWidth : canvas.width, y: lane.y + 15, w: carWidth, h: 30, speed: lane.speed, dir: lane.dir, color: colors[Math.floor(Math.random() * colors.length)] });
                }
            });

            ctx.font = "32px Arial"; ctx.textAlign = "center"; ctx.textBaseline = "middle";
            ctx.fillText("🐔", chicken.x + 15, chicken.y + 15);

            if (gameStatus === "PLAYING") {
                checkCollisions();
                if (chicken.y <= 130) { gameStatus = "WIN"; playSound('win'); winScreen.style.display = "block"; }
            }
        }

        window.addEventListener("keydown", function(e) {
            if(gameStatus !== "PLAYING") return;
            if(audioCtx.state === 'suspended') audioCtx.resume();
            if(e.key === "ArrowUp" || e.key === "w" || e.key === "W") { chicken.y -= chicken.speed; playSound('chicken'); }
            if(e.key === "ArrowDown" || e.key === "s" || e.key === "S") { chicken.y = Math.min(490, chicken.y + chicken.speed); }
