import streamlit as st
import streamlit.components.v1 as cp

st.set_page_config(page_title="Game Ga", page_icon="🐔")
st.title("🐔 Trò Chơi: Gà Qua Đường")

game_html = """
<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<style>body{margin:0;display:flex;flex-direction:column;align-items:center;background:#f0f0f0;font-family:sans-serif;}
canvas{border:4px solid #333;background:#87CEEB;border-radius:8px;max-width:100%;}
.btn-box{margin-top:10px;display:flex;gap:20px;}
.btn{width:80px;height:50px;font-size:24px;background:#FFA500;color:#fff;border:none;border-radius:10px;box-shadow:0 4px #cc8400;}</style></head>
<body><canvas id="gCanvas" width="500" height="500"></canvas>
<div class="btn-box"><button class="btn" id="bUp">▲</button><button class="btn" id="bDown">▼</button></div>
<script>
const cv=document.getElementById("gCanvas"),ctx=cv.getContext("2d"),aCtx=new(window.AudioContext||window.webkitAudioContext)();
let lv=1,gWon=false,wScr=false;
setInterval(()=>{if(aCtx.state==='suspended'||wScr)return;let o=aCtx.createOscillator(),g=aCtx.createGain();o.type='triangle';o.frequency.setValueAtTime(260,aCtx.currentTime);g.gain.setValueAtTime(0.015,aCtx.currentTime);g.gain.exponentialRampToValueAtTime(0.001,aCtx.currentTime+0.8);o.connect(g);g.connect(aCtx.destination);o.start();o.stop(aCtx.currentTime+0.8);},1000);
function pS(f,t,d,v){if(aCtx.state==='suspended')aCtx.resume();let o=aCtx.createOscillator(),g=aCtx.createGain();o.type=t;o.frequency.setValueAtTime(f,aCtx.currentTime);g.gain.setValueAtTime(v,aCtx.currentTime);g.gain.linearRampToValueAtTime(0,aCtx.currentTime+d);o.connect(g);g.connect(aCtx.destination);o.start();o.stop(aCtx.currentTime+d);}
function pCk(){pS(400,'sawtooth',0.08,0.06);setTimeout(()=>pS(450,'sawtooth',0.1,0.05),800);}
const ck={x:235,y:450,w:26,h:26,draw(){
ctx.fillStyle="#FFA500";ctx.fillRect(this.x+6,this.y+20,3,6);ctx.fillRect(this.x+17,this.y+20,3,6);
ctx.fillStyle="#FFF";ctx.beginPath();ctx.arc(this.x+13,this.y+13,11,0,Math.PI*2);ctx.fill();
ctx.fillStyle="#FF0000";ctx.beginPath();ctx.arc(this.x+13,this.y-1,4,0,Math.PI*2);ctx.fill();
ctx.fillStyle="#FFA500";ctx.beginPath();ctx.moveTo(this.x+13,this.y+2);ctx.lineTo(this.x+19,this.y+5);ctx.lineTo(this.x+13,this.y+8);ctx.fill();
ctx.fillStyle="#000";ctx.fillRect(this.x+11,this.y+3,2,2);}};
const cars=[{x:0,y:330,w:55,h:32,sp:1.5,c:'#FF4500'},{x:250,y:330,w:55,h:32,sp:1.5,c:'#FF4500'},{x:400,y:260,w:70,h:32,sp:-2,c:'#00F'},{x:100,y:260,w:70,h:32,sp:-2,c:'#00F'},{x:50,y:190,w:50,h:32,sp:2.3,c:'#FFD700'}];
function gSp(c){let inc=(lv-1)*0.18;return c.sp>0?Math.min(c.sp+inc,8.5):Math.max(c.sp-inc,-8.5);}
function mUp(){if(wScr)return;ck.y-=25;pCk();if(ck.y<=90){gWon=true;wScr=true;setTimeout(()=>{lv++;ck.x=235;ck.y=450;gWon=false;wScr=false;},2000);}}
function mDn(){if(!wScr&&ck.y<450)ck.y+=25;}
window.addEventListener("keydown",e=>{if(e.key==="ArrowUp")mUp();if(e.key==="ArrowDown")mDn();});
document.getElementById("bUp").addEventListener("click",mUp);document.getElementById("bDown").addEventListener("click",mDn);
function loop(){
ctx.clearRect(0,0,500,500);
ctx.fillStyle="#FFD700";ctx.beginPath();ctx.arc(50,40,20,0,Math.PI*2);ctx.fill();
ctx.fillStyle="#FFF";ctx.beginPath();ctx.arc(160,35,12,0,Math.PI*2);ctx.arc(175,30,16,0,Math.PI*2);ctx.arc(190,35,12,0,Math.PI*2);ctx.fill();
ctx.fillStyle="#32CD32";ctx.fillRect(0,80,500,50);ctx.fillStyle="#444";ctx.fillRect(0,130,500,250);ctx.fillStyle="#32CD32";ctx.fillRect(0,380,500,120);
ctx.fillStyle="#FFF";ctx.font="bold 16px Arial";ctx.textAlign="right";ctx.fillText("Màn chơi: "+lv+" / 100",480,30);
cars.forEach(c=>{let s=gSp(c);if(!wScr){c.x+=s;if(s>0&&c.x>500)c.x=-c.w;if(s<0&&c.x<-c.w)c.x=500;if(ck.x<c.x+c.w&&ck.x+ck.w>c.x&&ck.y<c.y+c.h&&ck.y+ck.h>c.y){ck.x=235;ck.y=450;}}
ctx.fillStyle=c.c;ctx.fillRect(c.x,c.y,c.w,c.h);ctx.fillStyle="#E0FFFF";if(s>0){ctx.fillRect(c.x+c.w-12,c.y+5,8,c.h-10);}else{ctx.fillRect(c.x+4,c.y+5,8,c.h-10);}
ctx.fillStyle="#000";ctx.fillRect(c.x+6,c.y-3,10,3);ctx.fillRect(c.x+c.w-16,c.y-3,10,3);ctx.fillRect(c.x+6,c.y+c.h,10,3);ctx.fillRect(c.x+c.w-16,c.y+c.h,10,3);});
ck.draw();
if(wScr){ctx.fillStyle="rgba(0,0,0,0.6)";ctx.fillRect(0,0,500,500);ctx.fillStyle="#FFD700";ctx.fillRect(70,170,360,130);ctx.fillStyle="#000";ctx.font="bold 22px Arial";ctx.textAlign="center";ctx.fillText("🎉 QUA MÀN THÀNH CÔNG! 🎉",250,220);ctx.font="16px Arial";ctx.fillText("Chuẩn bị sang Màn "+(lv+1)+"...", 250,265);}
requestAnimationFrame(loop);}loop();
</script></body></html>
"""

cp.html(game_html, height=580, width=510)
st.info("💡 Bấm nút ▲ và ▼ màu cam bên dưới màn hình game để di chuyển chú gà!")

