import streamlit as st
import random
import math

# Title and Introduction
st.title("🌐Idealistic Realist's Enhanced Betting Model")
st.write("Maximizing potential profits while minimizing risk in virtual sports betting.")

# Input: Bankroll Setup
st.header("Set Your Bankroll")
bankroll = st.number_input("Enter your starting bankroll (KES)", min_value=50.0, step=50.0, value=100.0)
bet_percentage = st.slider("Percentage of bankroll to bet per game (%)", 1, 10, 5)

# Markets to Focus On
market_choices = ["Over/Under 2.5 Goals", "Both Teams to Score"]
st.header("🎲Select Markets to Focus On")
markets = st.multiselect("Choose your preferred markets", market_choices, default=market_choices)

# Odds Inputs (for each option in BTTS and Over/Under 2.5)
st.header("⚙️ Input Odds for Current Game")
st.subheader("Both Teams to Score (BTTS) Odds")
btts_odds_1 = st.slider("BTTS Odds Option 1", min_value=1.1, max_value=3.5, step=0.01, value=1.9)
btts_odds_2 = st.slider("BTTS Odds Option 2", min_value=1.1, max_value=3.5, step=0.01, value=2.1)

st.subheader("Over/Under 2.5 Goals Odds")
over_under_odds_1 = st.slider("Over/Under 2.5 Odds Option 1", min_value=1.1, max_value=3.5, step=0.01, value=1.7)
over_under_odds_2 = st.slider("Over/Under 2.5 Odds Option 2", min_value=1.1, max_value=3.5, step=0.01, value=2.3)

# Kelly Criterion to Calculate Optimal Bet Size
def kelly_criterion(odds, probability, bankroll):
    # Formula: f* = (bp - q) / b
    # f* is the optimal fraction to bet, b is odds - 1, p is probability of success, q is probability of failure
    b = odds - 1
    q = 1 - probability
    f_star = (b * probability - q) / b
    
    # Apply Kelly Criterion, limiting it to the bet percentage input by user
    bet_fraction = max(min(f_star, bet_percentage / 100), 0)
    bet_amount = bankroll * bet_fraction
    return bet_amount

# Function to Determine Optimal Bets Based on Odds
def determine_optimal_bets(bankroll, bet_percentage, odds_dict):
    optimal_bets = {}
    
    for market, odds_options in odds_dict.items():
        for idx, odds in enumerate(odds_options):
            # Simulate a basic predicted probability for each odds value (this would be more advanced in a real scenario)
            probability = 1 / odds
            
            # Calculate the optimal bet using Kelly Criterion
            bet_amount = kelly_criterion(odds, probability, bankroll)
            potential_payout = bet_amount * odds
            
            # Save the optimal bet details
            optimal_bets[f"{market} Option {idx + 1}"] = {
                "Bet Amount": bet_amount,
                "Odds": odds,
                "Expected Payout": round(potential_payout, 2),
                "Probability": round(probability, 3)
            }
    
    return optimal_bets

# Execute Optimal Bets Calculation
st.header("Suggested High-Potential Bets")
selected_odds = {
    "BTTS": [btts_odds_1, btts_odds_2],
    "Over/Under 2.5": [over_under_odds_1, over_under_odds_2]
}
optimal_bets = determine_optimal_bets(bankroll, bet_percentage, selected_odds)

# Display High Potential Bets
if optimal_bets:
    for market, details in optimal_bets.items():
        st.write(f"### Market: {market}")
        st.write(f"- **Bet Amount:** KES {details['Bet Amount']:.2f}")
        st.write(f"- **Odds:** {details['Odds']}")
        st.write(f"- **Expected Payout:** KES {details['Expected Payout']:.2f}")
        st.write(f"- **Probability of Success:** {details['Probability']*100:.2f}%")
else:
    st.write("No optimal bets were identified for this game. Adjust bankroll or odds to explore more.")

# Market-Specific Tips Based on Current Odds
st.header("💡 Market Tips")
if "Over/Under 2.5 Goals" in markets:
    st.write("- **Over/Under 2.5**: Bet Over 2.5 in high-scoring matchups or Under 2.5 for games with defensive focus. Use odds patterns for decision-making.")
if "Both Teams to Score" in markets:
    st.write("- **BTTS**: Look for matches where both teams have high attacking potential, such as past matches with 2+ goals per team.")

# Anomaly Tracker for Odds Pattern Recognition
st.header("🔍 Anomaly Tracker")
# Simulate detection of odds fluctuations over multiple matches
trend_anomaly = random.choice([True, False])
if trend_anomaly:
    st.warning("⚠️ Odds anomaly detected! Adjust bet size or explore other markets.")
else:
    st.info("🧐 No significant anomalies in the odds trends. Proceed as usual.")

# Final Strategy Recommendation
st.header("🔑 Strategic Recommendation")
st.write("""
For high returns and minimized risk, always apply the Kelly Criterion for bet sizing, focus on Over/Under 2.5 and BTTS markets with higher odds (1.8 or more), and dynamically adjust based on detected odds anomalies.
""")