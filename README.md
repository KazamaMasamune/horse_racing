# 🏇 Horse Racing - Horse Race Winner Prediction System

**Horse Racing** is a machine learning system that predicts whether a horse will win a race, developed as a computer science project. Using data from `race-result-horse.csv`, it trains a random forest model to analyze horse, jockey, and race features. A Flask backend delivers predictions, while a Next.js frontend provides an intuitive interface for inputting race data and viewing results. Ideal for racing fans and data scientists! 🌟

## 📋 Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features
- 🐎 **Winner Prediction**: Classifies horses as winners or non-winners based on race data.
- 📊 **Accurate Model**: Achieves ~80% accuracy (tune `backend/train_model.py` for better results).
- 🌐 **Web Interface**: Next.js frontend for inputting race features (e.g., horse speed, jockey experience).
- 📈 **Confidence Scores**: Displays prediction probabilities (e.g., “Winner: 85%”).
- 💾 **Model Persistence**: Saves trained model (`backend/horse_race_predictor_model.pkl`) for fast predictions.
- 🛠️ **Extensible**: Supports adding new features or models to enhance performance.

## 🛠️ Technologies
```yaml
Machine Learning:
  - Python: 3.12 🐍
  - scikit-learn: 1.0.2 🤖
  - pandas: 1.3.5 📊
  - numpy: 1.21.6 🔢
  - joblib: 1.1.0 💾
Backend:
  - Flask: 2.0.1 🌐
Frontend:
  - Next.js: 14.0.0 ⚛️
  - JavaScript: UI 🖼️
Tools:
  - Git: Version control 🔗
  - VS Code: IDE 💻
Environment:
  - pip: Python packages 📦
  - npm: Node.js packages 📦
Planned:
  - FastAPI: Faster backend 🚀
  - TensorFlow: Deep learning models 🧠
horse_racing/
├── backend/
│   ├── app.py                    # Flask app for predictions
│   ├── train_model.py            # Trains the ML model
│   ├── horse_race_predictor_model.pkl  # Saved model
│   ├── features.pkl              # Feature preprocessing data
│   ├── race-result-horse.csv     # Dataset
│   ├── jockey_win_rates.png      # Feature visualization
│   ├── inspect_data.py           # Data analysis script
│   └── print_features.py         # Feature inspection utility
├── horse-race-frontend/
│   ├── pages/
│   │   ├── index.js              # Main web UI
│   │   ├── _app.js               # Next.js app config
│   │   ├── _document.js          # Document setup
│   │   └── api/hello.js          # Sample API endpoint
│   ├── styles/globals.css        # Global styles
│   ├── public/*.svg              # Static assets (icons)
│   ├── package.json              # Node.js dependencies
│   └── next.config.mjs           # Next.js config
├── .gitignore                    # Ignores venv/, node_modules/
└── README.md                     # Project documentation
⚙️ Installation
Set up the system locally:

Clone the Repository:
bash

Copy
git clone https://github.com/KazamaMasamune/horse_racing.git
cd horse_racing
Backend Setup:
Create a Python virtual environment:
bash

Copy
cd backend
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install dependencies:
bash

Copy
pip install flask==2.0.1 scikit-learn==1.0.2 pandas==1.3.5 numpy==1.21.6 joblib==1.1.0
Frontend Setup:
Navigate to frontend:
bash

Copy
cd ../horse-race-frontend
Install Node.js dependencies:
bash

Copy
npm install
Verify Files:
Ensure backend/race-result-horse.csv, backend/horse_race_predictor_model.pkl, and backend/train_model.py are present.
Note: Requires Python 3.12+ (python3 --version) and Node.js 18+ (node --version).

🚀 Usage
Run and interact with the system:

Train the Model (if needed):
bash

Copy
cd backend
source .venv/bin/activate
python3 train_model.py
Generates horse_race_predictor_model.pkl and jockey_win_rates.png.
Start the Flask Backend:
bash

Copy
python3 app.py
Runs on http://localhost:5000.
Start the Next.js Frontend:
In a new terminal:
bash

Copy
cd horse-race-frontend
npm run dev
Visit http://localhost:3000 in your browser
