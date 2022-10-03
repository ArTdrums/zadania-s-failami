'''Написать программу которая
В текущем каталоге создает текстовый файл stichi.txt
Записывает в него следующий стих (используя print или write)'''

f = open('stichi.txt', 'w', encoding='utf-8')
print('''We walk through the years like steps.
No need to whine that our ascent is hard.
If we suddenly don't find a new step —
The way back is always a moment.
''', file=f)

f.close()
