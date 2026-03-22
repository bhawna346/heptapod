import numpy as np

# Simulated detector data
data = np.random.normal(50, 5, 100)

# Inject anomalies
data[10] = 100
data[50] = 120

# Calculate Z-score
mean = np.mean(data)
std = np.std(data)

threshold = 2.5

print("Anomaly Detection Results:\n")

for i, value in enumerate(data):
    z_score = (value - mean) / std
    if abs(z_score) > threshold:
        print(f"Anomaly detected at index {i}: value = {value:.2f}")
