import pandas as pd
from datetime import datetime, timedelta
import random
import numpy as np

def generate_entry(charger_id, timestamp):
    faulted = random.random() < 0.1
    label = 1 if faulted else 0
    
    return {
        "timestamp": timestamp.isoformat() + "Z",
        "charger_id": charger_id,
        "mean_voltage": round(random.uniform(215, 235), 2),
        "std_current": round(random.uniform(0.5, 5.0), 2),
        "max_current": round(random.uniform(10, 20), 2),
        "min_voltage": round(random.uniform(210, 225), 2),
        "energy_delta": round(random.uniform(0.5, 5.0), 2),
        "pct_time_faulted": round(random.uniform(0.0, 1.0 if faulted else 0.3), 2),
        "status_transitions": random.randint(1, 6),
        "status_entropy": round(random.uniform(0.3, 2.0), 2),
        "boot_events": random.randint(0, 2),
        "boot_interval_mean": round(random.uniform(0.5, 6.0), 2),
        "heartbeat_loss_rate": round(random.uniform(0.0, 0.5), 2),
        "charging_session_count": random.randint(0, 3),
        "charging_success_rate": round(random.uniform(0.0, 1.0), 2),
        "mean_session_duration": round(random.uniform(0.0, 60.0), 2),
        "time_since_last_fault": random.randint(0, 24),
        "fault_duration_avg": round(random.uniform(0.0, 2.0), 2),
        "fault_burst_count": random.randint(0, 5),
        "mean_voltage_6h": round(random.uniform(215, 235), 2),
        "max_faults_24h": random.randint(0, 8),
        "heartbeat_gap_std": round(random.uniform(0.1, 2.0), 2),
        "label": label
    }

# Generate dataset
start_time = datetime(2025, 1, 1, 0, 0)
hours = 24*30*12 # 12 months of hourly data
chargers = ["CHG_001", "CHG_002", "CHG_003", "CHG_004", "CHG_005"]
data = []

for hour in range(hours):
    for charger in chargers:
        ts = start_time + timedelta(hours=hour)
        data.append(generate_entry(charger, ts))

df = pd.DataFrame(data)
df.to_csv("synthetic_ocpp_sample.csv", index=False)