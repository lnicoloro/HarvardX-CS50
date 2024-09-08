from flask import Flask, render_template, request

app = Flask(__name__)       ## says to turn this current file into a flask application __name__ refers to the file it is in

# @app.route("/")             ## says here is code i want executed when the root (aka default aka index) of the webpage (/) is visited
# def index():
#     # if "name" in request.args:          ## request.args is a dictionary from flask that stores all the key value pairs fromthe url
#     #     name = request.args("name")       ## found at end of url www.url.com/?name=louis only works for GET
#     # else:
#     #     name = "world"

#     name = request.args.get("name", "world")     ### does what the four lines above did ( if no value for name then world will be used)

#     return render_template("index.html", placeholder=name)      ##need to specify the what needs to be replced with what
#     # return Hello World             ## can just return text or can use line above to run the html from the specified file


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        return render_template("greet.html", name=request.form.get("name", "world")) ## request.form used for POST


