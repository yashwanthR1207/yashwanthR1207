import urllib.request
import json
import re

USERNAME = "yashwanthR1207"
EXCLUDE_FORKS = True

def get_repos():
    url = f"https://api.github.com/users/{USERNAME}/repos?type=public&sort=updated&per_page=100"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github.v3+json")
    
    with urllib.request.urlopen(req) as response:
        repos = json.loads(response.read().decode())
        
    if EXCLUDE_FORKS:
        repos = [repo for repo in repos if not repo.get("fork")]
        
    return repos

def generate_markdown(repos):
    markdown = "<table width=\"100%\">\n"
    for i in range(0, len(repos), 2):
        markdown += "  <tr>\n"
        
        # First column
        repo1 = repos[i]
        markdown += f'    <td width="50%">\n'
        markdown += f'      <a href="{repo1["html_url"]}">\n'
        markdown += f'        <img src="https://github-readme-stats.vercel.app/api/pin/?username={USERNAME}&repo={repo1["name"]}&theme=dark&bg_color=0D0D0D&border_color=00FFFF&title_color=FF6600&text_color=FFFFFF&icon_color=FF6600" width="100%" />\n'
        markdown += f'      </a>\n'
        markdown += f'    </td>\n'
        
        # Second column
        if i + 1 < len(repos):
            repo2 = repos[i + 1]
            markdown += f'    <td width="50%">\n'
            markdown += f'      <a href="{repo2["html_url"]}">\n'
            markdown += f'        <img src="https://github-readme-stats.vercel.app/api/pin/?username={USERNAME}&repo={repo2["name"]}&theme=dark&bg_color=0D0D0D&border_color=00FFFF&title_color=FF6600&text_color=FFFFFF&icon_color=FF6600" width="100%" />\n'
            markdown += f'      </a>\n'
            markdown += f'    </td>\n'
        else:
            markdown += f'    <td width="50%"></td>\n'
            
        markdown += "  </tr>\n"
        
    markdown += "</table>\n"
    return markdown

def update_readme(markdown):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
        
    start_marker = "<!-- PROJECTS:START -->"
    end_marker = "<!-- PROJECTS:END -->"
    
    pattern = f"{start_marker}.*?{end_marker}"
    replacement = f"{start_marker}\n{markdown}{end_marker}"
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    repos = get_repos()
    # Exclude the profile repo itself
    repos = [repo for repo in repos if repo["name"].lower() != USERNAME.lower()]
    markdown = generate_markdown(repos)
    update_readme(markdown)
