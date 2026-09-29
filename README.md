# vshop
its like a e-shopping app for clothes ,beauty  products ,footwear ,skin care etc. 
🛍️ Welcome to V-Shop! V-Shop is a interactive command-line shopping assistant written in Python. V-Shop simulates an e‑commerce experience right inside your terminal complete with user authentication categorized browsing, cart management and automated receipt generation.

✨ Features

• Secure Sign‑in Simulation: V-Shop validates 10‑digit numbers and creates a random 4‑digit OTP for a realistic login flow.

• Dynamic Address Selector: V-Shop auto‑detects your location (pre‑set to VIT Bhopal University). Lets you enter a custom delivery address.

• Deep Catalog Browsing: V-Shop lets you explore four core shopping categories split into sub‑options:

• 👚 Clothes: V-Shop offers options for Men, Women and Kids along with size selectors.

• 🧴 Hair Care: V-Shop has shampoos, conditioners and hair oils.

• 🧼 Body Care: V-Shop includes body washes, soaps, face washes and lotions.

• 👟 Footwear: V-Shop lists sneakers, heels, sandals and sports shoes.

• Simulated Checkout: V-Shop shows cart totals confirms delivery and estimates a random delivery date.

• Itemized Billing: V-Shop prints a summary receipt with local timestamps, full item names and calculated spend totals.

🚀 Getting Started

Prerequisites

Make sure Python 3.x is installed on your system. No other libraries or external dependencies are needed.

Running the App

1. Save the script as vshop.py.

2. Open your terminal. Command prompt.

3. Launch the app by running:bash python vshop.py

Use code with caution.

🕹️ How to Use

1. Authentication: Enter your name and a valid 10‑digit mobile number. Copy the simulated OTP printed on the screen to log in successfully.

2. Set Address: Choose your default campus location. Input a fresh shipping address.

3. Shop: Navigate through the menus to browse collections view current prices and add items to your cart.

4. Checkout: Confirm your cash‑on‑delivery order.

5.. Exit: Type 1 or yes when prompted to keep adding more items or press any other key to close your session and get your printable receipt.

🛠️ Code Structure Overview

• is_valid_phone(phone): V-Shop confirms if user entry is a 10‑digit number.

• verify_otp(otp generated_otp): V-Shop handles the verification comparison.

• address(): V-Shop sets delivery destination routing.

• delivery(): V-Shop calculates a delivery date within 30 days and confirms COD terms.

• show_receipt(shopped spend): V-Shop compiles custom item lists. Totals the final currency amounts.

Would you like me to help you refactor the logic to make it more modular or add support for real‑time database storage, for the products?
