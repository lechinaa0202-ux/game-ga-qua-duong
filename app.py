import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Game Ga", page_icon="🐔", layout="centered")
st.title("🐔 Trò Chơi: Gà Qua Đường")

# Lựa chọn cấp độ khó
level = st.selectbox("Chọn độ khó:", ["Dễ", "Bình thường", "Khó"])
speed_map = {"Dễ": 2, "Bình thường": 4, "Khó": 7}
car_speed = speed_map[level]

# Toàn bộ mã nguồn xử lý game
game_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ margin: 0; display: flex; flex-direction: column; align-items: center; background: #f0f0f0; font-family: sans-serif; }}
        canvas {{ border: 4px solid #333; background: #87CEEB; border-radius: 8px; }}
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="500" height="520"></canvas>
    <p><b>Cách chơi:</b> Bấm phím Mũi tên Lên (▲) và Xuống (▼) trên bàn phím</p>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

        // 1. ÂM THANH (Nhạc nền, tiếng gà, tiếng xe)
        setInterval(() => {{
            if(audioCtx.state === 'suspended') return;
            let osc = audioCtx.createOscillator(), gain = audioCtx.createGain();
            osc.type = 'triangle'; osc.frequency.setValueAtTime(300, audioCtx.currentTime);
            gain.gain.setValueAtTime(0.02, audioCtx.currentTime); gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.8);
            osc.connect(gain); gain.connect(audioCtx.destination); osc.start(); osc.stop(audioCtx.currentTime + 0.8);
        }}, 900);

        function playSound(freq, type, duration, vol) {{
            if(audioCtx.state === 'suspended') audioCtx.resume();
            let osc = audioCtx.createOscillator(), gain = audioCtx.createGain();
            osc.type = type; osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
            gain.gain.setValueAtTime(vol, audioCtx.currentTime); gain.gain.linearRampToValueAtTime(0, audioCtx.currentTime + duration);
            osc.connect(gain); gain.connect(audioCtx.destination); osc.start(); osc.stop(audioCtx.currentTime + duration);
        }}

        // 2. KHỞI TẠO ĐỐI TƯỢNG (Gà và Xe cộ)
        const chicken = {{ x: 235, y: 470, w: 25, h: 25, draw() {{
            ctx.fillStyle = "#FFA500"; ctx.fillRect(this.x + 5, this.y + 20, 3, 6); ctx.fillRect(this.x + 17, this.y + 20, 3, 6); // Chân
            ctx.fillStyle = "#FFFFFF"; ctx.beginPath(); ctx.arc(this.x + 12, this.y + 12, 10, 0, Math.PI*2); ctx.fill(); // Thân
            ctx.fillStyle = "#FF0000"; ctx.beginPath(); ctx.arc(this.x + 12, this.y + 2, 4, 0, Math.PI*2); ctx.fill(); // Mào
        }} }};

        const cars = [
            {{ x: 0, y: 350, w: 50, h: 30, s: {car_speed}, c: '#FF4500' }},
            {{ x: 250, y: 350, w: 50, h: 30, s: {car_speed}, c: '#FF4500' }},
            {{ x: 400, y: 280, w: 60, h: 30, s: -{car_speed}-1, c: '#0000FF' }},
            {{ x: 100, y: 280, w: 60, h: 30, s: -{car_speed}-1, c: '#0000FF' }},
            {{ x: 50, y: 210, w: 50, h: 30, s: {car_speed}+2, c: '#228B22' }}
        ];

        let gameWon = false;

        // 3. ĐIỀU KHIỂN GÀ
        window.addEventListener("keydown", e => {{
            if (gameWon) return;
            if (e.key === "ArrowUp" && chicken.y > 0) {{ chicken.y -= 25; playSound(600, 'sawtooth', 0.1, 0.05); }}
            if (e.key === "ArrowDown" && chicken.y < 470) chicken.y += 25;
            if (chicken.y <= 110) gameWon = true;
        }});

        // 4. VÒNG LẶP CHẠY GAME
        function gameLoop() {{
            ctx.clearRect(0, 0, 500, 520);

            // Bối cảnh bầu trời, mặt trời, mây và đường đi
            ctx.fillStyle = "#FFD700"; ctx.beginPath(); ctx.arc(50, 50, 20, 0, Math.PI*2); ctx.fill(); // Mặt trời
            ctx.fillStyle = "#FFFFFF"; ctx.beginPath(); ctx.arc(150, 45, 12, 0, Math.PI*2); ctx.arc(165, 40, 16, 0, Math.PI*2); ctx.arc(180, 45, 12, 0, Math.PI*2); ctx.fill(); // Mây
            ctx.fillStyle = "#32CD32"; ctx.fillRect(0, 100, 500, 50); // Đích
            ctx.fillStyle = "#444444"; ctx.fillRect(0, 150, 500, 250); // Đường
            ctx.fillStyle = "#32CD32"; ctx.fillRect(0, 400, 500, 120); // Xuất phát

            // Cập nhật xe và kiểm tra va chạm
            if (!gameWon && Math.random() < 0.02) playSound(40, 'sawtooth', 0.3, 0.01);
            cars.forEach(car => {{
                if (!gameWon) {{
                    car.x += car.s;
                    if (car.s > 0 && car.x > 500) car.x = -car.w;
                    if (car.s < 0 && car.x < -car.w) car.x = 500;
                    if (chicken.x < car.x + car.w && chicken.x + chicken.w > car.x && chicken.y < car.y + car.h && chicken.y + chicken.h > car.y) {{
                        chicken.x = 235; chicken.y = 470; // Bị đụng đưa về chỗ cũ
                    }}
                }}
                ctx.fillStyle = car.c; ctx.fillRect(car.x, car.y, car.w, car.h); // Vẽ xe
            }});

            chicken.draw();

            // Biển chúc mừng khi chiến thắng
            if (gameWon) {{
                ctx.fillStyle = "rgba(0, 0, 0, 0.6)"; ctx.fillRect(0, 0, 500, 520);
                ctx.fillStyle = "#FFD700"; ctx.fillRect(75, 180, 350, 130);
                ctx.fillStyle = "#000000"; ctx.font = "bold 22px Arial"; ctx.textAlign = "center";
                ctx.fillText("🎉 XUẤT SẮC! 🎉", 250, 230);
                ctx.font = "16px Arial"; ctx.fillText("Bạn đã giúp gà qua đường thành công!", 250, 270);
            }}
            requestAnimationFrame(gameLoop);
        }}
        gameLoop();
    </script>
</body>
</html>
"""

components.html(game_html, height=570, width=520)
st.info("💡 Click chuột vào khung game trước khi nhấn nút di chuyển để kích hoạt âm thanh.")
