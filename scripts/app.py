from flask import Flask, request, jsonify
import pickle
import pandas as pd

with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)  
    df = pd.DataFrame([data])  
    
    
    prediction = model.predict(df)  
    return jsonify({'prediction': prediction.tolist()})  

if __name__ == '__main__':
    app.run(port=5000, debug=True)  
