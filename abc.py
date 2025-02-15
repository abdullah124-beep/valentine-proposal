from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name="Areesha")

@app.route('/no')
def no_response():
    return render_template('no.html')

if __name__ == '__main__':
    app.run(debug=True)

# HTML files to create:
# templates/index.html
# templates/no.html
