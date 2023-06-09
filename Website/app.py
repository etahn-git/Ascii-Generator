from flask import Flask, render_template, request
from pyfiglet import Figlet

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/ascii')
def ascii():
    return render_template('./ascii.html')

@app.route('/acsii')
def acsii():
    return redirect("http://tools.etahn.dev/ascii", code=301)

@app.route('/generate_ascii', methods=['POST'])
def generate_ascii():
    text = request.json['text']
    figlet = Figlet(font='standard')
    ascii_art = figlet.renderText(text)
    return ascii_art

if __name__ == '__main__':
    app.run()

