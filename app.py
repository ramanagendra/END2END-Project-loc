
from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData,PredictPipeline

from flask import Flask,request,render_template, jsonify

app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/predict", methods=["GET","POST"])
def predict_datapoints():
    if request.method == "GET":
        return render_template("form.html")
    
    else:
        CustomData(

            carat=float(request.form.get('carat')),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table'))
            x=float(request.form.get('x')),
            y=float(request.form.get('y')),
            z=float(request.form.get('z')),
            cut=request.from.get('cut'),
            color=request.form.get('color'),
            clarity=request.form.get('clarity')
        )


        




app.run()