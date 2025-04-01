document.addEventListener('DOMContentLoaded', function() {
    // Model performance data (from your images)
    const modelStats = {
        'dqn': { totalReward: 296.760010, totalProfit: 1.085815 },
        'trpo': { totalReward: 509.070007, totalProfit: 1.567007 },
        'ppo': { totalReward: 368.949890, totalProfit: 1.384247 } // Default from original code
    };

    // Initial state data
    const initialState = [
        [0, 450], [5, 400], [15, 500], [20, 550], 
        [30, 650], [50, 650], [60, 750], [75, 850], 
        [90, 975], [100, 975]
    ];
    
    let currentState = [...initialState];
    let tradeHistory = [];
    let currentModel = 'ppo'; // Default model
    
    // Elements
    const predictBtn = document.getElementById('predict-btn');
    const resetBtn = document.getElementById('reset-btn');
    const statusEl = document.getElementById('status');
    const loadingEl = document.getElementById('loading');
    const actionTextEl = document.getElementById('action-text');
    const actionDisplayEl = document.getElementById('action-display');
    const currentPriceEl = document.getElementById('current-price');
    const stateInputsEl = document.getElementById('state-inputs');
    const totalRewardEl = document.getElementById('total-reward');
    const totalProfitEl = document.getElementById('total-profit');
    const tradeCountEl = document.getElementById('trade-count');
    const tradeIndicatorsEl = document.getElementById('trade-indicators');
    const modelCards = document.querySelectorAll('.model-card');
    
    // Model selection handler
    modelCards.forEach(card => {
        card.addEventListener('click', function() {
            modelCards.forEach(c => c.classList.remove('active'));
            this.classList.add('active');
            currentModel = this.dataset.model;
            
            // Update stats when switching models
            updateModelStats();
            statusEl.textContent = `Switched to ${currentModel.toUpperCase()} model. Ready for predictions.`;
        });
    });

    // Update displayed stats for current model
    function updateModelStats() {
        totalRewardEl.textContent = modelStats[currentModel].totalReward.toFixed(6);
        totalProfitEl.textContent = modelStats[currentModel].totalProfit.toFixed(6);
    }

    // [Rest of your existing code remains the same...]
    // (chart setup, state inputs, prediction logic, etc.)

    // Initialize
    updateModelStats(); // Set initial values
    generateStateInputs();
    updateCurrentPrice();
    
    // [Keep all other existing functions unchanged]
});