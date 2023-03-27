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


if __name__== '__main__':
    app.run(debug=True)