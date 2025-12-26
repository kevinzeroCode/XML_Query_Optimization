# XML Query Optimization: PostgreSQL vs MongoDB

本專案旨在評估與比較 **關聯式資料庫 (PostgreSQL)** 與 **文件型資料庫 (MongoDB)** 在處理大規模 XML 資料時的效能差異。

實驗重點包含：
1.  **混合資料來源**：結合 Wikipedia 真實爬蟲資料與 DTD 規則生成的合成資料。
2.  **結構化優化**：比較原始 XML 儲存與轉型為 **JSONB (PostgreSQL)** 及 **BSON (MongoDB)** 後的查詢效率。
3.  **自動化實驗流程**：從資料生成、ETL (Extract-Transform-Load) 到基準測試 (Benchmarking) 的完整腳本。

---

## 🛠️ 1. 環境準備 (Prerequisites)

請確保您的系統已安裝以下工具：
* **Docker Desktop** (務必啟動並確認左下角為綠色狀態)
* **Python 3.10+** (建議使用 Conda)
* **Java Runtime (JRE)** (用於執行 MSV 資料生成器)

### 安裝 Python 依賴
```bash
# 建立虛擬環境 (推薦)
conda create -n xmlgen python=3.10 -y
conda activate xmlgen

# 安裝必要套件
pip install flask flask-wtf psycopg2-binary pymongo lxml requests
```
## 🐳 2. 啟動資料庫 (Start Databases)
本實驗使用 Docker 容器化部署 PostgreSQL 與 MongoDB。
```bash
# 1. 啟動 PostgreSQL (位於 xml-db 目錄)
cd xml-db
docker-compose up -d

# 2. 啟動 MongoDB (手動啟動容器)
docker run -d --name mongo-xml -p 27017:27017 mongo:7

# 3. 確認容器狀態 (STATUS 應為 Up)
docker ps
```
## ⚙️ 3. 下載生成工具 (Setup DTD Tools)
由於版權與檔案大小考量，本專案不包含 Java JAR 執行檔。請執行以下指令下載 Sun MSV Generator 等必要工具。

請進入工具目錄：
```bash
cd ../dtd-tools
```
下載指令 (Windows CMD): 請逐行執行以下指令：
```bash
curl -L --ssl-no-revoke -o msv-generator.jar [https://repo1.maven.org/maven2/net/java/dev/msv/msv-generator/2013.6.1/msv-generator-2013.6.1.jar](https://repo1.maven.org/maven2/net/java/dev/msv/msv-generator/2013.6.1/msv-generator-2013.6.1.jar)
curl -L --ssl-no-revoke -o msv-core.jar [https://repo1.maven.org/maven2/net/java/dev/msv/msv-core/2013.6.1/msv-core-2013.6.1.jar](https://repo1.maven.org/maven2/net/java/dev/msv/msv-core/2013.6.1/msv-core-2013.6.1.jar)
curl -L --ssl-no-revoke -o xsdlib.jar [https://repo1.maven.org/maven2/net/java/dev/msv/xsdlib/2013.6.1/xsdlib-2013.6.1.jar](https://repo1.maven.org/maven2/net/java/dev/msv/xsdlib/2013.6.1/xsdlib-2013.6.1.jar)
curl -L --ssl-no-revoke -o relaxngDatatype-1.0.jar [https://repo1.maven.org/maven2/relaxngDatatype/relaxngDatatype/1.0/relaxngDatatype-1.0.jar](https://repo1.maven.org/maven2/relaxngDatatype/relaxngDatatype/1.0/relaxngDatatype-1.0.jar)
curl -L --ssl-no-revoke -o isorelax-20030108.jar [https://repo1.maven.org/maven2/isorelax/isorelax/20030108/isorelax-20030108.jar](https://repo1.maven.org/maven2/isorelax/isorelax/20030108/isorelax-20030108.jar)
curl -L --ssl-no-revoke -o xercesImpl-2.12.2.jar [https://repo1.maven.org/maven2/xerces/xercesImpl/2.12.2/xercesImpl-2.12.2.jar](https://repo1.maven.org/maven2/xerces/xercesImpl/2.12.2/xercesImpl-2.12.2.jar)
curl -L --ssl-no-revoke -o xml-resolver-1.2.jar [https://repo1.maven.org/maven2/xml-resolver/xml-resolver/1.2/xml-resolver-1.2.jar](https://repo1.maven.org/maven2/xml-resolver/xml-resolver/1.2/xml-resolver-1.2.jar)
```
## 🏭 4. 生成實驗數據 (Generate Data)
使用 Java MSV 根據 DTD 結構生成 100 筆隨機 XML 樣本。

執行生成指令 (Windows CMD)： (注意：Windows 使用 ; 作為 Classpath 分隔符)

```bash
java -cp "msv-generator.jar;msv-core.jar;xsdlib.jar;relaxngDatatype-1.0.jar;isorelax-20030108.jar;xercesImpl-2.12.2.jar;xml-resolver-1.2.jar" com.sun.msv.generator.Driver -dtd ../dtd/nitf-3-0.dtd -root nitf -n 100 nitf_sample.$.xml
```
資料歸檔： 生成後，建議將檔案整理至數據目錄：
```bash
# 確保目錄存在
mkdir -p ../xml-data/nitf
# 移動生成的 xml 檔案
move nitf_sample*.xml ../xml-data/nitf/
```
## 📊 5. 執行效能評測 (Run Benchmarks)
現在我們將比較 PostgreSQL (JSONB 優化) 與 MongoDB 的查詢速度。請確保終端機位於 dtd-tools/ 目錄下。

### 🐘 實驗 A: PostgreSQL (Relational + JSONB)
此實驗包含三個步驟：載入 -> 轉換格式 -> 跑分。
載入原始 XML
```bash
python load_nitf.py
```
功能：將 XML 檔案讀取並存入 Postgres 的 raw_xml_table。

轉換為 JSONB 並建立索引 (關鍵步驟)
```bash
python xml_to_jsonb.py
```
執行基準測試
```bash
python benchmark_queries.py
```
觀察重點：比較 Raw XML Query Time 與 JSONB Query Time 的巨大差異。

### 🍃 實驗 B: MongoDB (NoSQL Document)
載入並轉換資料
```bash
python load_nitf_mongo.py
```
功能：解析 XML 並直接映射為 MongoDB Document (BSON) 格式存入。

執行基準測試
```bash
python mongo_benchmark.py
```
觀察重點：紀錄查詢耗時，並與 Postgres JSONB 的結果進行比較。