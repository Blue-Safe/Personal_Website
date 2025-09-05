from flask import Flask, render_template

app = Flask(__name__)


posts = [
    {
      "slug": "mark I recap",
      "title": "CRUNCH Mark I -Recap", 
      "date": "2025-09-02",
      "highlight": True, 
      "summary":"...",
      "body": "<p>All right, after taking a break, I'm ready to comeback with full force. I have 2 and a half weeks before I go back to school. So, here are my thoughts on MK I.</p> <h3> What went well </h3> <li> 3D printed frame <p>-Was strong, solid, and straightforward to assemble.</p></li> <li>  On board electronics <p>-Everything was compatable & worked. PCA board was a great call. I succsesfully could program all the moving parts and have them work together.</p></li>",
      "imgs": [("images/MK1_coverON.jpg","Testing"),
               ("images/MK1_skelly.jpg","This is also a test")]
      },
      {
          "slug": "bluetooth gui",
          "title": "bluetooth gui",
          "date": "2025-08-02",
          "highlight": False,
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