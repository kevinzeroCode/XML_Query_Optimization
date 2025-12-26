import time
import statistics
import psycopg2

# === 這裡換成你實際的帳號 / 密碼 ===
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "xmldb",
    "user": "xmluser",
    "password": "xmlpass"   # 如果你之前設的是 123456 就改成 "123456"
}

# 跑幾次（可以改大一點，例如 100、500）
RUNS = 50

# 三種查詢方式
QUERIES = {
    "xml_xpath": """
        SELECT id, filename
        FROM nitf_xml_raw
        WHERE xpath('/nitf/@change.time', doc)::text = '{14:00}';
    """,
    "xml_generated_col": """
        SELECT id, filename
        FROM nitf_xml_raw
        WHERE change_time = '14:00';
    """,
    "jsonb_change_time": """
        SELECT id, filename
        FROM nitf_jsonb
        WHERE data->>'change_time' = '14:00';
    """
}

def run_benchmark():
    conn = psycopg2.connect(**DB_CONFIG)
    conn.autocommit = True
    cur = conn.cursor()

    # 確保沒有把 enable_seqscan 關掉
    cur.execute("SET enable_seqscan = on;")

    results = {}

    for name, sql in QUERIES.items():
        print(f"\n=== Running benchmark for: {name} ===")
        times = []

        # 簡單 warm-up 一次，避免第一次很慢
        cur.execute(sql)
        cur.fetchall()

        for i in range(RUNS):
            start = time.perf_counter()
            cur.execute(sql)
            _rows = cur.fetchall()
            end = time.perf_counter()

            elapsed_ms = (end - start) * 1000
            times.append(elapsed_ms)

        results[name] = times

    cur.close()
    conn.close()
    return results

def summarize(results):
    print("\n================ Benchmark Summary (ms) ================")
    for name, times in results.items():
        avg = statistics.mean(times)
        median = statistics.median(times)
        min_t = min(times)
        max_t = max(times)
        print(f"\n[{name}]")
        print(f"  runs   : {len(times)}")
        print(f"  avg    : {avg:.3f} ms")
        print(f"  median : {median:.3f} ms")
        print(f"  min    : {min_t:.3f} ms")
        print(f"  max    : {max_t:.3f} ms")

if __name__ == "__main__":
    results = run_benchmark()
    summarize(results)

