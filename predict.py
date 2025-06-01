import pickle
import sys
import pandas as pd

def predict(features):
    try:
        with open("model.pkl", "rb") as f:
            model, le_X, le_y, columns = pickle.load(f)
        
        # Prepare input (now handles both web and CLI)
        features = {
            'Outlook': sys.argv[1] if len(sys.argv) > 1 else features['Outlook'],
            'Temp': sys.argv[2] if len(sys.argv) > 2 else features['Temp'],
            'Humidity': sys.argv[3] if len(sys.argv) > 3 else features['Humidity'],
            'Windy': sys.argv[4] if len(sys.argv) > 4 else features['Windy']
        }
        features['Windy'] = str(features['Windy']).upper() == 'TRUE'
        
        input_data = pd.DataFrame([features], columns=columns)
        for col in columns:
            input_data[col] = le_X[col].transform([input_data[col][0]])[0]
        
        prediction = model.predict(input_data)
        return le_y.inverse_transform(prediction)[0]
        
    except Exception as e:
        return f"Prediction Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) == 5:
        print(predict({}))  # Empty dict since we're using sys.argv