from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/", methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        find_char = request.form.get('find-char')
        replace_text = request.form.get('replace-text')
        note = request.form.get('user-note')

        user_text = note.replace(find_char, replace_text)

    return render_template('home.html', user_text=user_text)

@app.route("/json_converter", methods=['GET', 'POST'])
def get_pretty_json():

    if request.method == 'POST':

        get_user_json = request.form.get('json-input')
        if "'" in get_user_json:
            get_user_json = get_user_json.replace("'", "\"")
        json_data = json.loads(get_user_json)
        print_json = json.dumps(json_data, indent=4)

        # json_strings = get_user_json.split('}, {')

        # if len(json_strings) < 1:
        #     json_strings[0] = json_strings[0] + '}'
        #     json_strings[-1] = '{' + json_strings[-1]

        # formatted_objects = []
        # for json_data in json_strings:
        #     formatted_objects.append(json.dumps(json.loads(json_data), indent=4))
        # print_json = formatted_objects

        return render_template('json_formatter.html', pretty_json=print_json)

    return render_template('json_formatter.html')

if __name__== '__main__':
    app.run(debug=True)