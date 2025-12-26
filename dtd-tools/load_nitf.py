import psycopg2
from pathlib import Path

# 依照你現在的設定填入
DB_NAME = "xmldb"
DB_USER = "xmluser"
DB_PASSWORD = "xmlpass"   # <=== 這裡改成你自己的
DB_HOST = "localhost"
DB_PORT = 5432

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
)

cur = conn.cursor()

xml_dir = Path(".")  # 目前目錄 ~/dtd-tools
files = sorted(xml_dir.glob("nitf_sample*.xml"))

print(f"Found {len(files)} files")

for path in files:
    with path.open("r", encoding="utf-8") as f:
        xml_content = f.read()
    cur.execute(
        "INSERT INTO nitf_xml_raw (filename, doc) VALUES (%s, %s)",
        (path.name, xml_content),
    )
    print("Inserted", path.name)

conn.commit()
cur.close()
conn.close()
print("Done.")

