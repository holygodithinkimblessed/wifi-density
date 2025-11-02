import pandas as pd
import matplotlib.pyplot as plt
import sys

FILE = "data/rssi_log.csv"
try:
    df = pd.read_csv(FILE)
except FileNotFoundError:
    print("No data file found:", FILE)
    sys.exit(1)

df['rssi'] = df['rssi'].astype(float)
print("Count:", len(df))
print("Mean: {:.2f}, Std: {:.2f}, Var: {:.2f}".format(df['rssi'].mean(), df['rssi'].std(), df['rssi'].var()))

df['moving_avg'] = df['rssi'].rolling(window=10, min_periods=1).mean()
plt.figure(figsize=(10,4))
plt.plot(df['rssi'], label='rssi', alpha=0.6)
plt.plot(df['moving_avg'], label='moving_avg(10)', linewidth=1.5)
plt.legend()
plt.xlabel('Index')
plt.ylabel('RSSI (dBm)')
plt.title('RSSI Time Series')
plt.grid(True)
plt.tight_layout()
plt.show()
