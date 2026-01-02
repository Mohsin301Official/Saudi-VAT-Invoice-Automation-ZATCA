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
*(Yahan aap apne ek generated Invoice PDF ka screenshot laga sakte hain)*

---
*Developed by Mustansar - Open for Data Analyst roles in Riyadh.*
