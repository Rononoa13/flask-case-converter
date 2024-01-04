from flask import Flask, render_template, request

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


@app.route("/csv_json_converter", methods=['GET', 'POST'])
def convert_csv_to_json():
    return render_template('csv_to_json.html')

if __name__== '__main__':
    app.run(debug=True)