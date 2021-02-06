from flask import Flask,render_template,request,session,url_for
import  pickle as pkl
import numpy as np

app = Flask(__name__)
model = pkl.load(open("model.pkl","rb"))
@app.route("/")
def home():
    return render_template("welcome.html")
@app.route("/predict",methods=["POST","GET"])
def predict():
    if request.method=="POST":
        sl = int(request.form["a"])
        sw = int(request.form["b"])
        pl = int(request.form["c"])
        pw = int(request.form["d"])
        prediction = model.predict(np.array([[sl,sw,pl,pw]]))
        ans=list(prediction)
        return render_template("display.html",arr=str(ans[0]))
    else:
        return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)