from flask import Flask, render_template, request, flash, redirect
import json
from pathlib import Path

ROOT_FOLDER = Path(__file__).resolve().parent
UPLOAD_FOLDER = f"{ROOT_FOLDER}/uploads"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

import csv

def make_JSON(csv_file, json_file):
    json_array = []
    # Read uploaded csv file.
    with open(csv_file, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        # header = csv_reader.fieldnames
        for row in csv_reader:
            json_array.append(row)
    
    # Write to JSON 
    with open(json_file, 'w') as jsonfile:
        json.dump(json_array, jsonfile, indent=4)
        # jsonfile.write(json_string)
            
    # print(csv_reader)
    return json_array

@app.route("/csv_json_converter", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No files')
            return redirect(request.url)
        file = request.files['file']
        # If user sends empty 
        if file.filename == '':
            flash('No file selected.')
            return redirect(request.url)
        
        if file:
            file_name = file.filename
            file.save(Path(app.config['UPLOAD_FOLDER']) / file_name)

            """
                Do something with the uploaded file, 
                here change it into JSON.
            """
            make_JSON(Path(app.config['UPLOAD_FOLDER']) / file_name, f"converted_json/{file_name}.json")
            return redirect('/csv_json_converter')
        

    return render_template('csv_to_json.html')

if __name__== '__main__':
    app.run(debug=True)