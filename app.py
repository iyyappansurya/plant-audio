import requests
from flask import Flask,jsonify,request
import requests

API_URL = "https://api-inference.huggingface.co/models/codenamewei/speech-to-text"
headers = {"Authorization": "Bearer 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"}

app = Flask(_name_)
@app.route('/index',methods=['GET','POST'])
def index():
    return 'hello world'

def query(filename):
    with open(filename, "rb") as f:
       data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()
def tex(url,text):
  response = requests.post(url,headers=headers,data=text)
  return response.json()
@app.route('/result',methods=['GET','POST'])
def result():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        text = jsonify(query(filename))
        spech = 'https://agrithon.up.railway.app/text'
        pred = tex(spech,text)
        return pred
if _name_ == "_main_":
    app.run(debug=True)
