import streamlit as st
import streamlit.components.v1 as cp

st.set_page_config(page_title="Game Ga", page_icon="🐔")
st.title("🐔 Trò Chơi: Gà Qua Đường")

# Định nghĩa các ký tự đặc biệt bằng hàm chr() để tránh lỗi ngắt dòng trên điện thoại
nhay_kep = chr(34) + chr(34) + chr(34)
xuong_dong = chr(10)

# Xây dựng mã nguồn trò chơi chuyển động mượt mà
game_code = [
    "<!DOCTYPE html><html><head><meta charset='UTF-8'><style>",
    "body{margin:0;display:flex;flex-direction:column;align-items:center;background:#f0f0f0;font-family:sans-serif;user-select:none;}",
    "canvas{border:4px solid #333;border-radius:8px;max-width:100%;}",
    ".btn-box{margin-top:10px;display:flex;gap:20px;}",
    ".btn{width:80px;height:50px;font-size:24px;background:#FFA500;color:#fff;border:none;border-radius:10px;box-shadow:0 4px #cc8400;}",
    "</style></head><body>",
    "<canvas id='gCanvas' width='500' height='500'></canvas>",
    "<div class='btn-box'><button class='btn' id='bUp'>▲</button><button class='btn' id='bDown'>▼</button></div>",
    "<script>",
    "const cv=document.getElementById('gCanvas'),ctx=cv.getContext('2d'),aCtx=new(window.AudioContext||window.webkitAudioContext)();",
    "let lv=1,gWon=false,wScr=false,decorations=[];",
    "setInterval(()=>{if(aCtx.state==='suspended'||wScr)return;let o=aCtx.createOscillator(),g=aCtx.createGain();o.type='triangle';o.frequency.setValueAtTime(260,aCtx.currentTime);g.gain.setValueAtTime(0.012,aCtx.currentTime);g.gain.exponentialRampToValueAtTime(0.001,aCtx.currentTime+0.8);o.connect(g);g.connect(aCtx.destination);o.start();o.stop(aCtx.currentTime+0.8);},1000);",
    "function pCk(){if(aCtx.state==='suspended')aCtx.resume();let o=aCtx.createOscillator(),g=aCtx.createGain();o.type='sawtooth';o.frequency.setValueAtTime(480,aCtx.currentTime);g.gain.setValueAtTime(0.06,aCtx.currentTime);g.gain.linearRampToValueAtTime(0,aCtx.currentTime+0.08);o.connect(g);g.connect(aCtx.destination);o.start();o.stop(aCtx.currentTime+0.08);}",
    "function getSkyColor(){let m=lv%5;if(m===1)return{sky:'#4682B4',sun:'#FFFFE0',gnd:'#228B22',n:false};if(m===2)return{sky:'#FF4500',sun:'#FFD700',gnd:'#556B2F',n:false};if(m===3)return{sky:'#111133',sun:'#FFFACD',gnd:'#006400',n:true};if(m===4)return{sky:'#FFB6C1',sun:'#FFA500',gnd:'#3CB371',n:false};return{sky:'#87CEEB',sun:'#FFD700',gnd:'#32CD32',n:false};}",
    "function generateDecorations(){decorations=[];let types=['tree','light'];for(let i=0;i<4;i++){decorations.push({x:Math.random()*440+20,y:Math.random()>0.5?410:90,type:types[Math.floor(Math.random()*types.length)]});}}generateDecorations();",
    "const ck={x:235,y:445,w:24,h:24,step:30,draw(){ctx.fillStyle='#D2691E';ctx.fillRect(this.x+5,this.y+18,3,7);ctx.fillRect(this.x+16,this.y+18,3,7);ctx.fillStyle='#FF0000';ctx.beginPath();ctx.moveTo(this.x+2,this.y+14);ctx.lineTo(this.x-4,this.y+6);ctx.lineTo(this.x+4,this.y+10);ctx.fill();ctx.fillStyle='#FFF';ctx.beginPath();ctx.arc(this.x+12,this.y+12,11,0,Math.PI*2);ctx.fill();ctx.fillStyle='#F5F5F5';ctx.beginPath();ctx.ellipse(this.x+2,this.y+12,3,6,0,0,Math.PI*2);ctx.fill();ctx.fillStyle='#FF0000';ctx.beginPath();ctx.arc(this.x+12,this.y-1,4,0,Math.PI*2);ctx.fill();ctx.fillStyle='#FFA500';ctx.beginPath();ctx.moveTo(this.x+12,this.y+2);ctx.lineTo(this.x+19,this.y+5);ctx.lineTo(this.x+12,this.y+8);ctx.fill();ctx.fillStyle='#000';ctx.fillRect(this.x+10,this.y+3,2,2);}};",
    "const cars=[{x:0,y:315,w:60,h:30,sp:1.5,c:'#FF4500'},{x:250,y:315,w:60,h:30,sp:1.5,c:'#FF4500'},{x:400,y:245,w:75,h:30,sp:-2.0,c:'#1E90FF'},{x:100,y:245,w:75,h:30,sp:-2.0,c:'#1E90FF'},{x:50,y:175,w:55,h:30,sp:2.3,c:'#BA55D3'}];",
    "function gSp(c){let inc=(lv-1)*0.16;return c.sp>0?Math.min(c.sp+inc,8.0):Math.max(c.sp-inc,-8.0);}",
    "function mUp(){if(wScr)return;if(ck.y>60)ck.y-=ck.step;pCk();if(ck.y<=110){gWon=true;wScr=true;setTimeout(()=>{lv++;generateDecorations();ck.x=235;ck.y=445;gWon=false;wScr=false;},2000);}}",
    "function mDn(){if(!wScr&&ck.y<445){ck.y+=ck.step;pCk();}}",
    "window.addEventListener('keydown',e=>{if(e.repeat)return;if(e.key==='ArrowUp')mUp();if(e.key==='ArrowDown')mDn();});",
    "document.getElementById('bUp').addEventListener('click',mUp);document.getElementById('bDown').addEventListener('click',mDn);",
    "function loop(){let env=getSkyColor();ctx.fillStyle=env.sky;ctx.fillRect(0,0,500,500);ctx.fillStyle=env.sun;ctx.beginPath();ctx.arc(60,45,20,0,Math.PI*2);ctx.fill();if(env.n){ctx.fillStyle=env.sky;ctx.beginPath();ctx.arc(72,45,16,0,Math.PI*2);ctx.fill();}ctx.fillStyle=env.gnd;ctx.fillRect(0,80,500,50);ctx.fillStyle='#3A3A3A';ctx.fillRect(0,130,500,240);ctx.fillStyle=env.gnd;ctx.fillRect(0,370,500,130);ctx.strokeStyle='rgba(255,255,255,0.85)';ctx.lineWidth=3;for(let y=203;y<350;y+=70){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(500,y);ctx.stroke();}decorations.forEach(d=>{if(d.type==='tree'){ctx.fillStyle='#8B4513';ctx.fillRect(d.x+4,d.y+10,4,10);ctx.fillStyle='#006400';ctx.beginPath();ctx.arc(d.x+6,d.y+6,10,0,Math.PI*2);ctx.fill();}else if(d.type==='light'){ctx.fillStyle='#111';ctx.fillRect(d.x+4,d.y,4,22);ctx.fillStyle='#222';ctx.fillRect(d.x,d.y-3,12,14);let flash=(Math.floor(Date.now()/400)%3===0)?'#FF0000':'#00FF00';ctx.fillStyle=flash;ctx.beginPath();ctx.arc(d.x+6,d.y+4,3,0,Math.PI*2);ctx.fill();}});ctx.fillStyle=env.n?'#FFF':'#000';ctx.font='bold 16px Arial';ctx.textAlign='right';ctx.fillText('Màn chơi: '+lv+' / 100',480,32);cars.forEach(c=>{let s=gSp(c);if(!wScr){c.x+=s;if(s>0&&c.x>500)c.x=-c.w;if(s<0&&c.x<-c.w)c.x=500;if(ck.x+2<c.x+c.w&&ck.x+ck.w-2>c.x&&ck.y+2<c.y+c.h&&ck.y+ck.h-2>c.y){ck.x=235;ck.y=445;}}ctx.fillStyle=c.c;ctx.fillRect(c.x,c.y,c.w,c.h);ctx.fillStyle='#E0FFFF';if(s>0){ctx.fillRect(c.x+c.w-14,c.y+4,10,c.h-8);}else{ctx.fillRect(c.x+4,c.y+4,10,c.h-8);}ctx.fillStyle='#111';ctx.fillRect(c.x+8,c.y-4,12,4);ctx.fillRect(c.x+c.w-20,c.y-4,12,4);ctx.fillRect(c.x+8,c.y+c.h,12,4);ctx.fillRect(c.x+c.w-20,c.y+c.h,12,4);ctx.fillStyle='#C0C0C0';ctx.fillRect(c.x+13,c.y-3,2,2);ctx.fillRect(c.x+c.w-15,c.y-3,2,2);});ck.draw();if(wScr){ctx.fillStyle='rgba(0,0,0,0.65)';ctx.fillRect(0,0,500,500);ctx.fillStyle='#FFD700';ctx.fillRect(70,170,360,130);ctx.lineWidth=4;ctx.strokeStyle='#FFF';ctx.strokeRect(70,170,360,130);ctx.fillStyle='#000';ctx.font='bold 22px Arial';ctx.textAlign='center';ctx.fillText('🎉 QUA MÀN THÀNH CÔNG! 🎉',250,222);ctx.font='15px Arial';ctx.fillText('Chuẩn bị bước sang Màn '+(lv+1)+'...',250,268);}requestAnimationFrame(loop);}loop();",
    "</script></body></html>"
]

# Gộp các dòng lại thành chuỗi văn bản hoàn chỉnh
game_html = xuong_dong.join(game_code)

# Nhúng bảng vẽ trò chơi thực sự vào Streamlit web
cp.html(game_html, height=580, width=510)
st.info("💡 Bấm nút ▲ / ▼ màu cam để điều khiển chú gà nhảy từng bước một!")
