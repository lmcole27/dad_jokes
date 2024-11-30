from flask import Flask, render_template

#CREATE WEBAPP
app = Flask(__name__)

#WEB HOME PAGE
@app.route('/', methods=['GET', 'POST'])
def welcome():
    return render_template("index.html")

#RUN THE WEBAPP
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)