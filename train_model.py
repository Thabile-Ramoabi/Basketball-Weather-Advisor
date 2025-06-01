import pandas as pd
import pickle
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

def train_model():
    try:
        # Load and prepare data
        df = pd.read_csv("temperature.csv")
        df.columns = df.columns.str.strip()
        
        X = df[['Outlook', 'Temp', 'Humidity', 'Windy']]
        y = df['Play Basketball']
        
        # Convert Windy to boolean
        X['Windy'] = X['Windy'].astype(bool)
        
        # Encode categorical features
        le_X = {col: LabelEncoder() for col in X.columns}
        for col in X.columns:
            X[col] = le_X[col].fit_transform(X[col])
        
        le_y = LabelEncoder()
        y = le_y.fit_transform(y)
        
        # Train and save model
        model = GaussianNB()
        model.fit(X, y)
        
        with open("model.pkl", "wb") as f:
            pickle.dump((model, le_X, le_y, X.columns.tolist()), f)
        
        print("Model trained successfully")
        return True
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    train_model()