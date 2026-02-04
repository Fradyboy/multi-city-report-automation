import csv
from datetime import datetime
import os


# Take multiple cities from user
cities_input = input("Enter cities (comma separated): ")
cities = [c.strip() for c in cities_input.split(",")]


# Create reports folder if not exists
os.makedirs("reports", exist_ok=True)


# Prepare summary report
summary_lines = []
summary_lines.append("MULTI-CITY REPORT SUMMARY")
summary_lines.append("------------------------")
summary_lines.append(f"Generated on: {datetime.now()}")
summary_lines.append("")


# Load CSV data once
with open("data.csv", "r") as file:
    data = list(csv.DictReader(file))


# Generate report for each city
for city in cities:
    count = 0
    report_lines = []

    report_lines.append(f"CITY REPORT: {city}")
    report_lines.append("-----------------")
    report_lines.append(f"Generated on: {datetime.now()}")
    report_lines.append("")

    for row in data:
        if row["city"].lower() == city.lower():
            report_lines.append(
                f"{row['name']} | Age: {row['age']} | City: {row['city']}"
            )
            count += 1

    report_lines.append("")
    report_lines.append(f"Total records: {count}")
    

    # Save city report
    filename = f"reports/report_{city}_{datetime.now().strftime('%Y-%m-%d')}.txt"
    with open(filename, "w") as report:
        report.write("\n".join(report_lines))

    summary_lines.append(f"{city}: {count} records")
    
    
    # Write logs
    with open("logs.txt", "a") as log:
        log.write(f"Report generated for {city} at {datetime.now()}\n")

# Save summary report
summary_file = f"reports/summary_{datetime.now().strftime('%Y-%m-%d')}.txt"
with open(summary_file, "w") as summary:
    summary.write("\n".join(summary_lines))

print("Multi-city reports generated successfully")