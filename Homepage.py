from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def student():
    return render_template("divya.html")
    #return render_template('student.html')
if __name__=="__main__":
    app.run()
