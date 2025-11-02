import csv, time, random, os

os.makedirs('data', exist_ok=True)
fpath = 'data/sim_rssi.csv'
with open(fpath,'w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['timestamp','rssi'])
    for i in range(300):
        r = random.randint(-70,-40)
        w.writerow([time.strftime('%Y-%m-%d %H:%M:%S'), r])
        time.sleep(0.05)
print('Simulated data written to', fpath)
