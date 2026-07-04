import urllib.request
import urllib.parse
import json
import re

USERNAME = "yashwanthR1207"
EXCLUDE_FORKS = True

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

def get_repos():
    url = f"https://api.github.com/users/{USERNAME}/repos?type=public&sort=updated&per_page=100"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github.v3+json")
    
    with urllib.request.urlopen(req) as response:
        repos = json.loads(response.read().decode())
        
    if EXCLUDE_FORKS:
        repos = [repo for repo in repos if not repo.get("fork")]
        
    return repos

def extract_stack_html(repo):
    icons = set()
    badges = []
    
    # 1. Check primary language
    lang = repo.get("language")
    if lang:
        lang_lower = lang.lower()
        if lang_lower in ICON_MAP:
            icons.add(ICON_MAP[lang_lower])
        elif lang_lower in ["html", "css", "java", "ruby", "rust", "go", "swift", "kotlin", "dart", "bash", "c", "cpp"]:
            icons.add(lang_lower)
        else:
            badges.append(lang)

    # 2. Check topics
    topics = repo.get("topics", [])
    for topic in topics:
        topic_lower = topic.lower()
        if topic_lower in ICON_MAP:
            icons.add(ICON_MAP[topic_lower])
        elif topic_lower in ["arduino", "raspberrypi", "linux", "docker", "ros", "react", "vue", "nodejs", "mongodb"]:
            icons.add(topic_lower)
        else:
            badges.append(topic)
            
    html_parts = []
    if icons:
        icon_str = ",".join(list(icons))
        html_parts.append(f'<img src="https://skillicons.dev/icons?i={icon_str}&theme=dark" height="30" valign="middle" />')
        
    for badge in badges[:3]: # limit to max 3 extra badges so it doesn't get too long
        badge_name = badge.replace("-", " ").upper()
        badge_url_name = urllib.parse.quote(badge_name)
        html_parts.append(f'<img src="https://img.shields.io/badge/{badge_url_name}-0D0D0D?style=flat-square&color=FF6600" height="28" valign="middle" />')
        
    if not html_parts:
        return "N/A"
        
    return "&nbsp;".join(html_parts)

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
        markdown += f'    <td align="center">{stack_html}</td>\n'
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
    # Exclude the profile repo itself
    repos = [repo for repo in repos if repo["name"].lower() != USERNAME.lower()]
    markdown = generate_markdown(repos)
    update_readme(markdown)
