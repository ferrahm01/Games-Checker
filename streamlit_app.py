import streamlit as st
import random

st.title("SHA-256 Hash Decoder Function")
             
seed = st.text_input(label = "SHA-256 Hash Code:", placeholder="Enter the hash to decode", key="seed_input", type="password")

def Analyse_Hash_Code(hash):

    arc1 = random.randint(0,300)/100
    variance = random.randint(0,8200)/100
    return arc1, variance

def Calculate_amount(base, expt):
    bet_amount = base * (expt / 100)
    return bet_amount

def Calculate_Return(chance1, variance):
    feat_val = chance1/2 * 100
    win_val = variance/75 * 100
    expt_return = feat_val + win_val / 2
    bet_amount = Calculate_amount(float(bet.strip("$")), expt_return)
    expt_return = round(expt_return, 2)
    bet_amount = round(bet_amount, 2)
    return expt_return, bet_amount

def Display_Results(chance1, win):
    st.write("Feature Chance: ", chance1, "%")
    st.write("Win Chance:", win, "%")
    expt_return, bet = Calculate_Return(chance1, win)
    st.write("Expected return: ", expt_return, "%")
    st.write("**Recommended Bet: $**", bet)

bet_levels = ["$0.05", "$0.10", "$0.15", "$0.20", "$0.25", "$0.30", "$0.40", "$0.50", "$0.60", "$0.70", "$0.80", "$0.90",  "$1.00", "$1.10", "$1.20", "$1.25", "$1.30", "$1.40", "$1.50", "$1.75", "$2.00", "$2.50", "$3.00", "$4.00", "$5.00", "$6.00", "$7.50", "$10.00", "$15.00", "$20.00", "$25.00", "$50.00", "$75.00", "$100.00", "$150.00", "$200.00", "$250.00", "$300.00", "$400.00", "$500.00", "$750.00", "$1000.00"]
bet = st.selectbox("Select Base Bet Amount:", options=bet_levels)

if st.button("Decode"):
    if len(seed) > 10:
        chance1, variance = Analyse_Hash_Code(seed)
        Display_Results(chance1, variance)
    elif not seed:
        st.error("Please enter a hash to decode.")
    else:
        st.error("Please enter a valid hash.")

if st.button("Next Spin"):
    if len(seed) > 10:
        chance1, variance = Analyse_Hash_Code(seed)
        Display_Results(chance1, variance)
    elif not seed:
        st.error("Please enter a hash to decode.")
    else:
        st.error("Please enter a valid hash.")




    
