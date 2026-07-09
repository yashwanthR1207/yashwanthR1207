import urllib.request
import urllib.parse
import json
import re
import os

USERNAME = "yashwanthR1207"
EXCLUDE_FORKS = True

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

ICON_MAP = {
    "c++": "cpp",
    "c": "c",
    "python": "python",
    "javascript": "js",
    "typescript": "ts",
    "html": "html",
    "css": "css",
    "arduino": "arduino",
    "matlab": "matlab",
    "jupyter notebook": "python",
    "java": "java",
    "c#": "cs",
    "php": "php",
    "shell": "bash",
    "vue": "vue",
    "react": "react",
    "nodejs": "nodejs",
    "docker": "docker",
    "linux": "linux",
    "ros": "ros"
}

def make_request(url):
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github.v3+json")
    if GITHUB_TOKEN:
        req.add_header("Authorization", f"token {GITHUB_TOKEN}")
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def get_repos():
    url = f"https://api.github.com/users/{USERNAME}/repos?type=public&sort=updated&per_page=100"
    repos = make_request(url)
    if not repos:
        return []
        
    if EXCLUDE_FORKS:
        repos = [repo for repo in repos if not repo.get("fork")]
        
    return repos

def get_languages(repo_name):
    url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/languages"
    return make_request(url) or {}

def extract_stack_html(repo):
    html_parts = []
    
    # 1. Get languages and calculate percentages
    langs = get_languages(repo["name"])
    total_bytes = sum(langs.values())
    
    # Process languages
    if total_bytes > 0:
        for lang, count in langs.items():
            lang_lower = lang.lower()
            icon = None
            if lang_lower in ICON_MAP:
                icon = ICON_MAP[lang_lower]
            elif lang_lower in ["html", "css", "java", "ruby", "rust", "go", "swift", "kotlin", "dart", "bash", "c", "cpp"]:
                icon = lang_lower
                
            percentage = (count / total_bytes) * 100
            # Only show languages > 1% to avoid clutter
            if percentage >= 1.0:
                pct_str = f"{percentage:.1f}%"
                
                if icon:
                    html_parts.append(f'<img src="https://skillicons.dev/icons?i={icon}&theme=dark" height="25" align="center" /> <sub>{pct_str}</sub>')
                else:
                    # Fallback text for language
                    html_parts.append(f'<b>{lang}:</b> <sub>{pct_str}</sub>')

    # 2. Check topics (no percentages for topics, just badges or icons)
    topics = repo.get("topics", [])
    topic_icons = set()
    topic_badges = []
    for topic in topics:
        topic_lower = topic.lower()
        if topic_lower in ICON_MAP:
            topic_icons.add(ICON_MAP[topic_lower])
        elif topic_lower in ["arduino", "raspberrypi", "linux", "docker", "ros", "react", "vue", "nodejs", "mongodb"]:
            topic_icons.add(topic_lower)
        else:
            topic_badges.append(topic)
            
    if topic_icons:
        icon_str = ",".join(list(topic_icons))
        html_parts.append(f'<img src="https://skillicons.dev/icons?i={icon_str}&theme=dark" height="25" align="center" />')
        
    for badge in topic_badges[:3]:
        badge_name = badge.replace("-", " ").upper()
        badge_url_name = urllib.parse.quote(badge_name)
        html_parts.append(f'<img src="https://img.shields.io/badge/{badge_url_name}-0D0D0D?style=flat-square&color=FF6600" height="23" align="center" />')
        
    if not html_parts:
        return "N/A"
        
    return "&nbsp;&nbsp;".join(html_parts)

def generate_markdown(repos):
    markdown = "<table>\n"
    markdown += "  <tr>\n"
    markdown += "    <th>Project</th>\n"
    markdown += "    <th>Tech Stack</th>\n"
    markdown += "  </tr>\n"
    
    for repo in repos:
        name = repo["name"].replace("-", " ").title()
        url = repo["html_url"]
        
        stack_html = extract_stack_html(repo)
        
        markdown += "  <tr>\n"
        markdown += f'    <td><b><a href="{url}">{name}</a></b></td>\n'
        markdown += f'    <td>{stack_html}</td>\n'
        markdown += "  </tr>\n"
        
    markdown += "</table>\n"
    return markdown

def update_readme(markdown):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
        
    start_marker = "<!-- PROJECTS:START -->"
    end_marker = "<!-- PROJECTS:END -->"
    
    pattern = f"{start_marker}.*?{end_marker}"
    replacement = f"{start_marker}\n{markdown}\n{end_marker}"
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    repos = get_repos()
    repos = [repo for repo in repos if repo["name"].lower() != USERNAME.lower()]
    markdown = generate_markdown(repos)
    update_readme(markdown)
