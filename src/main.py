import PySimpleGUI as sg
import csv
import os

#sg.theme('DarkAmber')
sg.theme('Dark Grey 13')
items = [[],[]]

CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.csv"))

with open(CONFIG_PATH, newline='') as csvfile:
    myReader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in myReader:
        items[0].append(row[0])
        items[1].append(row[1])

longest = ''
for word in items[0]:
    if len(word) > len(longest):
        longest = word

i = 0
for word in items[0]:
    items[0][i] = word + (' ' * (len(longest)-len(word)))
    i += 1

print(items[0])

layout = []

for item, price in zip(items[0], items[1]):
    layout.append([sg.Text(item), sg.Input('0', key=item), sg.Text(price+'kr')])

layout.append([sg.Text('Pris:'), sg.Text('0kr', key='-PRICE-')])
layout.append([sg.Button('Calculate'), sg.Button('Exit')])

window = sg.Window('Anchormen', layout)

while True:
    event, values = window.read()
    if event is None or event == 'Exit':
        break
    if event == 'Calculate':
        total_price = 0.0
        for item, price in zip(items[0], items[1]):
            total_price += float(values[item]) * float(price)
            window['-PRICE-'].update(str(total_price)+'kr')

window.close()
