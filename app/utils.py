
def get_propfirm_rules(firm):
    rules = {
        "FTMO": {"phase": "2", "targets": [10, 5], "daily": 5, "max": 10, "min_days": 10},
        "FunderPro": {"phase": "1", "targets": [14], "daily": 4, "max": 7},
        "FundedNext - Stellar 1": {"phase": "1", "targets": [10], "daily": 3, "max": 6},
        "FundedNext - Stellar 2": {"phase": "2", "targets": [8, 5], "daily": 5, "max": 10, "min_days": 5},
        "MyForexFunds": {"phase": "2", "targets": [8, 5], "daily": 5, "max": 12, "min_days": 5},
        "FundingPips": {"phase": "2", "targets": [8, 5], "daily": 5, "max": 10, "min_days": 3},
        "FundingPipsX": {"phase": "1", "targets": [10], "daily": 4, "max": 8, "min_days": 3}
    }
    return rules.get(firm, {})

def calculate_drawdown(rules, account_size, equity, daily_loss, total_loss):
    daily_limit = account_size * (rules['daily'] / 100)
    max_limit = account_size * (rules['max'] / 100)

    if daily_loss > daily_limit:
        dd_status = f"❌ Daily Loss Limit Exceeded! (${daily_loss} > ${daily_limit})"
    else:
        dd_status = f"✅ Within Daily Loss Limit (${daily_loss} / ${daily_limit})"

    if total_loss > max_limit:
        phase_status = f"❌ Max Drawdown Breached! (${total_loss} > ${max_limit})"
    else:
        phase_status = f"✅ Max Drawdown OK (${total_loss} / ${max_limit})"

    return dd_status, phase_status
