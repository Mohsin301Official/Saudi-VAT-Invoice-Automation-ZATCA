# Saudi VAT Invoice Automation System (ZATCA Compliant)

## 📌 Project Overview
An automated Python-based solution designed to generate **ZATCA Phase 1 (Fatoora)** compliant tax invoices. This system processes raw sales data from Excel, calculates VAT (15%), generates cryptographic **TLV (Tag-Length-Value) Base64 QR Codes**, and exports professional PDF invoices suitable for the Saudi market.

## 🚀 Key Features
* **ZATCA Compliance:** Implements official TLV encoding for QR Code generation (Seller Name, VAT No, Timestamp, Total, VAT).
* **Arabic Support:** Handles UTF-8 Arabic text rendering correctly using `Arabic-Reshaper` and `Bidi`.
* **Automated Workflow:** Converts bulk Excel data into individual PDF invoices in seconds.
* **Error Free:** Eliminates manual calculation errors in VAT (15%).

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** `Pandas` (ETL), `FPDF` (PDF Generation), `Qrcode`, `Base64`

## 📸 Sample Output
<img width="553" height="586" alt="image" src="https://github.com/user-attachments/assets/7761f95e-3cc0-4845-95fd-f26aa7296e9a" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/6538a91c-18e4-4bcd-91f4-c17f7b7e4a04" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/533c467c-206c-4f3d-bca2-aa5e4b6a7d49" />

---
*Developed by Mustansar - Open for Data Analyst roles in Riyadh.*
