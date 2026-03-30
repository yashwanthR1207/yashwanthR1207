<div align="center">

<svg viewBox="0 0 800 220" xmlns="http://www.w3.org/2000/svg" width="100%">
  <defs>
    <style>
      @keyframes glitch-main {
        0%, 90%, 100% { transform: translate(0,0); }
        91% { transform: translate(-3px, 1px); }
        93% { transform: translate(3px, -1px); }
        95% { transform: translate(-2px, 0); }
        97% { transform: translate(0, 2px); }
      }
      @keyframes glitch-cyan {
        0%, 85%, 100% { opacity: 0; transform: translate(0,0); }
        86% { opacity: 0.45; transform: translate(5px, 0); }
        88% { opacity: 0.45; transform: translate(-5px, 0); }
        90% { opacity: 0; }
      }
      @keyframes glitch-orange {
        0%, 87%, 100% { opacity: 0; transform: translate(0,0); }
        88% { opacity: 0.35; transform: translate(-4px, 2px); }
        90% { opacity: 0.35; transform: translate(4px, -2px); }
        92% { opacity: 0; }
      }
      @keyframes underline-grow {
        0% { stroke-dashoffset: 500; }
        100% { stroke-dashoffset: 0; }
      }
      @keyframes circuit-in {
        0% { stroke-dashoffset: 200; opacity: 0; }
        100% { stroke-dashoffset: 0; opacity: 0.5; }
      }
      @keyframes dot-blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.1; }
      }
      @keyframes cursor-blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0; }
      }
      .name-main {
        font-family: 'Courier New', Courier, monospace;
        font-weight: 900;
        font-size: 74px;
        letter-spacing: 12px;
        fill: #ffffff;
        animation: glitch-main 7s infinite;
      }
      .name-cyan {
        font-family: 'Courier New', Courier, monospace;
        font-weight: 900;
        font-size: 74px;
        letter-spacing: 12px;
        fill: #00FFFF;
        animation: glitch-cyan 7s infinite 0.04s;
      }
      .name-orange {
        font-family: 'Courier New', Courier, monospace;
        font-weight: 900;
        font-size: 74px;
        letter-spacing: 12px;
        fill: #FF6600;
        animation: glitch-orange 7s infinite 0.08s;
      }
      .circuit {
        fill: none;
        stroke: #00FFFF;
        stroke-width: 1;
        stroke-dasharray: 200;
        animation: circuit-in 1.8s ease-out both;
      }
      .dot-blink { animation: dot-blink 1.5s infinite; }
      .cursor { animation: cursor-blink 1s infinite; }
      .underline {
        stroke: #FF6600;
        stroke-width: 2.5;
        stroke-dasharray: 500;
        stroke-dashoffset: 500;
        fill: none;
        animation: underline-grow 1.5s ease-out 0.6s forwards;
      }
    </style>
  </defs>

  <rect width="800" height="220" fill="#0D0D0D" rx="8"/>

  <line x1="0" y1="110" x2="800" y2="110" stroke="#ffffff" stroke-width="0.3" opacity="0.06"/>
  <line x1="400" y1="0" x2="400" y2="220" stroke="#ffffff" stroke-width="0.3" opacity="0.06"/>

  <path class="circuit" d="M50 55 L50 95 L90 95" style="animation-delay:0.2s"/>
  <path class="circuit" d="M50 165 L50 130 L90 130" style="animation-delay:0.4s"/>
  <path class="circuit" d="M90 95 L90 130" stroke="#00FFFF" stroke-width="1" fill="none" stroke-dasharray="40" opacity="0.25" style="animation: circuit-in 1.8s ease-out 0.6s both"/>
  <circle cx="90" cy="95" r="3" fill="#00FFFF" class="dot-blink" style="animation-delay:0.5s"/>
  <circle cx="90" cy="130" r="3" fill="#FF6600" class="dot-blink" style="animation-delay:1.1s"/>

  <path class="circuit" d="M750 55 L750 95 L710 95" style="animation-delay:0.3s"/>
  <path class="circuit" d="M750 165 L750 130 L710 130" style="animation-delay:0.5s"/>
  <path class="circuit" d="M710 95 L710 130" stroke="#00FFFF" stroke-width="1" fill="none" stroke-dasharray="40" opacity="0.25" style="animation: circuit-in 1.8s ease-out 0.7s both"/>
  <circle cx="710" cy="95" r="3" fill="#00FFFF" class="dot-blink" style="animation-delay:0.8s"/>
  <circle cx="710" cy="130" r="3" fill="#FF6600" class="dot-blink" style="animation-delay:1.4s"/>

  <text x="108" y="135" font-family="Courier New, monospace" font-size="80" font-weight="200" fill="#FF6600" opacity="0.18">[</text>
  <text x="654" y="135" font-family="Courier New, monospace" font-size="80" font-weight="200" fill="#FF6600" opacity="0.18">]</text>

  <text x="400" y="133" class="name-cyan" text-anchor="middle">YASHWANTH R</text>
  <text x="400" y="133" class="name-orange" text-anchor="middle">YASHWANTH R</text>
  <text x="400" y="133" class="name-main" text-anchor="middle">YASHWANTH R</text>

  <rect x="675" y="106" width="3.5" height="34" fill="#00FFFF" class="cursor"/>
  <line x1="115" y1="149" x2="685" y2="149" class="underline"/>

  <text x="400" y="50" font-family="Courier New, monospace" font-size="11" fill="#00FFFF" text-anchor="middle" letter-spacing="4" opacity="0.85">// EEE ENGINEER · IoT · ROBOTICS</text>
  <text x="400" y="183" font-family="Courier New, monospace" font-size="11" fill="#8A2BE2" text-anchor="middle" letter-spacing="3" opacity="0.9">TURNING CIRCUITS INTO INTELLIGENCE</text>

  <circle cx="118" cy="52" r="2" fill="#00FFFF" opacity="0.5"/>
  <circle cx="682" cy="52" r="2" fill="#00FFFF" opacity="0.5"/>
  <circle cx="118" cy="180" r="2" fill="#FF6600" opacity="0.5"/>
  <circle cx="682" cy="180" r="2" fill="#FF6600" opacity="0.5"/>
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

