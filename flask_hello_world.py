from flask import Flask, request
app = Flask(__name__) 

@app.route('/model', methods=['POST'])

def hello_word():
    request_data = request.get_json(force=True)
    model_name = request_data['model']
    return "You are requesting for a {0} model".format(model_name)


if __name__ == "__main__":
    app.run(port=8000, debug=True)

# run on cmd : python flask_hello_world.py 
# then run on vs code terminal: python rest_client.py
# you will get: You should get requesting for a knn model