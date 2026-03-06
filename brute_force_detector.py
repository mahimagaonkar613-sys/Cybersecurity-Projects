import csv
from collections import defaultdict

FAILED_LIMIT = 3
failed_attempts = defaultdict(int)

suspicious_ips = []

# Read log file
with open("login_logs.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        ip = row["ip"]
        status = row["status"]

        if status == "failed":
            failed_attempts[ip] += 1

# Detect suspicious IPs
for ip, count in failed_attempts.items():
    if count >= FAILED_LIMIT:
        print("Possible Brute Force Attack Detected")
        print("IP Address:", ip)
        print("Failed Attempts:", count)
        print()

        suspicious_ips.append((ip, count))

# Save blocklist
if suspicious_ips:
    with open("blocklist.txt", "w") as block:
        for ip, count in suspicious_ips:
            block.write(ip + "\n")

# Generate security report
with open("security_report.txt", "w") as report:
    report.write("Security Report\n")
    report.write("-----------------\n")

    if suspicious_ips:
        for ip, count in suspicious_ips:
            report.write(f"Suspicious IP: {ip}\n")
            report.write(f"Failed Attempts: {count}\n")
            report.write("Risk Level: HIGH\n\n")
    else:
        report.write("No suspicious activity detected\n")

print("Scan completed")
print("Blocklist saved to blocklist.txt")
print("Security report generated")