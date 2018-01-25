path = "/home/paritosh/PycharmProjects/training/oop/Google Stock Market Data - google_stock_data.csv.csv"

lines = [lines for lines in open(path)]

print(lines[1])
dataset=[line.strip().split(",") for line in open(path)]

print(dataset[0])