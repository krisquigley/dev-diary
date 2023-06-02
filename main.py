import sys
from flask import Flask, render_template, send_from_directory
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
from config.settings import *

def split_and_strip(value, separator=','):
    return [v.strip() for v in value.split(separator)]

app = Flask(__name__)
app.jinja_env.filters['split_and_strip'] = split_and_strip
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
    if content.meta["projects"]:
        post_projects = [
            p
            for p in flatpages
            if p.path.startswith(PROJECT_DIR)
            and p.meta["slug"] in content.meta["projects"]
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
    project_posts = [
        p
        for p in flatpages
        if p.path.startswith(POST_DIR) and p.meta["projects"] and slug in p.meta["projects"]
    ]
    project_posts.sort(key=lambda item: item["date"], reverse=True)

    path = f"{PROJECT_DIR}/{slug}"
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


@app.route("/_redirects")
def redirects():
    return send_from_directory("public", "_redirects")


@app.route("/robots.txt")
def robots():
    return send_from_directory("public", "robots.txt")


@app.route("/<path:filepath>")
def public(filepath):
    return send_from_directory("public", filepath)

@app.context_processor
def utility_functions():
    def print_in_console(message):
        print(f"{message}")

    return dict(mdebug=print_in_console)




if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host="0.0.0.0", debug=True, port="3000")
