import pickle as pkl
import numpy as np
from flask import Flask,render_template,request


model=pkl.load(open('lspipe.pkl','rb'))
app = Flask(__name__, template_folder='templates')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    url = request.form.get('URL')
    X_predict = []
    X_predict.append(str(url))
    y_Predict = model.predict(X_predict)
    if y_Predict == 'bad':
        result = "This is a Phishing Site"
    else:
        result = "This is not a Phishing Site"
    
    return result

if __name__== '__main__':
    app.run(debug=True ,port=8001)


