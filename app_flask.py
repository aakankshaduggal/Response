from flask import Flask,render_template, request,json,url_for,flash,redirect,jsonify
from lipi_edits import generatedRes

#sentiment_value
#persona

app = Flask(__name__)
app.secret_key = 'random string'


@app.route("/get_response",methods=['GET','POST'])
def getResponse():
    print("oolala")
    print(request.get_json())
    persona = str(request.get_json()['persona'])

    sentiment_value = str(request.get_json()['sentiment_value'])
    print("printing input_statement")
    print(persona)
    print("END INPUT_STATEMENT")
	#print("printing input_statement")
    #print(sentiment_value)
    #print("END INPUT_STATEMENT")
    
    res=generatedRes(persona,sentiment_value)
    return res

if __name__=='__main__':
    app.run(debug=True)