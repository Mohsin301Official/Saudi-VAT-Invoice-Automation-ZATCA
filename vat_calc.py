import pandas as pd
import os
import base64
import qrcode
from fpdf import FPDF
import arabic_reshaper            # NEW: Arabic letters ko jodne ke liye
from bidi.algorithm import get_display # NEW: Right-to-Left likhne ke liye

# --- FUNCTION TO FIX ARABIC TEXT ---
def make_arabic(text):
    """
    Arabic text ko PDF ke liye compatible banata hai.
    """
    if not text:
        return ""
    reshaped_text = arabic_reshaper.reshape(str(text)) # Letters ko jodo
    bidi_text = get_display(reshaped_text) # Right-to-Left karo
    return bidi_text

# --- PART 1: ZATCA TLV FUNCTIONS ---
def generate_tlv_hex(tag_num, value):
    value_str = str(value)
    value_bytes = value_str.encode('utf-8')
    tag_byte = bytes([tag_num])
    length_byte = bytes([len(value_bytes)])
    return tag_byte + length_byte + value_bytes

def get_zatca_base64(seller_name, vat_number, timestamp, total_amount, vat_amount):
    tlv1 = generate_tlv_hex(1, seller_name)
    tlv2 = generate_tlv_hex(2, vat_number)
    tlv3 = generate_tlv_hex(3, timestamp)
    tlv4 = generate_tlv_hex(4, total_amount)
    tlv5 = generate_tlv_hex(5, vat_amount)
    all_tlvs = tlv1 + tlv2 + tlv3 + tlv4 + tlv5
    return base64.b64encode(all_tlvs).decode('utf-8')

# --- PART 2: QR IMAGE FUNCTION ---
def create_qr_image(base64_data, filename):
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(base64_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# --- PART 3: PDF INVOICE CLASS (UPDATED FOR ARABIC) ---
class ZATCA_Invoice(FPDF):
    def header(self):
        # Yahan hum Arial Font load kar rahe hain jo Arabic support karta hai
        # Make sure 'arial.ttf' folder mein मौजूद ho
        try:
            self.add_font('ArialCustom', '', 'arial.ttf', uni=True)
            self.set_font('ArialCustom', '', 16)
        except:
            print("Warning: 'arial.ttf' nahi mila. Default font use hoga (Arabic kharab ho sakti hai).")
            self.set_font('Arial', 'B', 16)
            
        self.cell(0, 10, 'AL-RIYADH TECH SOLUTIONS', 0, 1, 'C')
        self.set_font_size(10)
        self.cell(0, 10, 'VAT No: 310000000000003 | Riyadh, KSA', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font_size(8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_pdf(invoice_data, qr_path, output_filename):
    pdf = ZATCA_Invoice()
    pdf.add_page()

    # Font set karna zaroori hai
    try:
        pdf.add_font('ArialCustom', '', 'arial.ttf', uni=True)
        pdf.set_font('ArialCustom', '', 12)
    except:
        pdf.set_font('Arial', '', 12)

    # Invoice Details (Arabic Function use karein)
    cust_name = make_arabic(invoice_data['Customer_Name']) # Arabic Fix
    
    pdf.cell(100, 10, f"Invoice #: {invoice_data['Invoice_ID']}", 0, 1)
    pdf.cell(100, 10, f"Date: {invoice_data['Date']}", 0, 1)
    # Arabic naam print karne ke liye:
    pdf.cell(100, 10, f"Customer: {cust_name}", 0, 1)
    
    pdf.ln(10)

    # Table Header
    pdf.set_fill_color(200, 220, 255)
    # Note: Table headers English mein hi rakhein taake layout na tute
    pdf.cell(80, 10, 'Description', 1, 0, 'C', 1)
    pdf.cell(30, 10, 'Amount', 1, 0, 'C', 1)
    pdf.cell(30, 10, 'VAT (15%)', 1, 0, 'C', 1)
    pdf.cell(40, 10, 'Total', 1, 1, 'C', 1)

    # Table Row
    pdf.cell(80, 10, 'IT Services', 1)
    pdf.cell(30, 10, str(invoice_data['Amount']), 1, 0, 'C')
    pdf.cell(30, 10, str(invoice_data['VAT_Amount']), 1, 0, 'C')
    pdf.cell(40, 10, str(invoice_data['Total_Amount']), 1, 1, 'C')

    # Add QR Code
    pdf.image(qr_path, x=140, y=200, w=35)
    pdf.output(output_filename)

# --- PART 4: MAIN EXECUTION ---
file_path = 'invoices.xlsx'
if not os.path.exists(file_path):
    print("Error: Excel file nahi mili!")
else:
    df = pd.read_excel(file_path)
    print(f"Loaded {len(df)} invoices.")

    # Calculations
    VAT_RATE = 0.15
    df['VAT_Amount'] = df['Amount'] * VAT_RATE
    df['Total_Amount'] = df['Amount'] + df['VAT_Amount']
    df = df.round(2)

    SELLER_NAME = "My Saudi Company"
    SELLER_VAT_NO = "310000000000003"

    print("\n--- Starting Generation with Arabic Support ---")
    for index, row in df.iterrows():
        # Timestamp
        timestamp = f"{str(row['Date']).split()[0]} {str(row['Time'])}"

        # Base64
        base64_code = get_zatca_base64(
            SELLER_NAME, 
            SELLER_VAT_NO, 
            timestamp, 
            str(row['Total_Amount']), 
            str(row['VAT_Amount'])
        )

        # QR Image
        qr_filename = f"qr_{index}.png"
        create_qr_image(base64_code, qr_filename)

        # PDF
        pdf_filename = f"Invoice_{row['Invoice_ID']}.pdf"
        generate_pdf(row, qr_filename, pdf_filename)
        
        print(f"Generated: {pdf_filename}")

        # Cleanup
        if os.path.exists(qr_filename):
            os.remove(qr_filename)

    print("\nProcess Complete.")