## STREAK STATS

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=yashwanthR1207&theme=dark&hide_border=false&border=FF6600&background=0D0D0D&stroke=00FFFF&ring=FF6600&fire=FF6600&currStreakNum=00FFFF&sideNums=ffffff&currStreakLabel=FF6600&sideLabels=00FFFF&dates=888888&date_format=j+M%5B+Y%5D&mode=weekly&card_width=800" />
  <source media="(prefers-color-scheme: light)" srcset="https://streak-stats.demolab.com?user=yashwanthR1207&theme=default&hide_border=false&border=0047AB&background=F0F4FF&stroke=0047AB&ring=FF6600&fire=FF6600&currStreakNum=0047AB&sideNums=1a1a1a&currStreakLabel=FF6600&sideLabels=0047AB&dates=555555&date_format=j+M%5B+Y%5D&mode=weekly&card_width=800" />
  <img width="80%" src="https://streak-stats.demolab.com?user=yashwanthR1207&theme=dark&hide_border=false&border=FF6600&background=0D0D0D&stroke=00FFFF&ring=FF6600&fire=FF6600&currStreakNum=00FFFF&sideNums=ffffff&currStreakLabel=FF6600&sideLabels=00FFFF&dates=888888&date_format=j+M%5B+Y%5D&mode=weekly&card_width=800" alt="GitHub Streak Stats" />
</picture>

</div>

---

