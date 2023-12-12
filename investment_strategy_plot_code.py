# Consolidated code block for calculating and plotting investment returns and inverted drawdowns
import pandas as pd
import matplotlib.pyplot as plt

# Assuming 'investment_df' is already defined with the necessary columns
# If not, the code to create 'investment_df' should be included here

# Calculate the rolling maximum of the cumulative returns to determine the peak of the investment value
investment_df['Rolling_Max'] = investment_df['Cumulative_Strategy_Returns'].cummax()
# Calculate the drawdown
investment_df['Drawdown'] = investment_df['Rolling_Max'] - investment_df['Cumulative_Strategy_Returns']

# Calculate the same for a Buy and Hold strategy
investment_df['Buy_Hold_Rolling_Max'] = investment_df['SPY_Close'].pct_change().cumsum().cummax()
investment_df['Buy_Hold_Drawdown'] = investment_df['Buy_Hold_Rolling_Max'] - investment_df['SPY_Close'].pct_change().cumsum()

# Plot the cumulative returns and inverted drawdowns
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [2, 1]})

# Cumulative returns
ax1.plot(investment_df.index, investment_df['Cumulative_Strategy_Returns'], label='Strategy')
ax1.plot(investment_df.index, investment_df['SPY_Close'].pct_change().cumsum(), label='Buy and Hold SPY')
ax1.set_title('Investment Returns: Strategy vs. Buy and Hold SPY')
ax1.set_ylabel('Cumulative Returns')
ax1.grid(True)
ax1.legend()

# Inverted drawdown
ax2.fill_between(investment_df.index, investment_df['Drawdown'], 0, label='Strategy Drawdown', alpha=0.3)
ax2.fill_between(investment_df.index, investment_df['Buy_Hold_Drawdown'], 0, label='Buy and Hold Drawdown', alpha=0.3)
ax2.set_title('Inverted Rolling Drawdown: Strategy vs. Buy and Hold SPY')
ax2.set_ylabel('Drawdown')
ax2.set_xlabel('Date')
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()
