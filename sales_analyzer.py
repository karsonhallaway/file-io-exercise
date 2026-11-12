import csv
# Read sales_data.csv using csv.DictReader
with open('sales_data.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    sales_data = list(reader)
    for row in sales_data:
        row['price'] = float(row['price'])
        row['quantity'] = int(row['quantity'])
        


# === Calculations: ==== 
# Calculate total_revenue = sum(price * quantity for each row) 
total_revenue = sum(row['price'] * row['quantity'] for row in sales_data)


# Calculate revenue per product 
revenue_per_product = {}
for row in sales_data:
    product = row['product']
    if product not in revenue_per_product:
        revenue_per_product[product] = 0
    revenue_per_product[product] += row['price'] * row['quantity']



# Calculate total quantity sold per product 
quantity_per_product = {}
for row in sales_data:
    product = row['product']
    if product not in quantity_per_product:
        quantity_per_product[product] = 0
    quantity_per_product[product] += row['quantity']


# Calculate the day with the highest total revenue
revenue_per_day = {}
for row in sales_data:
    day = row['date']
    if day not in revenue_per_day:
        revenue_per_day[day] = 0
    revenue_per_day[day] += row['price'] * row['quantity']

highest_revenue_day = max(revenue_per_day, key=revenue_per_day.get)


# === Formatted Summary: ===
# Writes formatted summary to sales_report.txt
with open('sales_report.txt', 'w') as file:
    file.write(f"Total Revenue: {total_revenue:.2f}\n")
    file.write("Revenue per Product:\n")
    for product, revenue in revenue_per_product.items():
        file.write(f"  {product}: {revenue:.2f}\n")
    file.write("Quantity per Product:\n")
    for product, quantity in quantity_per_product.items():
        file.write(f"  {product}: {quantity}\n")
    file.write(f"Highest Revenue Day: {highest_revenue_day} with revenue {revenue_per_day[highest_revenue_day]:.2f}\n")


# Writes a summary CSV called product_summary.csv with colums: product, total_quantity, total_revenue
with open('product_summary.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['product', 'total_quantity', 'total_revenue'])
    for product in revenue_per_product:
        writer.writerow([product, quantity_per_product[product], revenue_per_product[product]])



