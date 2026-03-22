import numpy as np

# Simulated CMS data stream
data = np.random.normal(0, 1, 100)

# Inject anomaly
data[50] = 10  

threshold = 3

def detect_anomalies(data, threshold):
    anomalies = []
    for i, value in enumerate(data):
        if abs(value) > threshold:
            anomalies.append((i, value))
    return anomalies

anomalies = detect_anomalies(data, threshold)

print("Detected Anomalies:")
for idx, val in anomalies:
    print(f"Index {idx} -> Value {val}")
