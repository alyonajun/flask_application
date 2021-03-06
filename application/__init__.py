from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/table')
def table():
    """
Just a test enter
"""
    data_new = {"layout": "Some text",
            "title": "Super Test",
            "header": "HE-HE-HE-HE... Hello World!!",
            "lines": [
                {"title": "0", "columns": ["first_00", "first_01", "first_02", "first_03"]},
                {"title": "1", "columns": ["second_10", "second_11", "second_12", "second_13"]},
                {"title": "0", "columns": ["third_20", "third_21", "third_22", "third_23"]},
                {"title": "1", "columns": ["fourth_30", "fourth_31", "fourth_32", "fourth_33"]},
            ]
    }
    f = open("text.txt", "r")
    f.readline()
    for i in range(0, len(data_new["lines"]), 1):
        data_new["lines"][i]["columns"] = list(f.readline().split())
    return render_template('table.html', data_new = data_new)


def get_data():
    some_list = []
    for i in range(0, 4, 1):
        if request.method == 'POST':
            some_list.append(str(request.form['text'+str(i)]))
        else:
            some_list.append(str(request.args.get('text'+str(i))))
    return some_list

def func_1(some_list):
    with open('text.txt', 'a') as f:
        for item in some_list:
            f.write(item)
            f.write('\t')
        f.write('\n')
    f.close()

@app.route('/', methods = ['GET', 'POST'])
def index():
    some_list = get_data()
    func_1(some_list)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5000)

