import pandas as pd
import glob
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle, sys

files = glob.glob('data/rssi_*.csv')
if not files:
    print('No labeled files found in data/. Example: rssi_low_01.csv')
    sys.exit(1)

rows = []
for f in files:
    if 'low' in f:
        label='low'
    elif 'med' in f or 'medium' in f:
        label='medium'
    elif 'high' in f:
        label='high'
    else:
        label='unknown'
    df = pd.read_csv(f)
    r = df['rssi'].astype(float)
    rows.append({
        'mean': r.mean(),
        'std': r.std(),
        'var': r.var(),
        'min': r.min(),
        'max': r.max(),
        'range': r.max()-r.min(),
        'label': label
    })

data = pd.DataFrame(rows)
X = data.drop(columns=['label'])
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
print(classification_report(y_test, pred))
with open('model_rf.pkl','wb') as f:
    pickle.dump(clf, f)
print('Model saved to model_rf.pkl')
