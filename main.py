import sys
from flask import Flask, render_template, send_from_directory
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
from config.settings import *

app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)


@app.route("/")
def posts():
    pages = [p for p in flatpages if p.path.startswith(POST_DIR)]
    project_pages = [p for p in flatpages if p.path.startswith(PROJECT_DIR)]
    pages.sort(key=lambda item: item["date"], reverse=True)
    return render_template("posts/index.html", posts=pages, projects=project_pages)


@app.route("/<year>/<month>/<day>/<name>.html")
def post(year, month, day, name):
    path = f"{POST_DIR}/{year}-{month}-{day}-{name}"
    content = flatpages.get_or_404(path)
    post_projects = []
    if content.meta["project"]:
        post_projects = [
            p
            for p in flatpages
            if p.path.startswith(PROJECT_DIR)
            and p.meta["slug"] in content.meta["project"]
        ]
        post_projects.sort(key=lambda item: item["date"], reverse=True)
    return render_template(
        "posts/show.html", post=content, name=name, projects=post_projects
    )


@app.route("/projects/index.html")
def projects():
    pages = [p for p in flatpages if p.path.startswith(PROJECT_DIR)]
    pages.sort(key=lambda item: item["name"], reverse=True)
    return render_template("projects/index.html", projects=pages)


@app.route("/projects/<slug>.html")
def project(slug):
    path = f"{PROJECT_DIR}/{slug}"
    project_posts = [
        p
        for p in flatpages
        if p.path.startswith(POST_DIR) and p.meta["project"] == slug
    ]
    project_posts.sort(key=lambda item: item["date"], reverse=True)
    content = flatpages.get_or_404(path)
    return render_template(
        "projects/show.html", project=content, project_posts=project_posts, name=slug
    )


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/node_modules/<path:filepath>")
def node_modules(filepath):
    return send_from_directory("node_modules", filepath)


@app.route("/pygments.css")
def pygments_css():
    return pygments_style_defs("github-dark"), 200, {"Content-Type": "text/css"}


@app.route("/robots.txt")
def robots():
    return send_from_directory("static", "robots.txt")


@app.route("/_redirects")
def redirects():
    return send_from_directory("static", "_redirects")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host="0.0.0.0", debug=True, port="3000")
