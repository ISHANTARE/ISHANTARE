import urllib.request
import json
import re

def update_readme():
    try:
        # Fetch data from NASA APOD API
        api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
        req = urllib.request.Request(api_url)
        
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            
        image_url = data.get("url", "")
        title = data.get("title", "NASA Astronomy Picture of the Day")
        date_str = data.get("date", "")
        
        if not image_url:
            print("Failed to get APOD image URL.")
            return
            
        # Format markdown based on media type
        if "youtube.com" in image_url or "vimeo.com" in image_url:
            # For videos, try to extract a thumbnail or just link to it
            video_id = image_url.split("/")[-1].split("?")[0]
            thumbnail = f"https://img.youtube.com/vi/{video_id}/0.jpg" if "youtube.com" in image_url else "https://via.placeholder.com/800x450.png?text=Video+Transmission"
            markdown_content = f'[![{title}]({thumbnail})]({image_url})\\n<br/><i><b>{title}</b> ({date_str})</i>'
        else:
            # For regular images
            markdown_content = f'<a href="{image_url}"><img src="{image_url}" width="100%" style="border-radius: 10px;" alt="{title}"/></a>\\n<br/><i><b>{title}</b> ({date_str})</i>'
            
        readme_path = "README.md"
        with open(readme_path, "r", encoding="utf-8") as file:
            readme = file.read()
            
        # Create pattern to find the exact replacement block
        pattern = r"(<!-- START_SECTION:apod -->\\n)(.*?\\n)*(.*<!-- END_SECTION:apod -->)"
        
        # Replacement pattern
        replacement = f"\\g<1>{markdown_content}\\n\\g<3>"
        
        new_readme = re.sub(pattern, replacement, readme, flags=re.MULTILINE)
        
        with open(readme_path, "w", encoding="utf-8") as file:
            file.write(new_readme)
            
        print("Successfully updated README with NASA APOD")
    except Exception as e:
        print(f"Error updating APOD: {e}")

if __name__ == "__main__":
    update_readme()
