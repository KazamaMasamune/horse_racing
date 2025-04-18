import joblib

try:
    features = joblib.load('features.pkl')
    print("Features:", features)
except FileNotFoundError:
    print("Error: 'features.pkl' not found. Please run train_model.py first to generate the features file.")
except Exception as e:
    print(f"Error: An unexpected error occurred: {e}")
