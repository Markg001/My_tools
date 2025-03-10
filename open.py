#! usr/env/bin python3
#How to open a file in a simple way 


m = ("server.log.txt")
with open(m, "w")as file:
    file.write("\n2025-02-24 12:10:05,123 - INFO - User John logged in"
"\n2025-02-24 12:12:34,456 - ERROR - Database connection failed"
"\n2025-02-24 12:15:20,789 - WARNING - Disk space low"
"\n2025-02-24 12:18:50,111 - INFO - User Jane logged in"
"\n2025-02-24 12:20:11,222 - ERROR - Permission denied for user John"
"\n2025-02-24 12:25:55,333 - INFO - File upload successful"
"\n2025-02-24 12:30:30,444 - ERROR - Server timeout"
"\n2025-02-24 12:35:42,555 - WARNING - High memory usage detected")

errorcount=0
with open(m,"r")as file:
    for line in file:
        print(line.strip())
        if "ERROR" in line:
            errorcount += 1
    print(f"\nTotal ERRORS count:{errorcount}")
    if "ERROR" in line:
            print(line.strip())
        
