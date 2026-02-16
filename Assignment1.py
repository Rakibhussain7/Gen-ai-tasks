# 1. User Login Check
username_input = "admin"
password_input = "1234"

if username_input == "admin" and password_input == "1234":
    print("1. Login Successful")
else:
    print("1. Invalid Credentials")

# 2. Pass / Fail Analyzer
marks = [45, 78, 90, 33, 60]
pass_count = 0
fail_count = 0

for m in marks:
    if m >= 50:
        pass_count += 1
    else:
        fail_count += 1

print(f"2. Pass Students: {pass_count}, Fail Students: {fail_count}")

# 3. Simple Data Cleaner
names = [" Alice ", "bob", " CHARLIE "]
cleaned_names = [name.strip().lower() for name in names]
print(f"3. Cleaned Names: {cleaned_names}")

# 4. Message Length Analyzer
messages = ["Hi", "Welcome to the platform", "OK"]
print("4. Message Analysis:")
for msg in messages:
    length = len(msg)
    status = " (Long Message)" if length > 10 else ""
    print(f"   - '{msg}': {length} chars{status}")

# 5. Error Message Detector
logs = ["INFO", "ERROR", "WARNING", "ERROR"]
error_count = logs.count("ERROR")
print(f"5. Total Error Count: {error_count}")
