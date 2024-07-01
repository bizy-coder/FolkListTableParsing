import csv

with open('textTable.txt','r') as file:
	data = file.read()

lines =  data.strip().split('\n')[3:]

processed_data = []
for line in lines:
	name = line[:30].strip('~').lstrip().replace(' ', ' ')+" "
	if " or " in name:
		name = "OR: " + name.replace(" or ","")
	name = name.strip()
	birth = line[30:42].strip()
	death = line[42:54].strip()
	birthplace = line[54:].strip()
	processed_data.append([name, birth, death, birthplace])
	
with open('output.csv', 'w', newline="") as file:
	writer = csv.writer(file)
	writer.writerow(['Name', 'Birth', 'Death', 'Birthplace'])
	writer.writerows(processed_data)
