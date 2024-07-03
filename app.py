from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config["SECRET_KEY"] = "abcdef"

debug = DebugToolbarExtension(app)

@app.route("/")
def select_fav_story():
    """Show list of stories to select."""

    return render_template("select_story.html", stories=stories.values())


@app.route("/home")
def question_form():
    """Generate form prompting for all the words in the story"""

    story_id = request.args["story_id"]
    story = stories[story_id]
    
    prompts = story.prompts
    return render_template("home.html" ,story_id=story_id, title=story.title, prompts=prompts)


@app.route("/story")
def my_story():
    """Resulting Madlib story"""

    story_id = request.args["story_id"]
    story = stories[story_id]

    answers = request.args
    text = story.generate(answers)
    return render_template("story.html" , title=story.title, text=text)