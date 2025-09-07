from flask import Flask, render_template
import os, yaml, markdown
from datetime import datetime

app = Flask(__name__)


POSTS_DIR = os.path.join(app.root_path, "content", "posts")

def loadPosts():
    posts=[]
    for file in os.listdir(POSTS_DIR):
        if file.endswith(".md"):
            with open(os.path.join(POSTS_DIR, file), "r", encoding="utf-8") as f:
                raw = f.read()
            if raw.startswith("---"):
                _, fm_text,md_text = raw.split("---",2)
                meta =yaml.safe_load(fm_text)
                html_body = markdown.markdown(md_text, extensions=["fenced_code","tables"])
                meta["body_html"]=html_body
                meta["date_obj"] = datetime.fromisoformat(meta["date"])
                posts.append(meta)
    return sorted(posts,key=lambda p: p["date_obj"], reverse=True)



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/blog")
def blog():   
    return render_template("blog.html",posts=loadPosts())
@app.route("/blog/<slug>")
def blog_post(slug):
    posts = loadPosts()
    post = next((p for p in posts if p["slug"] == slug), None)
    if not post:
        return "Post not found", 404
    return render_template("post.html", post=post)



if __name__ == "__main__":
    app.run(debug=True)