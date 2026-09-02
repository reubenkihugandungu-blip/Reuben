import numpy as np

# 4 weeks of daily steps (28 days)
steps_28 = np.array([
    9200, 10500, 8800, 11000, 7600, 9400, 10200,
    8900, 10800, 9100, 11200, 7900, 10000, 9700,
    9500, 10300, 8600, 11500, 8200, 9800, 10600,
    9000, 10100, 8400, 10900, 7500, 9600, 10400,
])
print(f"28-day step analysis")
print(f" Mean:        {np.mean(steps_28):,.0f}")
print(f" Median:      {np.median(steps_28):,.0f}")
print(f" Std Dev:     {np.std(steps_28):,.0f}")
print(f" Min:         {np.min(steps_28):,.0f}")
print(f" Max:         {np.max(steps_28):,.0f}")
print(f" Total:       {np.sum(steps_28):,.0f}")
print(f" 75th Pctile: {np.percentile(steps_28, 75):,.0f}")
print(f" Days 10k+:   {np.sum(steps_28 >= 10000)}/28")