## CONTRIBUTION GRAPH

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=yashwanthR1207&bg_color=0d0d0d&color=00FFFF&line=FF6600&point=ffffff&area=true&hide_border=false&border_color=00FFFF" />
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=yashwanthR1207&bg_color=ffffff&color=0047AB&line=FF6600&point=0047AB&area=true&hide_border=false&border_color=0047AB" />
  <img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=yashwanthR1207&bg_color=0d0d0d&color=00FFFF&line=FF6600&point=ffffff&area=true&hide_border=false&border_color=00FFFF" />
</picture>

</div>

---

## TECHNOLOGY STACK

**Languages**

![C](https://img.shields.io/badge/C-00FFFF?style=flat-square&logo=c&logoColor=black)
![C++](https://img.shields.io/badge/C%2B%2B-FF6600?style=flat-square&logo=cplusplus&logoColor=white)
![Embedded C](https://img.shields.io/badge/Embedded%20C-00FFFF?style=flat-square&logo=c&logoColor=black)
![MATLAB](https://img.shields.io/badge/MATLAB-FF6600?style=flat-square&logo=mathworks&logoColor=white)

**Hardware & Microcontrollers**

![Arduino](https://img.shields.io/badge/Arduino-8A2BE2?style=flat-square&logo=arduino&logoColor=white)
![ESP8266](https://img.shields.io/badge/ESP8266-00FFFF?style=flat-square&logo=espressif&logoColor=black)
![NodeMCU](https://img.shields.io/badge/NodeMCU-FF6600?style=flat-square&logo=espressif&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-8A2BE2?style=flat-square&logo=raspberrypi&logoColor=white)

**IoT & Automation**

![Blynk IoT](https://img.shields.io/badge/Blynk%20IoT-00FFFF?style=flat-square&logo=blynk&logoColor=black)
![MQTT](https://img.shields.io/badge/MQTT-FF6600?style=flat-square&logo=mqtt&logoColor=white)
![Home Assistant](https://img.shields.io/badge/Home%20Assistant-8A2BE2?style=flat-square&logo=homeassistant&logoColor=white)

**Design & Electronics**

![Circuit Design](https://img.shields.io/badge/Circuit%20Design-FF6600?style=flat-square&logo=circuitverse&logoColor=white)
![Power Electronics](https://img.shields.io/badge/Power%20Electronics-8A2BE2?style=flat-square&logo=electron&logoColor=white)
![AutoCAD Electrical](https://img.shields.io/badge/AutoCAD%20Electrical-FF6600?style=flat-square&logo=autodesk&logoColor=white)
![KiCad](https://img.shields.io/badge/KiCad-00FFFF?style=flat-square&logo=kicad&logoColor=black)

**Tools & Dev**

![Git](https://img.shields.io/badge/Git-00FFFF?style=flat-square&logo=git&logoColor=black)
![GitHub](https://img.shields.io/badge/GitHub-FF6600?style=flat-square&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-8A2BE2?style=flat-square&logo=visualstudiocode&logoColor=white)
![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-00FFFF?style=flat-square&logo=arduino&logoColor=black)
![Linux](https://img.shields.io/badge/Linux-FF6600?style=flat-square&logo=linux&logoColor=white)

---

## FEATURED PROJECTS

| # | Project | Description | Stack |
|:---:|:---|:---|:---:|
| 01 | **IoT Godown Automation** | Smart cotton warehouse with fire, moisture and occupancy monitoring | ESP8266, Blynk, C++ |
| 02 | **Smart Home Automation** | Multi-sensor home system with live web dashboard and auto control | ESP8266, Arduino, HTTP |
| 03 | **Industry Solver** | Real-time industry problem solving using embedded systems | Arduino, C++ |
| 04 | **ROBOsoccer** | Competitive robot soccer bot with tank drive and RC control | Arduino, BTS7960, FlySky |
| 05 | **ROBOsoccer Version 2** | Competitive robot soccer bot with tank drive and RC control | Arduino, BTS7960, FlySky two channel control |

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
![Location](https://img.shields.io/badge/Location-Mysore%2C%20Karnataka-0047AB?style=flat-square&logo=googlemaps&logoColor=white)

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
