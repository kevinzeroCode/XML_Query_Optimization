from pathlib import Path
from lxml import etree
from pymongo import MongoClient

# 1. 連線到 Mongo
client = MongoClient("mongodb://localhost:27017")
db = client["xmldb"]
col = db["nitf_mongo"]

# 清空舊資料（可以保留也可以註解掉）
col.delete_many({})

# 2. NITF 檔案所在目錄（跟你之前一樣放 nitf_sample.*.xml 的地方）
data_dir = Path("/home/m11415015/dtd-tools")

xml_files = sorted(data_dir.glob("nitf_sample*.xml"))
print(f"Found {len(xml_files)} xml files")

for path in xml_files:
    with open(path, "rb") as f:
        doc = etree.parse(f)

    root = doc.getroot()

    # 這裡跟你在 JSONB 那邊做的一樣：抓 root tag、change.time、body_text
    change_time = root.get("change.time")  # <nitf change.time="14:00">
    body_elems = root.xpath("//body")
    body_text = body_elems[0].text if body_elems else ""

    doc_json = {
        "root_tag": root.tag,
        "filename": path.name,
        "change_time": change_time,
        "body_text": body_text,
    }

    col.insert_one(doc_json)
    print("Inserted", path.name)

print("Done.")

