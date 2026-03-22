<div align="center">

<!--CIRCUIT BANNER - works on GitHub via raw HTML-->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com?font=Orbitron&weight=900&size=55&duration=1&pause=10000&color=00FFFF&background=0D0D0Dff&center=true&vCenter=true&repeat=false&width=800&height=150&lines=YASHWANTH+R" />
  <source media="(prefers-color-scheme: light)" srcset="https://readme-typing-svg.demolab.com?font=Orbitron&weight=900&size=55&duration=1&pause=10000&color=0047AB&background=F0F4FFff&center=true&vCenter=true&repeat=false&width=800&height=150&lines=YASHWANTH+R" />
  <img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=900&size=55&duration=1&pause=10000&color=00FFFF&background=0D0D0Dff&center=true&vCenter=true&repeat=false&width=800&height=150&lines=YASHWANTH+R" width="100%" alt="YASHWANTH R" />
</picture>

<br>

<!-- ANIMATED CIRCUIT SVG BANNER -->
<svg width="860" height="110" viewBox="0 0 860 110" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .wire-path { stroke: #1a3a3a; stroke-width: 2; fill: none; }
      .comp-box  { fill: #0a0a0a; stroke-width: 1.5; }
      .label     { font-family: 'Courier New', monospace; font-size: 7px; font-weight: 700; text-anchor: middle; dominant-baseline: middle; }
      .node-dot  { fill: #00ffff; }

      /* Flowing current animations */
      .flow1 { stroke: #00ffff; stroke-width: 2; fill: none; stroke-dasharray: 8 18; animation: dash1 1.4s linear infinite; }
      .flow2 { stroke: #00ffff; stroke-width: 2; fill: none; stroke-dasharray: 8 18; animation: dash2 1.6s linear infinite; }
      .flow3 { stroke: #00ffff; stroke-width: 2; fill: none; stroke-dasharray: 8 18; animation: dash3 1.8s linear infinite; }
      .flow4 { stroke: #ff6600; stroke-width: 2; fill: none; stroke-dasharray: 8 18; animation: dash4 1.5s linear infinite; }
      .flow5 { stroke: #8a2be2; stroke-width: 2; fill: none; stroke-dasharray: 8 18; animation: dash5 1.3s linear infinite; }

      @keyframes dash1 { to { stroke-dashoffset: -26; } }
      @keyframes dash2 { to { stroke-dashoffset: -26; } }
      @keyframes dash3 { to { stroke-dashoffset: -26; } }
      @keyframes dash4 { to { stroke-dashoffset: -26; } }
      @keyframes dash5 { to { stroke-dashoffset: -26; } }

      /* LED blink */
      .led-body { fill: #001505; stroke: #00ff88; stroke-width: 1.5; animation: ledblink 1.4s ease-in-out infinite; }
      @keyframes ledblink {
        0%,100% { fill: #003010; filter: drop-shadow(0 0 4px #00ff88); }
        50%      { fill: #001005; filter: none; }
      }

      /* Pulse dot */
      .pdot { fill: #ff6600; animation: pdot 1s ease-in-out infinite; transform-origin: 812px 55px; }
      @keyframes pdot { 0%,100%{r:5;opacity:1;} 50%{r:9;opacity:0.3;} }

      /* VCC arrow blink */
      .vcc { fill: #00ffff; animation: vccblink 2s ease-in-out infinite; }
      @keyframes vccblink { 0%,100%{opacity:1;} 50%{opacity:0.3;} }

      /* GND */
      .gnd { stroke: #ff6600; stroke-width: 1.5; fill: none; }

      /* Oscilloscope trace */
      .osc-trace { stroke: #00ffff; stroke-width: 1.5; fill: none; stroke-dasharray: 200; animation: osctrace 3s linear infinite; filter: drop-shadow(0 0 2px #00ffff); }
      @keyframes osctrace { 0%{stroke-dashoffset:200;} 100%{stroke-dashoffset:0;} }
      .osc-trace2 { stroke: rgba(255,102,0,0.6); stroke-width: 1; fill: none; stroke-dasharray: 200; animation: osctrace2 4s linear infinite; }
      @keyframes osctrace2 { 0%{stroke-dashoffset:200;} 100%{stroke-dashoffset:0;} }

      /* Corner blink */
      .corner { stroke: #00ffff; stroke-width: 1.5; fill: none; opacity: 0.5; animation: cornerblink 3s ease-in-out infinite; }
      @keyframes cornerblink { 0%,100%{opacity:0.5;} 50%{opacity:0.15;} }

      /* Scan line */
      .scanline { fill: url(#scangrad); animation: scanmove 5s linear infinite; }
      @keyframes scanmove { 0%{transform:translateX(-200px);} 100%{transform:translateX(1100px);} }

      /* Coil arcs pulse */
      .coil { stroke: #8a2be2; stroke-width: 2; fill: none; animation: coilpulse 2s ease-in-out infinite; }
      @keyframes coilpulse { 0%,100%{opacity:1;} 50%{opacity:0.4;} }

      /* Cap plates */
      .cap-plate { stroke: #8a2be2; stroke-width: 3; animation: cappulse 1.8s ease-in-out infinite; }
      @keyframes cappulse { 0%,100%{opacity:1;filter:drop-shadow(0 0 3px #8a2be2);} 50%{opacity:0.5;filter:none;} }
    </style>
    <linearGradient id="scangrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="rgba(0,255,255,0)" />
      <stop offset="50%" stop-color="rgba(0,255,255,0.04)" />
      <stop offset="100%" stop-color="rgba(0,255,255,0)" />
    </linearGradient>
    <!-- PCB grid pattern -->
    <pattern id="pcbgrid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M20 0L0 0L0 20" stroke="rgba(0,255,255,0.04)" stroke-width="0.5" fill="none"/>
    </pattern>
  </defs>

  <!-- Background -->
  <rect width="860" height="110" fill="#0a0a0a" rx="10"/>
  <rect width="860" height="110" fill="url(#pcbgrid)" rx="10"/>

  <!-- Scan line -->
  <rect class="scanline" x="0" y="0" width="160" height="110" rx="0"/>

  <!-- Corner brackets -->
  <path class="corner" d="M14,8 L8,8 L8,22"/>
  <path class="corner" d="M846,8 L852,8 L852,22"/>
  <path class="corner" d="M14,102 L8,102 L8,88"/>
  <path class="corner" d="M846,102 L852,102 L852,88"/>

  <!-- Horizontal signal trace lines (decorative) -->
  <line x1="0" y1="27" x2="860" y2="27" stroke="rgba(0,255,255,0.06)" stroke-width="0.5"/>
  <line x1="0" y1="83" x2="860" y2="83" stroke="rgba(0,255,255,0.06)" stroke-width="0.5"/>

  <!-- ═══════════════════════════════════════════ -->
  <!--        MAIN CIRCUIT — left to right        -->
  <!-- ═══════════════════════════════════════════ -->

  <!-- VCC Power rail at top -->
  <line x1="30" y1="28" x2="830" y2="28" stroke="rgba(0,255,255,0.12)" stroke-width="1" stroke-dasharray="4 8"/>
  <text x="18" y="28" class="label vcc" fill="#00ffff" font-size="6">VCC</text>

  <!-- GND rail at bottom -->
  <line x1="30" y1="82" x2="830" y2="82" stroke="rgba(255,102,0,0.12)" stroke-width="1" stroke-dasharray="4 8"/>
  <text x="18" y="82" class="label" fill="#ff6600" font-size="6">GND</text>

  <!-- ── MAIN HORIZONTAL WIRE (base trace at y=55) ── -->
  <!-- Wire segments with flowing current -->
  <!-- Seg 1: start → resistor -->
  <line x1="28" y1="55" x2="68" y2="55" class="wire-path"/>
  <line x1="28" y1="55" x2="68" y2="55" class="flow1"/>

  <!-- ── RESISTOR (x=68) ── -->
  <rect x="68" y="46" width="44" height="18" class="comp-box" rx="3" stroke="#ff6600"/>
  <!-- color bands -->
  <line x1="77" y1="47" x2="77" y2="63" stroke="#ff0000" stroke-width="3"/>
  <line x1="84" y1="47" x2="84" y2="63" stroke="#ff6600" stroke-width="3"/>
  <line x1="91" y1="47" x2="91" y2="63" stroke="#8a2be2" stroke-width="3"/>
  <line x1="98" y1="47" x2="98" y2="63" stroke="#ffd700" stroke-width="3"/>
  <text x="90" y="71" class="label" fill="#ff6600" font-size="6">4.7kΩ</text>
  <!-- VCC drop line -->
  <line x1="90" y1="46" x2="90" y2="28" stroke="rgba(0,255,255,0.2)" stroke-width="1" stroke-dasharray="2 3"/>

  <!-- Seg 2: resistor → node1 -->
  <line x1="112" y1="55" x2="145" y2="55" class="wire-path"/>
  <line x1="112" y1="55" x2="145" y2="55" class="flow1"/>
  <!-- Node 1 -->
  <circle cx="145" cy="55" r="4" class="node-dot" filter="url(#glow)"/>

  <!-- ── CAPACITOR (x=145) ── -->
  <!-- wire in -->
  <line x1="145" y1="55" x2="165" y2="55" class="wire-path"/>
  <line x1="145" y1="55" x2="165" y2="55" class="flow2"/>
  <!-- plate 1 -->
  <line x1="165" y1="40" x2="165" y2="70" class="cap-plate"/>
  <!-- gap -->
  <!-- plate 2 -->
  <line x1="173" y1="40" x2="173" y2="70" class="cap-plate"/>
  <!-- wire out -->
  <line x1="173" y1="55" x2="193" y2="55" class="wire-path"/>
  <line x1="173" y1="55" x2="193" y2="55" class="flow2"/>
  <!-- GND drop -->
  <line x1="169" y1="70" x2="169" y2="82" stroke="rgba(255,102,0,0.25)" stroke-width="1" stroke-dasharray="2 3"/>
  <text x="169" y="38" class="label" fill="#8a2be2" font-size="6">100μF</text>

  <!-- Node 2 -->
  <circle cx="193" cy="55" r="4" class="node-dot"/>

  <!-- ── ESP8266 IC (x=200) ── -->
  <line x1="193" y1="55" x2="210" y2="55" class="wire-path"/>
  <line x1="193" y1="55" x2="210" y2="55" class="flow3"/>
  <!-- IC body -->
  <rect x="210" y="38" width="70" height="34" class="comp-box" rx="3" stroke="#00ffff" stroke-width="1.5"/>
  <!-- left pins -->
  <line x1="205" y1="45" x2="210" y2="45" stroke="#00ffff" stroke-width="2"/>
  <line x1="205" y1="52" x2="210" y2="52" stroke="#00ffff" stroke-width="2"/>
  <line x1="205" y1="59" x2="210" y2="59" stroke="#00ffff" stroke-width="2"/>
  <line x1="205" y1="66" x2="210" y2="66" stroke="#00ffff" stroke-width="2"/>
  <!-- right pins -->
  <line x1="280" y1="45" x2="285" y2="45" stroke="#00ffff" stroke-width="2"/>
  <line x1="280" y1="52" x2="285" y2="52" stroke="#00ffff" stroke-width="2"/>
  <line x1="280" y1="59" x2="285" y2="59" stroke="#00ffff" stroke-width="2"/>
  <line x1="280" y1="66" x2="285" y2="66" stroke="#00ffff" stroke-width="2"/>
  <!-- IC label -->
  <text x="245" y="52" class="label" fill="#00ffff" font-size="8" font-weight="700">ESP</text>
  <text x="245" y="63" class="label" fill="#00ffff" font-size="8" font-weight="700">8266</text>
  <!-- WiFi symbol -->
  <path d="M237,44 Q245,39 253,44" stroke="#00ffff" stroke-width="1" fill="none" opacity="0.5"/>
  <path d="M234,41 Q245,35 256,41" stroke="#00ffff" stroke-width="0.8" fill="none" opacity="0.3"/>
  <!-- GND + VCC lines -->
  <line x1="245" y1="38" x2="245" y2="28" stroke="rgba(0,255,255,0.2)" stroke-width="1" stroke-dasharray="2 3"/>
  <line x1="245" y1="72" x2="245" y2="82" stroke="rgba(255,102,0,0.2)" stroke-width="1" stroke-dasharray="2 3"/>

  <!-- Seg 3: IC → node3 -->
  <line x1="285" y1="55" x2="318" y2="55" class="wire-path"/>
  <line x1="285" y1="55" x2="318" y2="55" class="flow3"/>
  <circle cx="318" cy="55" r="4" class="node-dot"/>

  <!-- ── LED (x=318) ── -->
  <line x1="318" y1="55" x2="335" y2="55" class="wire-path"/>
  <line x1="318" y1="55" x2="335" y2="55" class="flow4"/>
  <!-- LED body -->
  <ellipse cx="344" cy="55" rx="9" ry="10" class="led-body"/>
  <!-- LED flat edge -->
  <line x1="353" y1="46" x2="353" y2="64" stroke="#00ff88" stroke-width="1.5"/>
  <!-- LED rays -->
  <line x1="357" y1="49" x2="363" y2="44" stroke="#00ff88" stroke-width="1" opacity="0.6"/>
  <line x1="358" y1="55" x2="365" y2="55" stroke="#00ff88" stroke-width="1" opacity="0.6"/>
  <line x1="357" y1="61" x2="363" y2="66" stroke="#00ff88" stroke-width="1" opacity="0.6"/>
  <text x="344" y="71" class="label" fill="#00ff88" font-size="6">LED</text>
  <!-- LED wire out -->
  <line x1="353" y1="55" x2="373" y2="55" class="wire-path"/>
  <line x1="353" y1="55" x2="373" y2="55" class="flow4"/>
  <!-- GND drop -->
  <line x1="344" y1="65" x2="344" y2="82" stroke="rgba(255,102,0,0.25)" stroke-width="1" stroke-dasharray="2 3"/>

  <!-- Node 4 -->
  <circle cx="373" cy="55" r="4" class="node-dot"/>

  <!-- ── INDUCTOR (x=373) ── -->
  <line x1="373" y1="55" x2="386" y2="55" class="wire-path"/>
  <line x1="373" y1="55" x2="386" y2="55" class="flow5"/>
  <!-- Coil arcs -->
  <path d="M386,55 A6,6 0 0,1 398,55" class="coil"/>
  <path d="M398,55 A6,6 0 0,1 410,55" class="coil"/>
  <path d="M410,55 A6,6 0 0,1 422,55" class="coil"/>
  <path d="M422,55 A6,6 0 0,1 434,55" class="coil"/>
  <text x="410" y="71" class="label" fill="#8a2be2" font-size="6">10mH</text>
  <!-- inductor wire out -->
  <line x1="434" y1="55" x2="454" y2="55" class="wire-path"/>
  <line x1="434" y1="55" x2="454" y2="55" class="flow5"/>

  <!-- Node 5 -->
  <circle cx="454" cy="55" r="4" class="node-dot"/>

  <!-- ── ARDUINO UNO IC (x=460) ── -->
  <line x1="454" y1="55" x2="468" y2="55" class="wire-path"/>
  <line x1="454" y1="55" x2="468" y2="55" class="flow1"/>
  <!-- IC body -->
  <rect x="468" y="36" width="80" height="38" class="comp-box" rx="3" stroke="#ff6600" stroke-width="1.5"/>
  <!-- left pins -->
  <line x1="463" y1="44" x2="468" y2="44" stroke="#ff6600" stroke-width="2"/>
  <line x1="463" y1="51" x2="468" y2="51" stroke="#ff6600" stroke-width="2"/>
  <line x1="463" y1="58" x2="468" y2="58" stroke="#ff6600" stroke-width="2"/>
  <line x1="463" y1="65" x2="468" y2="65" stroke="#ff6600" stroke-width="2"/>
  <!-- right pins -->
  <line x1="548" y1="44" x2="553" y2="44" stroke="#ff6600" stroke-width="2"/>
  <line x1="548" y1="51" x2="553" y2="51" stroke="#ff6600" stroke-width="2"/>
  <line x1="548" y1="58" x2="553" y2="58" stroke="#ff6600" stroke-width="2"/>
  <line x1="548" y1="65" x2="553" y2="65" stroke="#ff6600" stroke-width="2"/>
  <!-- pin labels top/bottom -->
  <line x1="480" y1="36" x2="480" y2="31" stroke="#ff6600" stroke-width="1.5"/>
  <line x1="490" y1="36" x2="490" y2="31" stroke="#ff6600" stroke-width="1.5"/>
  <line x1="500" y1="36" x2="500" y2="31" stroke="#ff6600" stroke-width="1.5"/>
  <line x1="510" y1="36" x2="510" y2="31" stroke="#ff6600" stroke-width="1.5"/>
  <line x1="520" y1="36" x2="520" y2="31" stroke="#ff6600" stroke-width="1.5"/>
  <line x1="530" y1="36" x2="530" y2="31" stroke="#ff6600" stroke-width="1.5"/>
  <line x1="480" y1="74" x2="480" y2="79" stroke="#ff6600" stroke-width="1.5"/>
  <line x1="490" y1="74" x2="490" y2="79" stroke="#ff6600" stroke-width="1.5"/>
  <line x1="500" y1="74" x2="500" y2="79" stroke="#ff6600" stroke-width="1.5"/>
  <line x1="510" y1="74" x2="510" y2="79" stroke="#ff6600" stroke-width="1.5"/>
  <!-- IC label -->
  <text x="508" y="51" class="label" fill="#ff6600" font-size="7.5" font-weight="700">ARDUINO</text>
  <text x="508" y="62" class="label" fill="#ff6600" font-size="7.5" font-weight="700">UNO</text>
  <!-- VCC/GND -->
  <line x1="508" y1="36" x2="508" y2="28" stroke="rgba(0,255,255,0.2)" stroke-width="1" stroke-dasharray="2 3"/>
  <line x1="508" y1="74" x2="508" y2="82" stroke="rgba(255,102,0,0.2)" stroke-width="1" stroke-dasharray="2 3"/>

  <!-- Seg after arduino -->
  <line x1="553" y1="55" x2="583" y2="55" class="wire-path"/>
  <line x1="553" y1="55" x2="583" y2="55" class="flow2"/>
  <circle cx="583" cy="55" r="4" class="node-dot"/>

  <!-- ── TRANSISTOR / MOSFET symbol (x=583) ── -->
  <line x1="583" y1="55" x2="597" y2="55" class="wire-path"/>
  <line x1="583" y1="55" x2="597" y2="55" class="flow3"/>
  <!-- transistor gate line (vertical) -->
  <line x1="597" y1="43" x2="597" y2="67" stroke="#8a2be2" stroke-width="2"/>
  <!-- gate horizontal -->
  <line x1="590" y1="55" x2="597" y2="55" stroke="#8a2be2" stroke-width="1.5"/>
  <!-- drain -->
  <line x1="597" y1="46" x2="611" y2="46" stroke="#8a2be2" stroke-width="1.5"/>
  <line x1="611" y1="46" x2="611" y2="55" stroke="#8a2be2" stroke-width="1.5"/>
  <!-- source -->
  <line x1="597" y1="64" x2="611" y2="64" stroke="#8a2be2" stroke-width="1.5"/>
  <line x1="611" y1="64" x2="611" y2="55" stroke="#8a2be2" stroke-width="1.5"/>
  <!-- arrow -->
  <polygon points="607,53 611,55 607,57" fill="#8a2be2"/>
  <text x="601" y="76" class="label" fill="#8a2be2" font-size="6">MOSFET</text>

  <!-- wire from drain out -->
  <line x1="611" y1="55" x2="635" y2="55" class="wire-path"/>
  <line x1="611" y1="55" x2="635" y2="55" class="flow3"/>

  <!-- Node 6 -->
  <circle cx="635" cy="55" r="4" class="node-dot"/>

  <!-- ── OSCILLOSCOPE BOX (x=640) ── -->
  <line x1="635" y1="55" x2="648" y2="55" class="wire-path"/>
  <line x1="635" y1="55" x2="648" y2="55" class="flow4"/>
  <rect x="648" y="38" width="72" height="34" class="comp-box" rx="3" stroke="#00ffff" stroke-width="1.5"/>
  <!-- osc screen inner -->
  <rect x="652" y="42" width="64" height="26" fill="#001a1a" rx="2"/>
  <!-- osc grid -->
  <line x1="668" y1="42" x2="668" y2="68" stroke="rgba(0,255,255,0.1)" stroke-width="0.5"/>
  <line x1="684" y1="42" x2="684" y2="68" stroke="rgba(0,255,255,0.1)" stroke-width="0.5"/>
  <line x1="700" y1="42" x2="700" y2="68" stroke="rgba(0,255,255,0.1)" stroke-width="0.5"/>
  <line x1="652" y1="52" x2="716" y2="52" stroke="rgba(0,255,255,0.1)" stroke-width="0.5"/>
  <line x1="652" y1="60" x2="716" y2="60" stroke="rgba(0,255,255,0.1)" stroke-width="0.5"/>
  <!-- oscilloscope square wave trace -->
  <polyline class="osc-trace" points="654,62 662,62 662,48 672,48 672,62 682,62 682,48 692,48 692,62 702,62 702,48 712,48 712,62 714,62"/>
  <!-- sine trace -->
  <path class="osc-trace2" d="M654,56 Q659,46 664,56 Q669,66 674,56 Q679,46 684,56 Q689,66 694,56 Q699,46 704,56 Q709,66 714,56"/>
  <text x="684" y="80" class="label" fill="#00ffff" font-size="5.5">OSC · 5V/div</text>
  <!-- osc wire in/out pins -->
  <line x1="643" y1="48" x2="648" y2="48" stroke="#00ffff" stroke-width="1.5"/>
  <line x1="643" y1="62" x2="648" y2="62" stroke="#00ffff" stroke-width="1.5"/>

  <!-- Seg after osc -->
  <line x1="720" y1="55" x2="750" y2="55" class="wire-path"/>
  <line x1="720" y1="55" x2="750" y2="55" class="flow5"/>

  <!-- Node 7 -->
  <circle cx="750" cy="55" r="4" class="node-dot"/>

  <!-- ── MCU CHIP (x=755) ── -->
  <line x1="750" y1="55" x2="762" y2="55" class="wire-path"/>
  <line x1="750" y1="55" x2="762" y2="55" class="flow1"/>
  <rect x="762" y="44" width="44" height="22" class="comp-box" rx="2" stroke="#ff6600" stroke-width="1.5"/>
  <!-- notch -->
  <path d="M762,44 Q784,40 806,44" stroke="#ff6600" stroke-width="1" fill="none" opacity="0.5"/>
  <!-- pins top/bottom -->
  <line x1="770" y1="44" x2="770" y2="39" stroke="#ff6600" stroke-width="1.5"/>
  <line x1="778" y1="44" x2="778" y2="39" stroke="#ff6600" stroke-width="1.5"/>
  <line x1="786" y1="44" x2="786" y2="39" stroke="#ff6600" stroke-width="1.5"/>
  <line x1="794" y1="44" x2="794" y2="39" stroke="#ff6600" stroke-width="1.5"/>
  <line x1="770" y1="66" x2="770" y2="71" stroke="#ff6600" stroke-width="1.5"/>
  <line x1="778" y1="66" x2="778" y2="71" stroke="#ff6600" stroke-width="1.5"/>
  <line x1="786" y1="66" x2="786" y2="71" stroke="#ff6600" stroke-width="1.5"/>
  <line x1="794" y1="66" x2="794" y2="71" stroke="#ff6600" stroke-width="1.5"/>
  <text x="784" y="57" class="label" fill="#ff6600" font-size="7" font-weight="700">MCU</text>

  <!-- final wire + pulse dot -->
  <line x1="806" y1="55" x2="820" y2="55" class="wire-path"/>
  <line x1="806" y1="55" x2="820" y2="55" class="flow2"/>
  <circle cx="826" cy="55" r="5" class="pdot"/>

  <!-- ── VCC / GND LABELS ── -->
  <text x="30" y="24" class="label vcc" fill="#00ffff" font-size="6.5">+5V</text>
  <text x="30" y="91" class="label" fill="#ff6600" font-size="6.5">GND</text>

  <!-- Status dot -->
  <circle cx="845" cy="20" r="4" fill="#00ff88">
    <animate attributeName="opacity" values="1;0.2;1" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text x="836" y="34" class="label" fill="rgba(0,255,255,0.4)" font-size="5.5">LIVE</text>
</svg>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=3000&pause=1000&color=FF6600&center=true&vCenter=true&width=650&lines=Electrical+and+Electronics+Engineer;Student+at+VVCE+Mysore;IoT+%7C+Embedded+Systems+%7C+Automation;Turning+Circuits+into+Intelligence" />
  <source media="(prefers-color-scheme: light)" srcset="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=3000&pause=1000&color=0047AB&center=true&vCenter=true&width=650&lines=Electrical+and+Electronics+Engineer;Student+at+VVCE+Mysore;IoT+%7C+Embedded+Systems+%7C+Automation;Turning+Circuits+into+Intelligence" />
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=3000&pause=1000&color=FF6600&center=true&vCenter=true&width=650&lines=Electrical+and+Electronics+Engineer;Student+at+VVCE+Mysore;IoT+%7C+Embedded+Systems+%7C+Automation;Turning+Circuits+into+Intelligence" alt="Typing SVG" />
</picture>

<br><br>

<a href="https://www.linkedin.com/in/yashwanth-r-7855a7395">
<img src="https://img.shields.io/badge/LINKEDIN-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
</a>
<img src="https://img.shields.io/badge/VVCE%20MYSORE-FF6600?style=for-the-badge&logoColor=white" />
<img src="https://img.shields.io/badge/B.E.%20EEE-8A2BE2?style=for-the-badge&logoColor=white" />
<img src="https://komarev.com/ghpvc/?username=yashwanthR1207&style=for-the-badge&color=00FFFF&label=PROFILE+VIEWS" />

</div>

---

## SYSTEM IDENTITY
```
NAME        : Yashwanth R
ROLE        : EEE Engineer | IoT Developer | Hardware Builder | Student
LOCATION    : Mysore, Karnataka, India
INSTITUTION : Vidyavardhaka College of Engineering, Mysore
STATUS      : [ ONLINE ] — Building the future, one circuit at a time
INTERESTS   : IoT · Embedded Systems · Power Electronics · Automation
MISSION     : Merging hardware and firmware to solve real-world problems, ROBOTICS
```

---

## ABOUT ME

> *"TURNING IDEAS INTO ENERGY"*

I am a **B.E. Electrical and Electronics Engineering** student at **VVCE Mysore** who lives at the intersection of hardware design, embedded firmware, and IoT automation.

I do not just study how circuits work — I build systems that **sense, think, and respond** to the real world. From smart warehouse automation to IoT-based home control systems, I turn ideas into working hardware.

My mission is simple — bridge the gap between hardware and software through disciplined engineering, clean code, and creative problem solving.

- Currently building **IoT automation and smart energy systems**
- Hands-on with **ESP8266, Arduino, NodeMCU, and sensor integration**
- Exploring **power systems, PLC programming, and smart grid technologies**
- Open to **internships, collaborations, and real-world project challenges**

---

## GIT STATS

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=yashwanthR1207&show_icons=true&hide_border=false&border_color=00FFFF&bg_color=0d0d0d&title_color=00FFFF&icon_color=FF6600&text_color=ffffff" />
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-stats.vercel.app/api?username=yashwanthR1207&show_icons=true&hide_border=false&border_color=0047AB&bg_color=ffffff&title_color=0047AB&icon_color=FF6600&text_color=1a1a1a" />
  <img width="49%" src="https://github-readme-stats.vercel.app/api?username=yashwanthR1207&show_icons=true&hide_border=false&border_color=00FFFF&bg_color=0d0d0d&title_color=00FFFF&icon_color=FF6600&text_color=ffffff" />
</picture>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-streak-stats.herokuapp.com/?user=yashwanthR1207&hide_border=false&border=00FFFF&background=0d0d0d&stroke=00FFFF&ring=FF6600&fire=FF6600&currStreakLabel=ffffff&sideLabels=00FFFF&dates=ffffff" />
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-streak-stats.herokuapp.com/?user=yashwanthR1207&hide_border=false&border=0047AB&background=ffffff&stroke=0047AB&ring=FF6600&fire=FF6600&currStreakLabel=1a1a1a&sideLabels=0047AB&dates=1a1a1a" />
  <img width="49%" src="https://github-readme-streak-stats.herokuapp.com/?user=yashwanthR1207&hide_border=false&border=00FFFF&background=0d0d0d&stroke=00FFFF&ring=FF6600&fire=FF6600&currStreakLabel=ffffff&sideLabels=00FFFF&dates=ffffff" />
</picture>

<br><br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=yashwanthR1207&layout=compact&hide_border=false&border_color=8A2BE2&bg_color=0d0d0d&title_color=8A2BE2&text_color=ffffff" />
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=yashwanthR1207&layout=compact&hide_border=false&border_color=8A2BE2&bg_color=ffffff&title_color=8A2BE2&text_color=1a1a1a" />
  <img width="42%" src="https://github-readme-stats.vercel.app/api/top-langs/?username=yashwanthR1207&layout=compact&hide_border=false&border_color=8A2BE2&bg_color=0d0d0d&title_color=8A2BE2&text_color=ffffff" />
</picture>

</div>

---

## TECHNOLOGY STACK

![C](https://img.shields.io/badge/C-00FFFF?style=flat-square&logo=c&logoColor=black)
![C++](https://img.shields.io/badge/C%2B%2B-FF6600?style=flat-square&logo=cplusplus&logoColor=white)
![Embedded C](https://img.shields.io/badge/Embedded%20C-00FFFF?style=flat-square&logoColor=black)
![MATLAB](https://img.shields.io/badge/MATLAB-FF6600?style=flat-square&logo=mathworks&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-8A2BE2?style=flat-square&logo=arduino&logoColor=white)
![ESP8266](https://img.shields.io/badge/ESP8266-00FFFF?style=flat-square&logo=arduino&logoColor=black)
![NodeMCU](https://img.shields.io/badge/NodeMCU-FF6600?style=flat-square&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-8A2BE2?style=flat-square&logo=raspberrypi&logoColor=white)
![Blynk IoT](https://img.shields.io/badge/Blynk%20IoT-00FFFF?style=flat-square&logoColor=black)
![Circuit Design](https://img.shields.io/badge/Circuit%20Design-FF6600?style=flat-square&logoColor=white)
![Power Electronics](https://img.shields.io/badge/Power%20Electronics-8A2BE2?style=flat-square&logoColor=white)
![AutoCAD Electrical](https://img.shields.io/badge/AutoCAD%20Electrical-FF6600?style=flat-square&logoColor=white)
![Git](https://img.shields.io/badge/Git-00FFFF?style=flat-square&logo=git&logoColor=black)
![GitHub](https://img.shields.io/badge/GitHub-FF6600?style=flat-square&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-8A2BE2?style=flat-square&logo=visualstudiocode&logoColor=white)
![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-00FFFF?style=flat-square&logo=arduino&logoColor=black)

---

## FEATURED PROJECTS

| # | Project | Description | Stack |
|:---:|:---|:---|:---:|
| 01 | **IoT Godown Automation** | Smart cotton warehouse with fire, moisture and occupancy monitoring | ESP8266, Blynk, C++ |
| 02 | **Smart Home Automation** | Multi-sensor home system with live web dashboard and auto control | ESP8266, Arduino, HTTP |
| 03 | **INDUSTRY** | Real-time Industry problem solving using embedded system | Embedded C, Sensors |

---

## CURRENTLY WORKING ON
```
Smart Energy Monitoring System    
IoT-Based Load Controller         
MATLAB Power System Simulation
Robotics
ROBO COMPETITIONS     
GitHub Portfolio Cleanup         
```

---

## OPEN TO

![Internships](https://img.shields.io/badge/Open%20To-Internships-00FFFF?style=flat-square&logoColor=black)
![Collaborations](https://img.shields.io/badge/Open%20To-Collaborations-FF6600?style=flat-square&logoColor=white)
![Tech Talks](https://img.shields.io/badge/Open%20To-Tech%20Talks-8A2BE2?style=flat-square&logoColor=white)
![Location](https://img.shields.io/badge/Location-Mysore%2C%20Karnataka-0047AB?style=flat-square&logoColor=white)

---

<div align="center">

*If you found my work useful — drop a star and let us build something great together.*

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=0:0d0d0d,50:161616,100:0d0d0d&height=120&section=footer" />
  <source media="(prefers-color-scheme: light)" srcset="https://capsule-render.vercel.app/api?type=waving&color=0:f0f4ff,50:e8f0fe,100:f0f4ff&height=120&section=footer" />
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0d0d0d,50:161616,100:0d0d0d&height=120&section=footer" />
</picture>

</div>
