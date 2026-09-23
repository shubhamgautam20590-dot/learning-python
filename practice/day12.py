# import re

# text = "Failed login from 192.168.1.10"

# ips = re.findall(r"\d+", text)

# print(ips)
# import re

# text = "Failed login from 192.168.1.10"

# ip = re.findall(r"\d+\.\d+\.\d+\.\d+", text)

# print(ip)
# import re

# logs = [
#     "Failed login from 192.168.1.10",
#     "User admin logged in from 10.0.0.5",
#     "Failed login from 172.16.0.2"
# ]

# for log in logs:
#     ip = re.findall(r"\d+\.\d+\.\d+\.\d+", log)

#     if ip:
#         print(ip)

# import re

# logs = [
#     "Failed login from 192.168.1.10",
#     "User admin logged in from 10.0.0.5",
#     "Failed login from 172.16.0.2"
# ]

# ips = []

# for log in logs:
#     found = re.findall(r"\d+\.\d+\.\d+\.\d+", log)

#     if found:
#         ips.append(found[0])

# print(ips)

import re
logs = [
    "Failed login from 192.168.1.10",
    "User admin logged in from 10.0.0.5",
    "Failed login from 172.16.0.2",
    "User root logged in"
]
ips = []

for log in logs:
    found = re.findall(r"\d+\.\d+\.\d+\.\d+", log)

    if found:
        ips.append(found[0])

print(ips)
