import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
data = pd.read_csv('race-result-horse.csv')
print("Using horse-level features from race-result-horse.csv.")
print("Initial number of rows:", len(data))
print("Unique finishing_position values (before conversion):", data['finishing_position'].unique())

# Convert finishing_position to integer
data['finishing_position'] = pd.to_numeric(data['finishing_position'], errors='coerce')
print("Unique finishing_position values (after conversion):", data['finishing_position'].unique())
print("Initial number of winners (finishing_position == 1):", (data['finishing_position'] == 1).sum())

# Create target variable: 1 if winner (finishing_position = 1), 0 otherwise
data['winner'] = (data['finishing_position'] == 1).astype(int)
print("Number of winners after creating target:", data['winner'].sum())

# Check for missing values in required columns
required_columns = ['actual_weight', 'declared_horse_weight', 'draw', 'win_odds', 'jockey', 'finishing_position']
print("\nMissing values in required columns before dropna:")
print(data[required_columns].isna().sum())

# Drop rows with missing values in required columns
data = data.dropna(subset=required_columns)
print("\nNumber of rows after dropna:", len(data))
print("Number of winners after dropna:", data['winner'].sum())

# Filter rows with actual_weight > 0
data = data[data['actual_weight'] > 0]
print("Number of rows after actual_weight > 0:", len(data))
print("Number of winners after actual_weight > 0:", data['winner'].sum())

# Filter rows with win_odds > 0
data = data[data['win_odds'] > 0]
print("Number of rows after win_odds > 0:", len(data))
print("Number of winners after win_odds > 0:", data['winner'].sum())

# Check if we have at least two classes
print("Unique winner values after cleaning:", data['winner'].unique())
if len(data['winner'].unique()) < 2:
    raise ValueError("After cleaning, the dataset contains only one class for 'winner'. Cannot proceed with training.")

# Feature Engineering
# Limit to top 10 jockeys to reduce dimensionality
top_jockeys = data['jockey'].value_counts().head(10).index
data['jockey'] = data['jockey'].apply(lambda x: x if x in top_jockeys else 'Other')
jockey_dummies = pd.get_dummies(data['jockey'], prefix='jockey')

# Select features
features = ['actual_weight', 'declared_horse_weight', 'draw', 'win_odds'] + list(jockey_dummies.columns)
data = data.join(jockey_dummies)
X = data[features]
y = data['winner']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define models
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'SVM': SVC(probability=True),
    'Naive Bayes': GaussianNB(),
    'KNN': KNeighborsClassifier()
}

# Train and evaluate models
best_model = None
best_accuracy = 0
for name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=5)
    print(f"{name} Cross-Validation Accuracy: {scores.mean():.4f} (+/- {scores.std():.4f})")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred)
    print(f"{name} Test Accuracy: {test_accuracy:.4f}\n")
    if test_accuracy > best_accuracy:
        best_accuracy = test_accuracy
        best_model = model

# Save the best model and features
joblib.dump(best_model, 'horse_race_predictor_model.pkl')
joblib.dump(features, 'features.pkl')
print(f"Best model saved: {best_model.__class__.__name__} with Test Accuracy: {best_accuracy:.4f}")

# EDA Visualizations
plt.figure(figsize=(10, 6))
jockey_wins = data.groupby('jockey')['winner'].mean().sort_values(ascending=False)
sns.barplot(x='winner', y=jockey_wins.index, data=jockey_wins.reset_index())
plt.title('Win Rate by Jockey')
plt.xlabel('Win Rate')
plt.ylabel('Jockey')
plt.savefig('jockey_win_rates.png')
