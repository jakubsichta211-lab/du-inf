import csv
dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
dic2 = {}
subor = open("data.csv","r", encoding="UTF-8")
counter = 0
citac = csv.reader(subor)
next(citac)
for riadok in citac:
    pocet_umrti = riadok[5]
    if pocet_umrti.isdigit() and pocet_umrti != "0":
        counter+=1
        first_digit = pocet_umrti[0]
        dic[int(first_digit)] += 1
for i in dic:
    dic2[i] = round(dic[i] / counter * 100,2)
print(dic)
print(dic2)
