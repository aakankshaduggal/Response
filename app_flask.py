from flask import Flask, request,json,jsonify
from lipi_edits import generatedRes
from flask_restful import reqparse, abort, Api, Resource


#sentiment_value
#persona

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

@app.route("/get_response",methods=['GET','POST'])
#class getresponse(Resource)
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


task={
      'name':"lipi"}

@app.route("/test",methods=['GET'])
def test():
    return jsonify(task)

#api.add_resource(getresponse, '/get_response')
#api.add_resource(Todo, '/todos/<todo_id>')

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=8080 )