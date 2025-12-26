import os
import psycopg2
from lxml import etree
from psycopg2.extras import Json

# 1. 連線資訊依照你現在 docker / postgres 設定
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="xmldb",
    user="xmluser",
    password="xmlpass"
)
conn.autocommit = True
cur = conn.cursor()

# 2. 從 nitf_xml_raw 讀全部資料
cur.execute("SELECT id, filename, doc FROM nitf_xml_raw;")
rows = cur.fetchall()

def extract_fields(xml_text: str) -> dict:
    """
    從 NITF XML 抽一些欄位出來做 JSON：
    - root tag
    - 一些常見屬性 (version, change.date, change.time, baselang)
    - 第一個 <title> 文字
    - 整個 <body> 的純文字 (當作全文)
    """
    data = {}
    try:
        root = etree.fromstring(xml_text.encode("utf-8"))
    except Exception as e:
        # 解析失敗就只存 raw
        return {"parse_error": str(e)[:200], "raw_xml_snippet": xml_text[:500]}

    # root 資訊
    data["root_tag"] = root.tag
    for attr in ["version", "change.date", "change.time", "baselang", "uno", "class"]:
        if attr in root.attrib:
            data[attr.replace(".", "_")] = root.attrib[attr]

    # 標題：抓第一個 <title>
    title_el = root.find(".//title")
    if title_el is not None and title_el.text:
        data["title"] = title_el.text.strip()

    # 範例：抓第一個 <hedline> / <hl1> 的文字（如果有）
    hedline_el = root.find(".//hedline")
    if hedline_el is not None:
        hl1_el = hedline_el.find(".//hl1")
        if hl1_el is not None and hl1_el.text:
            data["headline"] = hl1_el.text.strip()

    # 全文：body 的純文字 (可能會很亂，但之後可以用來做全文搜尋)
    body_el = root.find(".//body")
    if body_el is not None:
        text = " ".join(body_el.itertext())
        data["body_text"] = text[:2000]  # 先截斷，以免太大

    return data

insert_sql = """
INSERT INTO nitf_jsonb (id, filename, data)
VALUES (%s, %s, %s)
ON CONFLICT (id) DO UPDATE
SET filename = EXCLUDED.filename,
    data     = EXCLUDED.data;
"""

for row in rows:
    id_, filename, doc = row
    # doc 是 pg 的 xml 型別，轉成字串
    xml_text = str(doc)
    json_data = extract_fields(xml_text)
    cur.execute(insert_sql, (id_, filename, Json(json_data)))
    print(f"Upserted id={id_}, filename={filename}")

cur.close()
conn.close()
print("Done.")

