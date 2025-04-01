from flask_cors import CORS
from flask import Flask, jsonify, request, render_template
import numpy as np
import os
from stable_baselines3 import PPO, DQN
from sb3_contrib import TRPO

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

# Initialize models to None
models = {
    'ppo': None,
    'trpo': None,
    'dqn': None
}

# Add profit tracking for each model
model_profits = {
    'ppo': 0,
    'trpo': 0,
    'dqn': 0
}

# Check if model files exist and load them
model_paths = {
    'ppo': "rl_stock_model.zip",
    'trpo': "trpo.zip",
    'dqn': "dqn.zip"
}

# Try to load each model
try:
    if os.path.exists(model_paths['ppo']):
        models['ppo'] = PPO.load(model_paths['ppo'])
        print("PPO model loaded successfully")
    else:
        print(f"Warning: PPO model file not found at {model_paths['ppo']}")

    if os.path.exists(model_paths['trpo']):
        models['trpo'] = TRPO.load(model_paths['trpo'])
        print("TRPO model loaded successfully")
    else:
        print(f"Warning: TRPO model file not found at {model_paths['trpo']}")

    if os.path.exists(model_paths['dqn']):
        models['dqn'] = DQN.load(model_paths['dqn'])
        print("DQN model loaded successfully")
    else:
        print(f"Warning: DQN model file not found at {model_paths['dqn']}")
        
except Exception as e:
    print(f"Error loading models: {str(e)}")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        
        # Validate request data
        if "state" not in data:
            return jsonify({"error": "Missing 'state' parameter"}), 400
            
        if "model" not in data:
            model_type = 'ppo'  # Default to PPO if not specified
        else:
            model_type = data["model"].lower()
            
        # Check if the requested model exists
        if model_type not in models or models[model_type] is None:
            return jsonify({
                "error": f"Model '{model_type}' not available. Please check model file: {model_paths[model_type]}"
            }), 500

        # Get the model
        model = models[model_type]
        
        # Process the observation data
        obs = np.array(data["state"])
        
        # Print the shape to verify
        print(f"Observation shape: {obs.shape}")
        
        # Make sure it's (10, 2) as expected by the model
        if obs.shape != (10, 2):
            return jsonify({"error": f"Invalid shape: {obs.shape}. Expected (10, 2)"}), 400
            
        # Reshape for model prediction (add batch dimension)
        obs = np.expand_dims(obs, axis=0)  # Reshape to (1, 10, 2)
        print(f"Reshaped observation for {model_type}: {obs.shape}")
        
        # Predict action
        action, _states = model.predict(obs)
        
        # Update profit if provided
        if "profit" in data:
            profit_change = float(data["profit"])
            model_profits[model_type] += profit_change
            
        # Use totalProfit from request if available for backward compatibility
        elif "totalProfit" in data:
            # Only update if the value is different (to avoid duplicating)
            new_profit = float(data["totalProfit"])
            if abs(model_profits[model_type] - new_profit) > 0.001:  # Small threshold to account for floating point
                model_profits[model_type] = new_profit
        
        # Return the prediction result with all model profits
        return jsonify({
            "action": int(action[0]),
            "model": model_type,
            "profit": model_profits[model_type],
            "all_profits": model_profits
        })
        
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/profits", methods=["GET"])
def get_profits():
    return jsonify(model_profits)

@app.route("/reset_profits", methods=["POST"])
def reset_profits():
    model_type = request.json.get("model", "all")
    
    if model_type == "all":
        for key in model_profits:
            model_profits[key] = 0
        return jsonify({"message": "All profits reset to 0"})
    elif model_type in model_profits:
        model_profits[model_type] = 0
        return jsonify({"message": f"{model_type.upper()} profit reset to 0"})
    else:
        return jsonify({"error": f"Invalid model type: {model_type}"}), 400

# Run the application
if __name__ == "__main__":
    app.run(debug=True)