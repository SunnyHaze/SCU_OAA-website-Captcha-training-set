import csv
data = []
# 读取数据
with open("label.csv", 'r', newline="" , encoding="utf8") as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
# 预览数据
for line in data:
    print(line)