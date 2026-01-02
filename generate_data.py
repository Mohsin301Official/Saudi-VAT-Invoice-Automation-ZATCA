import pandas as pd
import random
from datetime import datetime, timedelta

# 1. Setup Data Lists (English & Arabic Mix)
# Riyadh market ke hisaab se realistic naam
customers = [
    "Al-Nour Est", "مؤسسة النور", 
    "Riyadh Trading Co", "شركة الرياض التجارية", 
    "Tech Solutions", "حلول التقنية", 
    "Saudi Foods", "الأطعمة السعودية", 
    "Delta Construction", "شركة دلتا للمقاولات",
    "Alpha Market", "أسواق ألفا",
    "Red Sea Logistics", "الخدمات اللوجستية للبحر الأحمر",
    "Future Vision", "رؤية المستقبل"
]

data = []

# 2. Generate 50 Rows of Dummy Data
print("Generating 50 Invoices...")

for i in range(1, 51):
    # Invoice ID (INV-1001 se start)
    inv_id = f"INV-{1000 + i}"
    
    # Random Customer
    cust_name = random.choice(customers)
    
    # Date (Current Month - Jan 2026)
    # Aaj ki date se pichle 30 din mein koi bhi random date
    random_days = random.randint(0, 30)
    date_obj = datetime.now() - timedelta(days=random_days)
    date_str = date_obj.strftime("%Y-%m-%d")
    
    # Time (Random HH:MM:SS)
    hour = random.randint(8, 22) # Subah 8 se Raat 10 tak
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    time_str = f"{hour:02d}:{minute:02d}:{second:02d}"
    
    # Amount (100 se 5000 ke beech random float)
    amount = round(random.uniform(100.00, 5000.00), 2)
    
    # Row add karein
    data.append([inv_id, cust_name, date_str, time_str, amount])

# 3. DataFrame Create Karna
df = pd.DataFrame(data, columns=["Invoice_ID", "Customer_Name", "Date", "Time", "Amount"])

# 4. Excel File Save Karna
file_name = "invoices.xlsx"
df.to_excel(file_name, index=False)

print(f"Success! '{file_name}' ban gayi hai jisme 50 invoices hain.")
print("Ab aap apna 'vat_calc.py' run kar sakte hain.")