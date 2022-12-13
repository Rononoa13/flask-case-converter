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

        # print(f"{find_char}")
        # print(f"{replace_text}")
        # print(f"{note}")

        x = note.replace(find_char, replace_text)
        # print(f'this is changed text -> {x}')
    return render_template('home.html', x=x)


if __name__== '__main__':
    app.run(debug=True)