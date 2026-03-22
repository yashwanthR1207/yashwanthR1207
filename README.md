<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Yashwanth R — EEE Engineer</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet"/>
<style>
  *{margin:0;padding:0;box-sizing:border-box;}
  html,body{width:100%;background:#0d0d0d;display:flex;justify-content:center;align-items:center;min-height:100vh;font-family:'Fira Code',monospace;}
  .banner{width:860px;max-width:100%;background:#0a0a0a;border:1px solid #1a1a1a;border-radius:12px;padding:36px 32px 30px;position:relative;overflow:hidden;}
  .banner::before{content:'';position:absolute;inset:0;background-image:linear-gradient(rgba(0,255,255,0.025) 1px,transparent 1px),linear-gradient(90deg,rgba(0,255,255,0.025) 1px,transparent 1px);background-size:28px 28px;pointer-events:none;}
  .scan{position:absolute;top:0;left:-80%;width:60%;height:100%;background:linear-gradient(90deg,transparent,rgba(0,255,255,0.035),transparent);animation:scan 5s linear infinite;pointer-events:none;z-index:1;}
  @keyframes scan{0%{left:-60%;}100%{left:120%;}}
  .corner{position:absolute;width:22px;height:22px;border-color:#00ffff;border-style:solid;opacity:0.45;}
  .tl{top:10px;left:10px;border-width:2px 0 0 2px;}
  .tr{top:10px;right:10px;border-width:2px 2px 0 0;}
  .bl{bottom:10px;left:10px;border-width:0 0 2px 2px;}
  .br{bottom:10px;right:10px;border-width:0 2px 2px 0;}
  .sig{position:absolute;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,rgba(0,255,255,0.1),transparent);pointer-events:none;}
  .name-wrap{text-align:center;position:relative;z-index:2;margin-bottom:8px;}
  .name{font-family:'Orbitron',monospace;font-weight:900;font-size:clamp(30px,7vw,60px);letter-spacing:0.1em;display:inline-block;position:relative;animation:glitch 8s steps(1) infinite;}
  .name .char{display:inline-block;opacity:0;animation:charIn 0.5s ease forwards;}
  @keyframes charIn{0%{opacity:0;transform:translateY(-14px) skewX(8deg);}60%{opacity:1;transform:translateY(3px) skewX(-3deg);}100%{opacity:1;transform:translateY(0) skewX(0);}}
  .cyan-char{color:#00ffff;text-shadow:0 0 18px rgba(0,255,255,0.5);}
  .orange-char{color:#ff6600;text-shadow:0 0 18px rgba(255,102,0,0.5);}
  @keyframes glitch{0%,94%,100%{filter:none;}95%{filter:hue-rotate(90deg) brightness(1.4);transform:translateX(2px);}96%{filter:none;transform:translateX(0);}97%{filter:hue-rotate(-90deg) brightness(1.2);transform:translateX(-2px);}98%{filter:none;transform:translateX(0);}}
  .subtitle{text-align:center;font-family:'Fira Code',monospace;font-size:12px;font-weight:500;letter-spacing:0.18em;color:#ff6600;margin-bottom:24px;position:relative;z-index:2;opacity:0;animation:fadeUp 0.6s ease 1.2s forwards;}
  @keyframes fadeUp{0%{opacity:0;transform:translateY(8px);}100%{opacity:1;transform:translateY(0);}}
  .circuit-area{position:relative;z-index:2;display:flex;align-items:center;justify-content:center;gap:0;flex-wrap:nowrap;overflow:hidden;opacity:0;animation:fadeUp 0.6s ease 1.5s forwards;}
  .wire{height:2px;background:#1a3a3a;position:relative;display:inline-flex;align-items:center;flex-shrink:0;}
  .wire::after{content:'';position:absolute;top:0;left:0;height:2px;width:100%;background:linear-gradient(90deg,transparent,#00ffff 50%,transparent);background-size:60px 2px;animation:flowR 1.6s linear infinite;}
  @keyframes flowR{0%{background-position:-60px 0;}100%{background-position:60px 0;}}
  .node{width:7px;height:7px;border-radius:50%;background:#00ffff;box-shadow:0 0 8px rgba(0,255,255,0.8);flex-shrink:0;}
  .resistor{width:44px;height:18px;border:1.5px solid #ff6600;border-radius:4px;background:#120800;display:flex;align-items:center;justify-content:center;flex-shrink:0;gap:4px;}
  .band{width:3px;height:11px;border-radius:1px;}
  .capacitor{display:flex;align-items:center;flex-shrink:0;}
  .cap-wire{width:8px;height:2px;background:#1a3a3a;position:relative;}
  .cap-wire::after{content:'';position:absolute;top:0;left:0;height:2px;width:100%;background:linear-gradient(90deg,transparent,#00ffff 50%,transparent);background-size:30px 2px;animation:flowR 1.6s linear infinite;}
  .cap-plate{width:2.5px;height:24px;background:#8a2be2;border-radius:1px;box-shadow:0 0 5px rgba(138,43,226,0.6);}
  .cap-gap{width:6px;}
  .led{width:18px;height:18px;border-radius:50% 50% 50% 50% / 65% 65% 35% 35%;border:1.5px solid #00ff88;background:#001505;flex-shrink:0;animation:ledBlink 1.4s ease-in-out infinite;position:relative;}
  .led::after{content:'';position:absolute;top:-3px;right:-3px;width:5px;height:5px;border-top:1.5px solid #00ff88;border-right:1.5px solid #00ff88;transform:rotate(15deg);}
  @keyframes ledBlink{0%,100%{background:#003010;box-shadow:0 0 8px #00ff88,0 0 16px rgba(0,255,136,0.4);}50%{background:#001005;box-shadow:0 0 3px rgba(0,255,136,0.3);}}
  .ic{width:60px;height:34px;border:1.5px solid #00ffff;background:#020f0f;border-radius:3px;display:flex;align-items:center;justify-content:center;flex-shrink:0;position:relative;}
  .ic-pins{position:absolute;display:flex;flex-direction:column;gap:6px;top:5px;}
  .ic-pins.left{left:-6px;}
  .ic-pins.right{right:-6px;}
  .ic-pin{width:5px;height:2px;background:#00ffff;border-radius:1px;}
  .ic-text{font-family:'Fira Code',monospace;font-size:7.5px;font-weight:600;color:#00ffff;text-align:center;line-height:1.3;letter-spacing:0.05em;}
  .inductor{display:flex;align-items:center;flex-shrink:0;}
  .coil-arc{width:11px;height:11px;border-radius:50%;border-top:2px solid #8a2be2;border-left:2px solid #8a2be2;border-right:2px solid #8a2be2;border-bottom:2px solid transparent;margin-left:-2px;box-shadow:0 -2px 6px rgba(138,43,226,0.4);}
  .mcu{width:50px;height:28px;border:1.5px solid #ff6600;background:#100500;border-radius:2px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
  .mcu-text{font-family:'Fira Code',monospace;font-size:7.5px;font-weight:600;color:#ff6600;letter-spacing:0.08em;}
  .pulse-dot{width:9px;height:9px;border-radius:50%;background:#ff6600;flex-shrink:0;box-shadow:0 0 6px rgba(255,102,0,0.9);animation:pulse 1s ease-in-out infinite;}
  @keyframes pulse{0%,100%{transform:scale(1);opacity:1;}50%{transform:scale(1.7);opacity:0.3;}}
  .osc-wrap{position:relative;z-index:2;margin:18px auto 0;width:320px;height:44px;border:1px solid rgba(0,255,255,0.15);border-radius:4px;background:rgba(0,20,20,0.5);padding:4px;opacity:0;animation:fadeUp 0.6s ease 1.8s forwards;}
  .osc-label{position:absolute;top:3px;left:8px;font-size:8px;color:rgba(0,255,255,0.4);letter-spacing:0.1em;font-family:'Fira Code',monospace;}
  canvas#osc{display:block;width:100%;height:100%;}
  .tags{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin-top:20px;position:relative;z-index:2;opacity:0;animation:fadeUp 0.6s ease 2s forwards;}
  .tag{font-family:'Fira Code',monospace;font-size:10.5px;font-weight:500;padding:4px 11px;border-radius:4px;border:1px solid;letter-spacing:0.06em;transition:transform 0.15s,box-shadow 0.15s;cursor:default;}
  .tag:hover{transform:translateY(-2px);}
  .tc{color:#00ffff;border-color:rgba(0,255,255,0.4);background:rgba(0,255,255,0.06);}
  .tc:hover{box-shadow:0 0 10px rgba(0,255,255,0.3);}
  .to{color:#ff6600;border-color:rgba(255,102,0,0.4);background:rgba(255,102,0,0.06);}
  .to:hover{box-shadow:0 0 10px rgba(255,102,0,0.3);}
  .tp{color:#9a3be8;border-color:rgba(154,59,232,0.4);background:rgba(154,59,232,0.06);}
  .tp:hover{box-shadow:0 0 10px rgba(154,59,232,0.3);}
  .status{display:flex;align-items:center;justify-content:center;gap:8px;margin-top:18px;font-size:10px;color:rgba(255,255,255,0.25);letter-spacing:0.15em;font-family:'Fira Code',monospace;position:relative;z-index:2;opacity:0;animation:fadeUp 0.6s ease 2.2s forwards;}
  .status-dot{width:6px;height:6px;border-radius:50%;background:#00ff88;animation:pulse 2s ease-in-out infinite;}
</style>
</head>
<body>
<div class="banner">
  <div class="corner tl"></div>
  <div class="corner tr"></div>
  <div class="corner bl"></div>
  <div class="corner br"></div>
  <div class="scan"></div>
  <div class="sig" style="top:30%;"></div>
  <div class="sig" style="top:72%;"></div>

  <div class="name-wrap">
    <div class="name" id="nameEl"></div>
  </div>

  <div class="subtitle">[ ELECTRICAL &amp; ELECTRONICS ENGINEER · VVCE MYSORE ]</div>

  <div class="circuit-area">
    <div class="node"></div>
    <div class="wire" style="width:16px;"></div>
    <div class="resistor">
      <div class="band" style="background:#ff0000;"></div>
      <div class="band" style="background:#ff6600;"></div>
      <div class="band" style="background:#8a2be2;"></div>
      <div class="band" style="background:#ffd700;"></div>
    </div>
    <div class="wire" style="width:10px;"></div>
    <div class="node"></div>
    <div class="wire" style="width:10px;"></div>
    <div class="capacitor">
      <div class="cap-wire" style="width:8px;"></div>
      <div class="cap-plate"></div>
      <div class="cap-gap"></div>
      <div class="cap-plate"></div>
      <div class="cap-wire" style="width:8px;"></div>
    </div>
    <div class="node"></div>
    <div class="wire" style="width:10px;"></div>
    <div class="ic">
      <div class="ic-pins left">
        <div class="ic-pin"></div>
        <div class="ic-pin"></div>
        <div class="ic-pin"></div>
      </div>
      <div class="ic-text">ESP<br/>8266</div>
      <div class="ic-pins right">
        <div class="ic-pin"></div>
        <div class="ic-pin"></div>
        <div class="ic-pin"></div>
      </div>
    </div>
    <div class="wire" style="width:10px;"></div>
    <div class="node"></div>
    <div class="wire" style="width:10px;"></div>
    <div class="led"></div>
    <div class="wire" style="width:10px;"></div>
    <div class="node"></div>
    <div class="wire" style="width:10px;"></div>
    <div class="inductor">
      <div class="coil-arc"></div>
      <div class="coil-arc"></div>
      <div class="coil-arc"></div>
      <div class="coil-arc"></div>
    </div>
    <div class="wire" style="width:10px;"></div>
    <div class="node"></div>
    <div class="wire" style="width:10px;"></div>
    <div class="mcu"><div class="mcu-text">MCU</div></div>
    <div class="wire" style="width:10px;"></div>
    <div class="pulse-dot"></div>
    <div class="wire" style="width:16px;"></div>
    <div class="node"></div>
  </div>

  <div class="osc-wrap">
    <div class="osc-label">CH1 · 5V/DIV · 1ms/DIV</div>
    <canvas id="osc" width="310" height="36"></canvas>
  </div>

  <div class="tags">
    <span class="tag tc">IoT</span>
    <span class="tag to">Embedded Systems</span>
    <span class="tag tp">Power Electronics</span>
    <span class="tag tc">ESP8266</span>
    <span class="tag to">Arduino</span>
    <span class="tag tp">NodeMCU</span>
    <span class="tag tc">Automation</span>
    <span class="tag to">Robotics</span>
    <span class="tag tp">MATLAB</span>
    <span class="tag tc">Smart Grid</span>
    <span class="tag to">VVCE Mysore</span>
    <span class="tag tp">PLC</span>
  </div>

  <div class="status">
    <div class="status-dot"></div>
    SYSTEM ONLINE · BUILDING THE FUTURE, ONE CIRCUIT AT A TIME
  </div>
</div>

<script>
const nameText = "YASHWANTH R";
const nameEl = document.getElementById('nameEl');
nameText.split('').forEach((ch, i) => {
  const s = document.createElement('span');
  s.className = 'char ' + (ch === 'R' || ch === ' ' ? 'orange-char' : 'cyan-char');
  s.textContent = ch === ' ' ? '\u00a0' : ch;
  s.style.animationDelay = (i * 0.065) + 's';
  nameEl.appendChild(s);
});

const canvas = document.getElementById('osc');
const ctx = canvas.getContext('2d');
let t = 0;
function drawOsc() {
  const W = canvas.width, H = canvas.height;
  ctx.clearRect(0, 0, W, H);
  ctx.strokeStyle = 'rgba(0,255,255,0.08)';
  ctx.lineWidth = 0.5;
  for (let x = 0; x < W; x += 30) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke(); }
  for (let y = 0; y < H; y += 10) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }
  ctx.strokeStyle = '#00ffff';
  ctx.lineWidth = 1.6;
  ctx.shadowColor = '#00ffff';
  ctx.shadowBlur = 5;
  ctx.beginPath();
  const seg = 38;
  for (let x = 0; x < W; x++) {
    const pos = ((x + t) % seg + seg) % seg;
    let y;
    if (pos < seg * 0.15) y = H * 0.55;
    else if (pos < seg * 0.2)  y = H * 0.15;
    else if (pos < seg * 0.55) y = H * 0.15;
    else if (pos < seg * 0.6)  y = H * 0.85;
    else if (pos < seg * 0.95) y = H * 0.85;
    else y = H * 0.55;
    x === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
  }
  ctx.stroke();
  ctx.shadowBlur = 0;
  ctx.strokeStyle = 'rgba(255,102,0,0.5)';
  ctx.lineWidth = 1;
  ctx.beginPath();
  for (let x = 0; x < W; x++) {
    const y = H / 2 + Math.sin((x + t * 1.5) * 0.2) * (H * 0.28);
    x === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
  }
  ctx.stroke();
  t += 0.7;
  requestAnimationFrame(drawOsc);
}
drawOsc();
</script>
</body>
</html>
