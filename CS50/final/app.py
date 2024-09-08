from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test", methods=["GET", "POST"])
def test():

    if request.method == "POST":

        # get user input
        weight = int(request.form.get("weight"))
        pull = int(request.form.get("pull"))
        crimp = int(request.form.get("crimp"))
        hang = int(request.form.get("hang"))
        core = request.form.get("excersize").lower()
        core_time = int(request.form.get("core_time"))

        # list indexes are the points (output) while values are the times/weight ratios (input)
        pull_list = [-1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1, 1.2]
        crimp_list = [-1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1, 1.2]
        hang_list = [-1, 30, 60, 90, 120, 150, 180, 210, 270, 300, 330]
        knee_list = [-1, 10, 20, 30]
        lsit_list = [-1, -1, -1, -1, 10, 15, 20]
        lever_list = [-1, -1, -1, -1, -1, -1, -1, 5, 10, 20, 30]

        pull_ratio = pull / weight
        crimp_ratio = crimp / weight

        # calculate points based of index in respective list
        pull_points = pull_calc(pull_ratio, pull_list)
        crimp_points = crimp_calc(crimp_ratio, crimp_list)
        hang_points = hang_calc(hang, hang_list)
        core_points = core_calc(core, core_time, knee_list, lsit_list, lever_list)

        total = pull_points + crimp_points + hang_points + core_points

        # list index correspomds to points (input) while values are the grades(output)
        grade_list = ['error: you stink', '6a', '6a', '6b', '6b', '6c', '6c', '6c+', '6c+', '7a', '7a', '7a+', '7a+', '7b', '7b', '7b+', '7b+', '7c', '7c+', '7c+', '8a',
             '8a', '8a+', '8a+', '8b', '8b', '8b+', '8b+', '8c', '8c', '8c+', '8c+', '9a', '9a', '9a+', '9a+', '9b', '9b', '9b+', '9c']

        grade = grade_list[total]


        # if they score above a 40 they gotta be adam ondra right?
        if total >= 40:
            ao = "You're Adam Ondra!"
        else:
            ao = ""

        return render_template("results.html", pull_points=pull_points, crimp_points=crimp_points, hang_points=hang_points, core_points=core_points,
                               total=total, grade=grade, ao=ao)



    else:
        return render_template("test.html")


@app.route("/results")
def results():
    return render_template("results.html")



@app.route("/review")
def review():
    return render_template("review.html")









def pull_calc(ratio, list):
    for x in list:
        if x <= ratio:
            point = list.index(x)
    return point


def crimp_calc(ratio, list):
    for x in list:
        if x <= ratio:
            point = list.index(x)
    return point


def hang_calc(time, list):
    for x in list:
        if x <= time:
            point = list.index(x)
    return point


def core_calc(type, time, list1, list2, list3):
    if type == "knee":
        for x in list1:
            if x <= time:
                point = list1.index(x)
        return point

    elif type == "sit":
        for x in list2:
            if x <= time:
                point = list2.index(x)
        return point

    elif type == "lever":
        for x in list3:
            if x <= time:
                point = list3.index(x)
        return point


def find_weakness(list):
    min = list[0]
    for x in range(len(list)):
        if list[x] <= list[0]:
            min = list[x]
    return min