# sales_stats.py
# Basic script to analyze a list of sales figures

sales = [1200, 950, 1830, 760, 2100, 1450, 990]

total = sum(sales)
average = total / len(sales)
maximum = max(sales)
minimum = min(sales)

print("Sales Data:", sales)
print("Total Sales:", total)
print("Average Sale:", round(average, 2))
print("Highest Sale:", maximum)
print("Lowest Sale:", minimum)