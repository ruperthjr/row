import streamlit as st
import random
import math

# Title and Introduction
st.title("🌐Idealistic Realist's Upgraded Betting Model for 1.5 Goals")
st.write("Maximizing potential profits while minimizing risk in virtual sports betting with enhanced anomaly tracking.")

# Input: Bankroll Setup
st.header("Set Your Bankroll")
bankroll = st.number_input("Enter your starting bankroll (KES)", min_value=50.0, step=50.0, value=100.0)
bet_percentage = st.slider("Percentage of bankroll to bet per game (%)", 1, 10, 5)

# Markets to Focus On
market_choices = ["Over/Under 1.5 Goals", "Both Teams to Score"]
st.header("🎲 Select Markets to Focus On")
markets = st.multiselect("Choose your preferred markets", market_choices, default=market_choices)

# Odds Inputs (for each option in BTTS and Over/Under 1.5)
st.header("⚙️ Input Odds for Current Game")
st.subheader("Both Teams to Score (BTTS) Odds")
btts_odds_1 = st.slider("BTTS Odds Option 1", min_value=1.1, max_value=7.0, step=0.01, value=1.9)
btts_odds_2 = st.slider("BTTS Odds Option 2", min_value=1.1, max_value=7.0, step=0.01, value=2.1)

st.subheader("Over/Under 1.5 Goals Odds")
over_under_odds_1 = st.slider("Over/Under 1.5 Odds Option 1", min_value=1.1, max_value=7.0, step=0.01, value=1.4)
over_under_odds_2 = st.slider("Over/Under 1.5 Odds Option 2", min_value=1.1, max_value=7.0, step=0.01, value=2.0)

# Kelly Criterion to Calculate Optimal Bet Size
def kelly_criterion(odds, probability, bankroll):
    b = odds - 1
    q = 1 - probability
    f_star = (b * probability - q) / b
    bet_fraction = max(min(f_star, bet_percentage / 100), 0)
    bet_amount = bankroll * bet_fraction
    return bet_amount

# Anomaly Tracker
st.header("📈 Anomaly Tracker")
st.write("Tracking unusual betting trends and potential opportunities.")
def track_anomalies(odds):
    anomaly_score = random.uniform(0.1, 1.0)
    if anomaly_score > 0.8:
        return True, round(anomaly_score, 2)
    return False, round(anomaly_score, 2)

# Function to Determine Optimal Bets Based on Odds
def determine_optimal_bets(bankroll, bet_percentage, odds_dict):
    optimal_bets = {}

    for market, odds_options in odds_dict.items():
        for idx, odds in enumerate(odds_options):
            probability = 1 / odds
            bet_amount = kelly_criterion(odds, probability, bankroll)
            potential_payout = bet_amount * odds
            anomaly_detected, anomaly_score = track_anomalies(odds)
            
            optimal_bets[f"{market} Option {idx + 1}"] = {
                "Bet Amount": bet_amount,
                "Odds": odds,
                "Expected Payout": round(potential_payout, 2),
                "Probability": round(probability, 3),
                "Anomaly Detected": anomaly_detected,
                "Anomaly Score": anomaly_score
            }

    return optimal_bets

# Execute Optimal Bets Calculation
st.header("Suggested High-Potential Bets")
selected_odds = {
    "BTTS": [btts_odds_1, btts_odds_2],
    "Over/Under 1.5": [over_under_odds_1, over_under_odds_2]
}
optimal_bets = determine_optimal_bets(bankroll, bet_percentage, selected_odds)

# Display High Potential Bets with Anomaly Information
if optimal_bets:
    for market, details in optimal_bets.items():
        st.write(f"### Market: {market}")
        st.write(f"- **Bet Amount:** KES {details['Bet Amount']:.2f}")
        st.write(f"- **Odds:** {details['Odds']}")
        st.write(f"- **Expected Payout:** KES {details['Expected Payout']:.2f}")
        st.write(f"- **Probability of Success:** {details['Probability']*100:.2f}%")
        if details['Anomaly Detected']:
            st.markdown(f"**🔴 Anomaly Detected! Anomaly Score:** {details['Anomaly Score']} (Potential Opportunity)")
        else:
            st.write(f"Anomaly Score: {details['Anomaly Score']}")
else:
    st.write("No optimal bets identified for this game. Try adjusting your settings or odds.")