import time, pickle, numpy as np
from datetime import datetime

LOG_FILE = "data/rssi_log.csv"
MODEL_FILE = "model_rf.pkl"
WINDOW = 10

try:
    with open(MODEL_FILE,'rb') as f:
        clf = pickle.load(f)
except FileNotFoundError:
    print('No model file found. Run training first.')
    raise SystemExit(1)

def read_last_n(n):
    vals=[]
    try:
        with open(LOG_FILE,'r') as f:
            lines = f.readlines()
        for line in lines:
            if line.strip() and ',' in line and not line.startswith('#'):
                ts, rssi = line.strip().split(',',1)
                try:
                    vals.append(int(rssi))
                except:
                    pass
    except FileNotFoundError:
        return []
    return vals[-n:]

print('Realtime classifier started.')
while True:
    last = read_last_n(WINDOW)
    if len(last) == WINDOW:
        x = np.array(last).astype(float)
        feat = [x.mean(), x.std(), x.var(), x.min(), x.max(), x.max()-x.min()]
        pred = clf.predict([feat])[0]
        print(f"{datetime.now().strftime('%H:%M:%S')} | Predicted: {pred}")
    else:
        print('Waiting for enough samples...')
    time.sleep(1)
