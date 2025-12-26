# Revisiting XML Query Processing: DTD-Based Optimization

This repository implements the XML query optimization techniques described in the project documentation. The core idea is to leverage the schema information provided by **DTDs (Document Type Definitions)** to optimize XML labeling (encoding), storage, and query processing speeds compared to schema-agnostic approaches.

## 📂 Project Structure

```text
XML_Query_Optimization/
├── dtd/                     # Source DTD files (Schemas)
├── dtd-tools/               # Scripts for parsing and preprocessing DTDs
├── xml-generator-from-dtd/  # Tools to generate synthetic XML data based on DTD
├── xml-db/                  # Core Database Engine (Encoding, Storage, Querying)
├── xml-data/                # (Optional) Sample XML datasets
└── README.md
