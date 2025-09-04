from flask import Flask, render_template

app = Flask(__name__)


posts = [
    {
      "slug": "mark I recap",
      "title": "CRUNCH Mark I -Recap", 
      "date": "2025-09-02", 
      "summary":"...",
      "body": "<p>...</p>"
      },
      {
          "slug": "bluetooth gui",
          "title": "bluetooth gui",
          "date": "2025-08-02",
          "summary": "Made a GUI in python that communicated with the terminal to send signals over bluetooth",
          "body": "<p>Details...</p>"
      }
      ]


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
    ordered = sorted(posts, key=lambda p: p["date"], reverse=True)    
    return render_template("blog.html",posts=ordered)
@app.route("/blog/<slug>")
def blog_post(slug):
    post = next((p for p in posts if p["slug"] == slug), None)
    if post is None:
        return "Post not found", 404
    return render_template("post.html",post=post)



if __name__ == "__main__":
    app.run(debug=True)