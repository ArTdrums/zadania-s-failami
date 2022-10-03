'''
Представленный файл, разбить на 4 файла, каждый из которых содержит по одному абзацу стиха
'''
f = open('../zadanie3.txt', 'r', encoding='utf-8')
f1 = open('zadanie3.1txt.', 'w', encoding='utf-8')
f2 = open('zadanie3.2txt.', 'w', encoding='utf-8')
f3 = open('zadanie3.3txt.', 'w', encoding='utf-8')
f4 = open('zadanie3.4txt.', 'w', encoding='utf-8')
s = f.read()  # считтываем исходный файл
print(type(s))
a = s.split('\n')  # разбиваем его по строкам далее далеам записть в файлы  по срезам
print(a)

fail_1 = a[0:4]
print(fail_1)
for i in fail_1:
    print(i, file=f1)
f1.close()
fail_2 = a[5:9]
for i in fail_2:
    print(i, file=f2)
f2.close()
fail_3 = a[10:15]
for i in fail_3:
    print(i, file=f3)
f3.close()
fail_4 = a[16:20]
for i in fail_4:
    print(i, file=f4)
f4.close()
f.close()
