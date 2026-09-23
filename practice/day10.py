# logs = [
#     "Failed login from 192.168.1.10",
#     "User logged in successfully",
#     "Failed LOGIN from 10.0.0.5"
# ]
# count = 0
# for log in logs:
#     if "Failed" in log:
#         count += 1
# print(f"Number of failed login attempts: {count}")

# for log in logs:
#     if "Failed" in log:
#         print(log)

# import re
# log = "Failed login from 192.168.1.10"
# numbers = re.findall(r"\d+", log)
# print(numbers)

#import re

# logs = [
#     "Failed login from 192.168.1.10",
#     "User admin logged in",
#     "Failed login from 10.0.0.5"
# ]

# for log in logs:
#     if "Failed" in log:
#         print("Suspicious:", log)

#         numbers = re.findall(r"\d+", log)
#         print("Numbers:", numbers)