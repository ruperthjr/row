import streamlit as st
import random
import math

# Title and Introduction
st.title("🌐 Idealistic Realist's Enhanced Betting Model")
st.write("Maximizing potential profits while minimizing risk in virtual sports betting.")

# Input: Bankroll Setup
st.header("💰 Set Your Bankroll")
bankroll = st.number_input("Enter your starting bankroll (KES)", min_value=500.0, step=50.0, value=1000.0)
bet_percentage = st.slider("Percentage of bankroll to bet per game (%)", 1, 10, 5)

# Markets to Focus On
market_choices = [
    "Over/Under 2.5 Goals",
    "Both Teams to Score",
    "Asian Handicap",
    "First Half/Full Time",
    "Exact Score",
    "Double Chance",
    "Total Goals",
    "Half-Time Over/Under",
    "First Team to Score"
]
st.header("🎲 Select Markets to Focus On")
markets = st.multiselect("Choose your preferred markets", market_choices, default=market_choices)

# Odds Inputs (for each option in BTTS and Over/Under 2.5)
st.header("⚙️ Input Odds for Current Game")
st.subheader("Both Teams to Score (BTTS) Odds")
btts_odds_1 = st.slider("BTTS Odds Option 1", min_value=1.1, max_value=3.5, step=0.01, value=1.9)
btts_odds_2 = st.slider("BTTS Odds Option 2", min_value=1.1, max_value=3.5, step=0.01, value=2.1)

st.subheader("Over/Under 2.5 Goals Odds")
over_under_odds_1 = st.slider("Over/Under 2.5 Odds Option 1", min_value=1.1, max_value=3.5, step=0.01, value=1.7)
over_under_odds_2 = st.slider("Over/Under 2.5 Odds Option 2", min_value=1.1, max_value=3.5, step=0.01, value=2.3)

# Asian Handicap Odds Inputs
st.subheader("Asian Handicap Odds")
asian_handicap_1 = st.slider("Asian Handicap Option 1 (e.g., +1, -1)", min_value=1.1, max_value=3.5, step=0.01, value=2.0)
asian_handicap_2 = st.slider("Asian Handicap Option 2", min_value=1.1, max_value=3.5, step=0.01, value=2.5)

# First Half/Full Time Odds Inputs
st.subheader("First Half/Full Time Odds")
first_half_full_time_1 = st.slider("First Half/Full Time Option 1", min_value=1.1, max_value=3.5, step=0.01, value=2.0)
first_half_full_time_2 = st.slider("First Half/Full Time Option 2", min_value=1.1, max_value=3.5, step=0.01, value=2.8)

# Exact Score Odds Inputs
st.subheader("Exact Score Odds")
exact_score_1 = st.slider("Exact Score Option 1 (e.g., 2-1)", min_value=1.1, max_value=20.0, step=0.01, value=15.0)
exact_score_2 = st.slider("Exact Score Option 2", min_value=1.1, max_value=20.0, step=0.01, value=12.0)

# Double Chance Odds Inputs
st.subheader("Double Chance Odds")
double_chance_1 = st.slider("Double Chance Option 1", min_value=1.1, max_value=3.5, step=0.01, value=1.5)
double_chance_2 = st.slider("Double Chance Option 2", min_value=1.1, max_value=3.5, step=0.01, value=2.1)

# Total Goals Odds Inputs
st.subheader("Total Goals Odds")
total_goals_1 = st.slider("Total Goals Option 1 (e.g., 1-3)", min_value=1.1, max_value=3.5, step=0.01, value=2.2)
total_goals_2 = st.slider("Total Goals Option 2", min_value=1.1, max_value=3.5, step=0.01, value=2.8)

# Half-Time Over/Under Odds Inputs
st.subheader("Half-Time Over/Under Odds")
half_time_1 = st.slider("Half-Time Over/Under Option 1", min_value=1.1, max_value=3.5, step=0.01, value=1.9)
half_time_2 = st.slider("Half-Time Over/Under Option 2", min_value=1.1, max_value=3.5, step=0.01, value=2.3)

# First Team to Score Odds Inputs
st.subheader("First Team to Score Odds")
first_team_to_score_1 = st.slider("First Team to Score Option 1", min_value=1.1, max_value=3.5, step=0.01, value=2.5)
first_team_to_score_2 = st.slider("First Team to Score Option 2", min_value=1.1, max_value=3.5, step=0.01, value=3.0)

# Kelly Criterion to Calculate Optimal Bet Size
def kelly_criterion(odds, probability, bankroll):
    b = odds - 1
    q = 1 - probability
    f_star = (b * probability - q) / b
    bet_fraction = max(min(f_star, bet_percentage / 100), 0)
    bet_amount = bankroll * bet_fraction
    return bet_amount

# Function to Determine Optimal Bets Based on Odds
def determine_optimal_bets(bankroll, bet_percentage, odds_dict):
    optimal_bets = {}
    
    for market, odds_options in odds_dict.items():
        for idx, odds in enumerate(odds_options):
            probability = 1 / odds  # Simulated probability (this can be refined in real-world scenarios)
            bet_amount = kelly_criterion(odds, probability, bankroll)
            potential_payout = bet_amount * odds
            optimal_bets[f"{market} Option {idx + 1}"] = {
                "Bet Amount": bet_amount,
                "Odds": odds,
                "Expected Payout": round(potential_payout, 2),
                "Probability": round(probability, 3)
            }
    
    return optimal_bets

# Execute Optimal Bets Calculation
st.header("📊 Suggested High-Potential Bets")
selected_odds = {
    "BTTS": [btts_odds_1, btts_odds_2],
    "Over/Under 2.5": [over_under_odds_1, over_under_odds_2],
    "Asian Handicap": [asian_handicap_1, asian_handicap_2],
    "First Half/Full Time": [first_half_full_time_1, first_half_full_time_2],
    "Exact Score": [exact_score_1, exact_score_2],
    "Double Chance": [double_chance_1, double_chance_2],
    "Total Goals": [total_goals_1, total_goals_2],
    "Half-Time Over/Under": [half_time_1, half_time_2],
    "First Team to Score": [first_team_to_score_1, first_team_to_score_2]
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
    st.write("No optimal bets were identified for the selected markets.")