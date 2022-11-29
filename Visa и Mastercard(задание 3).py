import matplotlib.pyplot as plt
import numpy as np
from random import randint
import statistics as stat


visa_list = []
with open('Visa.txt') as file:
    while (line := file.readline().rstrip()):
        line = line[0:4]
        line = line.replace(',', '.')
        visa_list.append(float(line))

mastercard_list = []
with open('MasterCard.txt') as file:
    while (line := file.readline().rstrip()):
        line = line[0:4]
        line = line.replace(',', '.')
        mastercard_list.append(float(line))

print('Visa',visa_list)
print('MasterCard',mastercard_list )

a= stat.correlation(visa_list, mastercard_list)
print("коэффициент корреляции Пирсона:",a)


visa_vinz = []
mastercard_vinz = []

for i in range(len(visa_list)):
    visa_vinz.append(visa_list[i])
    mastercard_vinz.append(mastercard_list[i])

for i in range(250):
    index = randint(0, len(visa_vinz) - 1)
    if visa_vinz[index] != []:
        visa_vinz[index] = []
    if mastercard_vinz[index] != []:
        mastercard_vinz[index] = []

visa_appr = []
visa_corrl = []
mastercard_appr = []
mastercard_corrl = []
for i in range(len(visa_list)):
    visa_appr.append(visa_vinz[i])
    visa_corrl.append(visa_vinz[i])
    mastercard_appr.append(mastercard_vinz[i])
    mastercard_corrl.append(mastercard_vinz[i])

print('Visa', visa_vinz)
print('MasterCard', mastercard_vinz)

#Винзорирование
def vinz(list):
    for i in range(len(list)):
        if list[i] == []:
            index = -1
            index_next = i
            index_previous = i
            while True:
                index_next += 1
                index_previous -= 1
                if index_next < len(list) and list[index_next] != []:
                    index = index_next
                    break
                if index_previous >= 0 and list[index_previous] != []:
                    index = index_previous
                    break
            list[i] = list[index]

vinz(visa_vinz)
vinz(mastercard_vinz)
print('Винзорирование:')
print('Visa', visa_vinz)
print('MasterCard', mastercard_vinz)

#Линейная аппроксимация
def appr(list):
    for i in range(len(list)):
        if list[i] == []:
            index_next = i
            index_priveous = i
            while True:
                index_next += 1
                if index_next >= len(list) or list[index_next] != []:
                    break
            while True:
                index_priveous -= 1
                if index_priveous < 0 or list[index_priveous] != []:
                    break
            if index_next >= len(list):
                index_next = index_priveous - 1
                while True:
                    if index_next >= 0 and list[index_next] != []:
                        break
                    index_next -= 1

            if index_priveous < 0:
                index_priveous = index_next + 1
                while True:
                    if index_priveous < len(list) and list[index_priveous] != []:
                        break
                    index_priveous += 1
            if list[index_priveous] == list[index_next]:
                list[i] = list[index_next]
            else:
                a = (index_priveous - index_next) / (list[index_priveous] - list[index_next])
                b = index_next - a * list[index_next]
                list[i] = (i - b)/a

appr(visa_appr)
appr(mastercard_appr)
print('Линейная аппроксимация')
print('Visa', visa_appr)
print('MasterCard', mastercard_appr)

#Корреляционное восстановление
def corrl(list_one, list_two):
    for i in range(len(list_one)):
        if list_one[i] == []:
            index = -1
            index_next = i
            index_priveous = i
            while True:
                index_next += 1
                index_priveous -= 1
                if index_next < len(list_one) and list_one[index_next] != []:
                    index = index_next
                    break
                if index_priveous >= 0 and list_one[index_priveous] != []:
                    index = index_priveous
                    break
            list_one[i] = (list_two[i]/list_two[index])*list_one[index]

corrl(visa_corrl, mastercard_list)
corrl(mastercard_corrl, visa_list)
print('корреляционное восстановление')
print('Visa', visa_corrl)
print('MasterCard', mastercard_corrl)


fig, ax = plt.subplots(4,2)
ax[0,0].set_title("Обычный набор данных Visa")
ax[0,0].plot(visa_list, color = 'green')
ax[1,0].set_title("Винзорирование")#Visa
ax[1,0].plot(visa_vinz)
ax[1,0].plot(visa_list, color = 'green')
ax[0,1].set_title("Обычный набор данных MasterCard")
ax[0,1].plot(mastercard_list, color = 'red')
ax[1,1].set_title("Винзорирование")#MasterCard
ax[1,1].plot(mastercard_vinz)
ax[1,1].plot(mastercard_list, color = 'red')
ax[2,0].set_title("Линейная аппроксимация")#Visa
ax[2,0].plot(visa_appr)
ax[2,0].plot(visa_list, color = 'green')
ax[2,1].set_title("Линейная аппроксимация")#MasterCard
ax[2,1].plot(mastercard_appr)
ax[2,1].plot(mastercard_list, color = 'red')
ax[3,0].set_title("Корреляционное восстановление")#Visa
ax[3,0].plot(visa_corrl)
ax[3,0].plot(visa_list, color = 'green')
ax[3,1].set_title("Корреляционное восстановление")#MasterCard
ax[3,1].plot(mastercard_corrl)
ax[3,1].plot(mastercard_list, color = 'red')
for ax in ax.flat:
    ax.label_outer()
plt.show()
