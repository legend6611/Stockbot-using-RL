📈 Stock Trading Reinforcement Learning Bot

A reinforcement-learning–based stock trading bot that learns trading strategies (Buy/Sell/Hold) using real market data.
The project includes:

RL algorithms: DQN, PPO, TRPO

Training environment built using OpenAI Gym

Flask API to load models and serve predictions

Frontend (HTML/CSS/JS or React) to visualize real-time charts and model outputs

Model-selection dropdown (choose DQN/PPO/TRPO and view results)

🚀 Features
✅ Reinforcement Learning

Custom Gym environment for stock trading

Support for DQN, PPO, TRPO

Reward shaping based on portfolio returns

Model saving & loading

✅ Backend (Flask)

API to select model (DQN/PPO/TRPO)

API to run inference and return predictions

Routes for real-time chart data

Lightweight, fast deployment

✅ Frontend

Real-time stock visualizations

Dropdown to choose the RL model

Profit & loss metrics

Graphs rendered using Chart.js 

📂 Project Structure
stock-bot/
│
├── backend/
│   ├── app.py                # Flask server
│   ├── models/               # Saved RL models (DQN/PPO/TRPO)
│   ├── training/             # RL training scripts
│   ├── environment/          # Gym environment
│   └── utils/                # Helper scripts
│
├── frontend/
│   ├── index.html / React app
│   ├── chart.js
│   └── scripts.js
│
├── data/
│   └── stock_data.csv        # Market dataset used for training/testing
│
└── README.md

🧠 RL Algorithms Used
1. DQN (Deep Q-Network)

Learns Q-values for Buy/Sell/Hold

Good for discrete-action trading

2. PPO (Proximal Policy Optimization)

Stable, continuous improvement

Works well with noisy financial signals

3. TRPO (Trust Region Policy Optimization)

Focuses on stable policy updates

Useful when training is unstable


▶️ Training the Models

To train DQN:

python training/train_dqn.py


To train PPO:

python training/train_ppo.py


To train TRPO:

python training/train_trpo.py


Models will be saved automatically in:

backend/models/

▶️ Running Predictions

Send a request to Flask:

GET /predict?model=dqn


Or choose the model from the frontend dropdown.

📊 Frontend Visualizations

The frontend displays:

Live candlestick charts

Buy/Sell signals predicted by the RL model

Portfolio curve

Cumulative returns

Comparison of DQN vs PPO vs TRPO performance

📈 Example Results

Profit

Number of Trades

Profit Multiplier

💡 Future Enhancements

Add LSTM-based policy networks

Portfolio optimization with multiple stocks

Backtesting on large datasets

Deploy on AWS/GCP with Docker

Add WebSockets for real-time data streaming

🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open a PR or issue.
