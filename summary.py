import sys #Access command-line arguments
from collections import Counter #Count occurences and store it in dictionary
filename = sys.argv[1] #Get the log in variable filename
with open(filename) as f: #Open the log file
    lines=f.readlines() #Read all lines 
print("Total lines:", len(lines))#Print total lines
 
counts=Counter() #Create 
for line in lines:
    fields = line.split()
    if len(fields) > 7:
        key = fields[7]
        counts[key] +=1

print("Top 5:")
for item, n in counts.most_common(5):
    print(item, n)
    
