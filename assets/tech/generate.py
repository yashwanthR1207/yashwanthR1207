import urllib.request
import re
import os

icons = [
    # Programming (Cyan/Blue)
    ("c", "C", "#00e5ff", "#0077ff"),
    ("cplusplus", "C++", "#00e5ff", "#0077ff"),
    ("python", "Python", "#00e5ff", "#0077ff"),
    ("matlab", "MATLAB", "#00e5ff", "#0077ff"),
    ("pandas", "Data", "#00e5ff", "#0077ff"),
    
    # Embedded (Purple/Pink)
    ("arduino", "Arduino", "#b500ff", "#5000ff"),
    ("espressif", "ESP32", "#b500ff", "#5000ff"),
    ("raspberrypi", "Raspberry Pi", "#b500ff", "#5000ff"),
    
    # Electronics (Orange/Gold)
    ("altiumdesigner", "PCB", "#ff3b00", "#ff9a00"),
    ("circuitverse", "Circuits", "#ff3b00", "#ff9a00"),
    ("ros", "Robotics", "#ff3b00", "#ff9a00"),
    
    # Dev Tools (Green/Teal)
    ("git", "Git", "#00ff88", "#0099ff"),
    ("linux", "Linux", "#00ff88", "#0099ff"),
    ("docker", "Docker", "#00ff88", "#0099ff"),
    ("postman", "Postman", "#00ff88", "#0099ff")
]

def get_icon_path(slug):
    url = f"https://cdn.simpleicons.org/{slug}/white"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            paths = "".join(re.findall(r'<path[^>]*>', data))
            return paths
    except Exception as e:
        print(f"Error fetching {slug}: {e}")
        return ""

def generate_svg(slug, name, color1, color2):
    paths = get_icon_path(slug)
    
    svg = f"""<svg width="240" height="260" viewBox="0 0 240 260" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad_{slug}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{color1}" stop-opacity="0.15" />
      <stop offset="100%" stop-color="{color2}" stop-opacity="0.02" />
    </linearGradient>
    <linearGradient id="border_{slug}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{color1}" stop-opacity="0.9" />
      <stop offset="100%" stop-color="{color2}" stop-opacity="0.3" />
    </linearGradient>
    <linearGradient id="glowGrad_{slug}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{color1}" stop-opacity="0.6" />
      <stop offset="100%" stop-color="{color2}" stop-opacity="0.2" />
    </linearGradient>
    
    <filter id="neon_text_{slug}" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="blur1" />
      <feMerge>
        <feMergeNode in="blur1" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="neon_logo_{slug}" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur1" />
      <feGaussianBlur in="SourceGraphic" stdDeviation="12" result="blur2" />
      <feMerge>
        <feMergeNode in="blur2" />
        <feMergeNode in="blur1" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <g>
    <!-- Master Floating Animation -->
    <animateTransform attributeName="transform" type="translate" values="0,2; 0,-8; 0,2" dur="4s" repeatCount="indefinite" />
    
    <!-- Outer Glow Behind Card -->
    <rect x="25" y="25" width="190" height="210" rx="20" fill="url(#glowGrad_{slug})" filter="blur(20px)">
      <animate attributeName="opacity" values="0.4; 0.8; 0.4" dur="3s" repeatCount="indefinite" />
    </rect>

    <!-- Glassmorphism Card Base -->
    <rect x="25" y="25" width="190" height="210" rx="20" fill="#0D1117" stroke="url(#border_{slug})" stroke-width="2" />
    <rect x="25" y="25" width="190" height="210" rx="20" fill="url(#grad_{slug})" />

    <!-- Animated Particle Rings -->
    <circle cx="120" cy="110" r="50" fill="none" stroke="{color1}" stroke-width="1" stroke-dasharray="4 8" opacity="0.3">
      <animateTransform attributeName="transform" type="rotate" values="0 120 110; 360 120 110" dur="20s" repeatCount="indefinite" />
    </circle>
    <circle cx="120" cy="110" r="65" fill="none" stroke="{color2}" stroke-width="1" stroke-dasharray="2 10" opacity="0.2">
      <animateTransform attributeName="transform" type="rotate" values="360 120 110; 0 120 110" dur="15s" repeatCount="indefinite" />
    </circle>
    
    <!-- Logo with Neon Glow and Pulse -->
    <g transform="translate(80, 70) scale(3.3)" fill="#ffffff" filter="url(#neon_logo_{slug})">
      <animate attributeName="opacity" values="0.7; 1; 0.7" dur="2.5s" repeatCount="indefinite" />
      {paths}
    </g>
    
    <!-- Technology Name -->
    <text x="120" y="200" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="20" font-weight="700" fill="#ffffff" text-anchor="middle" filter="url(#neon_text_{slug})">{name}</text>
  </g>
</svg>"""
    return svg

print("Generating 15 animated SVGs...")
for slug, name, c1, c2 in icons:
    print(f"Generating {slug}...")
    content = generate_svg(slug, name, c1, c2)
    with open(f"/Users/yashwanth/Desktop/yashwanthR1207/assets/tech/{slug}.svg", "w") as f:
        f.write(content)
print("Done!")
