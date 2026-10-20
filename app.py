import streamlit as st
import streamlit.components.v1 as cp

st.set_page_config(page_title="Game Ga", page_icon="🐔")
st.title("🐔 Trò Chơi: Gà Qua Đường")

xuong_dong = chr(10)

game_code = [
    "<!DOCTYPE html><html><head><meta charset='UTF-8'>",
    "<meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no'>",
    "<style>",
    "body{margin:0;display:flex;flex-direction:column;align-items:center;background:#f0f0f0;font-family:sans-serif;user-select:none;-webkit-user-select:none;touch-action:none;}",
    "canvas{border:4px solid #333;border-radius:8px;max-width:100%;}",
    ".btn-box{margin-top:15px;display:flex;gap:20px;}",
    ".btn{width:85px;height:55px;font-size:26px;background:#FFA500;color:#fff;border:none;border-radius:12px;box-shadow:0 4px #cc8400;touch-action:manipulation;}",
    "</style></head><body>",
    "<canvas id='gCanvas' width='500' height='500'></canvas>",
    "<div class='btn-box'><button class='btn' id='bUp'>▲</button><button class='btn' id='bDown'>▼</button></div>",
    "<script>",
    "const cv=document.getElementById('gCanvas'),ctx=cv.getContext('2d'),aCtx=new(window.AudioContext||window.webkitAudioContext)();",
    "let lv=1,gWon=false,wScr=false,gLost=false,decorations=[];",
    "let timeLimit=15,timeLeft=15,lastTime=Date.now();",
    "setInterval(()=>{if(aCtx.state==='suspended'||wScr||gLost)return;let o=aCtx.createOscillator(),g=aCtx.createGain();o.type='triangle';o.frequency.setValueAtTime(260,aCtx.currentTime);g.gain.setValueAtTime(0.012,aCtx.currentTime);g.gain.exponentialRampToValueAtTime(0.001,aCtx.currentTime+0.8);o.connect(g);g.connect(aCtx.destination);o.start();o.stop(aCtx.currentTime+0.8);},1000);",
    "function pCk(){if(aCtx.state==='suspended')aCtx.resume();let o=aCtx.createOscillator(),g=aCtx.createGain();o.type='sawtooth';o.frequency.setValueAtTime(480,aCtx.currentTime);g.gain.setValueAtTime(0.06,aCtx.currentTime);g.gain.linearRampToValueAtTime(0,aCtx.currentTime+0.08);o.connect(g);g.connect(aCtx.destination);o.start();o.stop(aCtx.currentTime+0.08);}",
    "function pDie(){let o=aCtx.createOscillator(),g=aCtx.createGain();o.type='sawtooth';o.frequency.setValueAtTime(150,aCtx.currentTime);g.gain.setValueAtTime(0.1,aCtx.currentTime);g.gain.linearRampToValueAtTime(0,aCtx.currentTime+0.3);o.connect(g);g.connect(aCtx.destination);o.start();o.stop(aCtx.currentTime+0.3);}",
    "function getSkyColor(){let m=lv%5;if(m===1)return{sky:'#4682B4',sun:'#FFFFE0',gnd:'#228B22',n:false};if(m===2)return{sky:'#FF4500',sun:'#FFD700',gnd:'#556B2F',n:false};if(m===3)return{sky:'#111133',sun:'#FFFACD',gnd:'#006400',n:true};if(m===4)return{sky:'#FFB6C1',sun:'#FFA500',gnd:'#3CB371',n:false};return{sky:'#87CEEB',sun:'#FFD700',gnd:'#32CD32',n:false};}",
    "function generateDecorations(){decorations=[];let types=['tree','light'];for(let i=0;i<4;i++){decorations.push({x:Math.random()*440+20,y:Math.random()>0.5?440:130,type:types[Math.floor(Math.random()*types.length)]});}}generateDecorations();",
    "const ck={x:235,y:445,w:22,h:22,step:34,draw(){ctx.fillStyle='#D2691E';ctx.fillRect(this.x+4,this.y+16,3,7);ctx.fillRect(this.x+15,this.y+16,3,7);ctx.fillStyle='#FF0000';ctx.beginPath();ctx.moveTo(this.x+2,this.y+12);ctx.lineTo(this.x-4,this.y+5);ctx.lineTo(this.x+4,this.y+9);ctx.fill();ctx.fillStyle='#FFF';ctx.beginPath();ctx.arc(this.x+11,this.y+10,10,0,Math.PI*2);ctx.fill();ctx.fillStyle='#F5F5F5';ctx.beginPath();ctx.ellipse(this.x+2,this.y+10,3,5,0,0,Math.PI*2);ctx.fill();ctx.fillStyle='#FF0000';ctx.beginPath();ctx.arc(this.x+11,this.y-2,4,0,Math.PI*2);ctx.fill();ctx.fillStyle='#FFA500';ctx.beginPath();ctx.moveTo(this.x+11,this.y+1);ctx.lineTo(this.x+18,this.y+4);ctx.lineTo(this.x+11,this.y+7);ctx.fill();ctx.fillStyle='#000';ctx.fillRect(this.x+9,this.y+2,2,2);}};",
    "const cars=[{x:0,y:315,w:55,h:24,sp:1.8,c:'#FF4500'},{x:250,y:315,w:55,h:24,sp:1.8,c:'#FF4500'},{x:400,y:245,w:70,h:24,sp:-2.2,c:'#1E90FF'},{x:100,y:245,w:70,h:24,sp:-2.2,c:'#1E90FF'},{x:50,y:175,w:50,h:24,sp:2.6,c:'#BA55D3'}];",
    "function gSp(c) { let inc=(lv-1)*0.22; return c.sp>0?Math.min(c.sp+inc,9.0):Math.max(c.sp-inc,-9.0); }",
    "function resetGame(){ck.x=235;ck.y=445;timeLeft=timeLimit;gWon=false;wScr=false;gLost=false;}",
    "function mUp(){if(wScr||gLost)return;if(ck.y>100)ck.y-=ck.step;pCk();if(ck.y<=140){gWon=true;wScr=true;setTimeout(()=>{lv++;generateDecorations();resetGame();},2000);}}",
    "function mDown(){if(!wScr&&!gLost&&ck.y<445){ck.y+=ck.step;pCk();}}",
    "window.addEventListener('keydown',e=>{if(e.repeat)return;if(e.key==='ArrowUp')mUp();if(e.key==='ArrowDown')mDown();});",
    "document.getElementById('bUp').addEventListener('touchstart',e=>{e.preventDefault();mUp();});",
    "document.getElementById('bDown').addEventListener('touchstart',e=>{e.preventDefault();mDown();});",
    "document.getElementById('bUp').addEventListener('click',e=>{mUp();});",
    "document.getElementById('bDown').addEventListener('click',e=>{mDown();});",
    "function loop(){",
    "let env=getSkyColor();ctx.fillStyle='#87CEEB';ctx.fillRect(0,0,500,500);",
    "let now=Date.now();if(!wScr&&!gLost){let dt=(now-lastTime)/1000;timeLeft-=dt;if(timeLeft<=0){timeLeft=0;gLost=true;pDie();}}lastTime=now;",
    "ctx.fillStyle=env.sky;ctx.fillRect(0,0,500,90);ctx.fillStyle=env.sun;ctx.beginPath();ctx.arc(60,45,20,0,Math.PI*2);ctx.fill();",
    "if(env.n){ctx.fillStyle=env.sky;ctx.beginPath();ctx.arc(72,45,16,0,Math.PI*2);ctx.fill();}",
    "ctx.fillStyle=env.gnd;ctx.fillRect(0,90,500,55);ctx.fillStyle='#3A3A3A';ctx.fillRect(0,145,500,215);ctx.fillStyle=env.gnd;ctx.fillRect(0,360,500,140);",
    "ctx.strokeStyle='rgba(255,255,255,0.85)';ctx.lineWidth=3;for(let y=198;y<350;y+=71){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(500,y);ctx.stroke();}",
    "decorations.forEach(d=>{if(d.type==='tree'){ctx.fillStyle='#8B4513';ctx.fillRect(d.x+4,d.y+10,4,10);ctx.fillStyle='#006400';ctx.beginPath();ctx.arc(d.x+6,d.y+6,10,0,Math.PI*2);ctx.fill();}else if(d.type==='light'){ctx.fillStyle='#111';ctx.fillRect(d.x+4,d.y,4,22);ctx.fillStyle='#222';ctx.fillRect(d.x,d.y-3,12,14);let flash=(Math.floor(Date.now()/400)%3===0)?'#FF0000':'#00FF00';ctx.fillStyle=flash;ctx.beginPath();ctx.arc(d.x+6,d.y+4,3,0,Math.PI*2);ctx.fill();}});",
    "ctx.fillStyle=env.n?'#FFF':'#000';ctx.font='bold 15px Arial';ctx.textAlign='right';ctx.fillText('Màn: '+lv+'/100',480,30);",
    "let barW=(timeLeft/timeLimit)*120;ctx.fillStyle='rgba(0,0,0,0.2)';ctx.fillRect(360,43,120,12);ctx.fillStyle=timeLeft<4?'#FF0000':'#00FF00';ctx.fillRect(360,43,barW,12);ctx.fillStyle=env.n?'#FFF':'#000';ctx.font='11px Arial';ctx.fillText('Thời gian',425,38);",
    "cars.forEach(c=>{let s=gSp(c);if(!wScr&&!gLost){c.x+=s;if(s>0&&c.x>500)c.x=-c.w;if(s<0&&c.x<-c.w)c.x=500;if(ck.x+7<c.x+c.w&&ck.x+ck.w-7>c.x&&ck.y+5<c.y+c.h&&ck.y+ck.h-5>c.y){pDie();resetGame();}}ctx.fillStyle=c.c;ctx.fillRect(c.x,c.y,c.w,c.h);ctx.fillStyle='#E0FFFF';if(s>0){ctx.fillRect(c.x+c.w-12,c.y+3,9,c.h-6);}else{ctx.fillRect(c.x+3,c.y+3,9,c.h-6);}ctx.fillStyle='#111';ctx.fillRect(c.x+6,c.y-4,10,4);ctx.fillRect(c.x+c.w-16,c.y-4,10,4);ctx.fillRect(c.x+6,c.y+c.h,10,4);ctx.fillRect(c.x+c.w-16,c.y+c.h,10,4);ctx.fillStyle='#C0C0C0';ctx.fillRect(c.x+10,c.y-3,2,2);ctx.fillRect(c.x+c.w-12,c.y-3,2,2);});",
    "ck.draw();",
    "if(wScr){ctx.fillStyle='rgba(0,0,0,0.65)';ctx.fillRect(0,0,500,500);ctx.fillStyle='#FFD700';ctx.fillRect(70,170,360,130);ctx.lineWidth=4;ctx.strokeStyle='#FFF';ctx.strokeRect(70,170,360,130);ctx.fillStyle='#000';ctx.font='bold 22px Arial';ctx.textAlign='center';ctx.fillText('🎉 QUA MÀN THÀNH CÔNG! 🎉',250,222);ctx.font='15px Arial';ctx.fillText('Chuẩn bị bước sang Màn '+(lv+1)+'...',250,268);}",
    "if(gLost){ctx.fillStyle='rgba(0,0,0,0.7)';ctx.fillRect(0,0,500,500);ctx.fillStyle='#FF0000';ctx.fillRect(70,170,360,130);ctx.lineWidth=4;ctx.strokeStyle='#FFF';ctx.strokeRect(70,170,360,130);ctx.fillStyle='#FFF';ctx.font='bold 22px Arial';ctx.textAlign='center';ctx.fillText('⏰ HẾT GIỜ RỒI! ⏰',250,225);ctx.font='15px Arial';ctx.fillText('Nhấp vào nút di chuyển để chơi lại',250,268);if(bUpPres||bDnPres||keys['ArrowUp']||keys['ArrowDown']){resetGame();}}",
    "requestAnimationFrame(loop);}",
    "let bUpPres=false,bDnPres=false;document.getElementById('bUp').addEventListener('pointerdown',()=>{bUpPres=true;});document.getElementById('bUp').addEventListener('pointerup',()=>{bUpPres=false;});document.getElementById('bDown').addEventListener('pointerdown',()=>{bDnPres=true;});document.getElementById('bDown').addEventListener('pointerup',()=>{bDnPres=false;});",
    "let keys={};window.addEventListener('keydown',e=>{keys[e.key]=true;});window.addEventListener('keyup',e=>{keys[e.key]=false;});",
    "loop();",
    "</script></body></html>"
]

game_html = xuong_dong.join(game_code)
cp.html(game_html, height=595, width=510)
st.info("💡 Game đã khó hơn: Có thêm 15 giây đếm ngược và tốc độ xe chạy nhanh hơn rất nhiều!")

