
import streamlit as st
from utils import get_propfirm_rules, calculate_drawdown

st.set_page_config(page_title="Supreme PropFirm Trading Calculator", layout="wide")

st.title("💼 Supreme Prop Firm Risk Calculator")
firm = st.selectbox("Choose your Prop Firm", ["FTMO", "FunderPro", "FundedNext - Stellar 1", "FundedNext - Stellar 2", "MyForexFunds", "FundingPips", "FundingPipsX"])
account_size = st.number_input("Account Size ($)", min_value=1000, step=100)
equity = st.number_input("Current Equity ($)", min_value=0.0, value=account_size * 1.0)
daily_loss = st.number_input("Today's Loss ($)", min_value=0.0, value=0.0)
total_loss = st.number_input("Total Loss ($)", min_value=0.0, value=0.0)

rules = get_propfirm_rules(firm)
dd_status, phase_status = calculate_drawdown(rules, account_size, equity, daily_loss, total_loss)

st.subheader("📋 Firm Rules")
st.json(rules)

st.subheader("📊 Evaluation Status")
st.success(dd_status)
st.info(phase_status)

st.caption("Developed with ❤️ for funded traders.")
