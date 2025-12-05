import re

pattern = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+-\s+-\s+\[(?P<datetime>[^\]]+)\]\s+"[^"]+"\s+(?P<status>\d{3})'
)

with open("sample.log", "r") as file, open("output.txt", "a") as output_file:
    for line in file:
        match = pattern.search(line)
        if match:
            ip = match.group("ip")
            timestamp = match.group("datetime")
            status = match.group("status")

            output = f"{ip}, {timestamp}, {status}"
            output_file.write(output + "\n")
