from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('gw_welcome_page.html')

if __name__ == "__main__":
    app.run() 
