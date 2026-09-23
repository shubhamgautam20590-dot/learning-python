# import re

# logs = [
#     "Failed login from 192.168.1.10",
#     "User admin logged in",
#     "Failed login from 10.0.0.5"
# ]

# for log in logs:
#     if "Failed" in log:
#         numbers = re.findall(r"\d+", log)
#         print(numbers)
        
# failed_logs = []    #create an empty list to store failed logs  

# for log in logs:
#     if "Failed" in log:
#         failed_logs.append(log) 

# print(failed_logs)

count = 0

# for log in logs:
#     if "Failed" in log:
#         count += 1

# print("Suspicious entries:", count)
 

import re
logs = [
    "Failed login",
    "Success login",
    "Failed login"
]
failed_logs = []
for log in logs:
    if re.search(r"Failed", log):
        failed_logs.append(log)
print(failed_logs)