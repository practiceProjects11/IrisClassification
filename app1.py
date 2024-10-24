import pickle
from flask import Flask,render_template,redirect,request,url_for

with open("iris.pkl","rb") as file:
  model=pickle.load(file)
  
app1=Flask(__name__)
@app1.route("/")
def home():
  return render_template("classification.html")
@app1.route("/classification" ,methods=["POST","GET"])
def classification():
    if request.method=="POST":
        sepal_length=request.form["s-length"]
        sepal_width=request.form["s-width"]
        petal_length=request.form["p-length"]
        petal_width=request.form["p-width"]
        input1=[float(sepal_length),float(sepal_width),float(petal_length),float(petal_width)]
        prediction=model.predict([input1])
        if prediction[0]==0:
            return redirect(url_for("iris_setosa"))
        elif prediction[0]==1:
            return redirect(url_for("iris_versicolor"))
        elif prediction[0]==2:
            return redirect(url_for("iris_verginica"))




    return render_template("classification.html")
@app1.route("/iris_setosa",methods=["POST","GET"])
def iris_setosa():
    return render_template("iris_setosa.html")
@app1.route("/iris_verginica",methods=["POST","GET"])
def iris_verginica():
    return render_template("iris_verginica.html")
@app1.route("/iris_versicolor",methods=["POST","GET"])
def iris_versicolor():
    return render_template("iris_versicolor.html")
if __name__=="__main__":
    app1.run(debug=True)
