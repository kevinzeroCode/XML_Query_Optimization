import time
from statistics import mean, median
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["xmldb"]
col = db["nitf_mongo"]

N_RUNS = 50
times = []

# 先暖機一次
col.count_documents({"change_time": "14:00"})

for _ in range(N_RUNS):
    t0 = time.perf_counter()
    list(col.find({"change_time": "14:00"}, {"_id": 1, "filename": 1}))
    dt = (time.perf_counter() - t0) * 1000  # ms
    times.append(dt)

print("runs   :", N_RUNS)
print("avg    : {:.3f} ms".format(mean(times)))
print("median : {:.3f} ms".format(median(times)))
print("min    : {:.3f} ms".format(min(times)))
print("max    : {:.3f} ms".format(max(times)))

