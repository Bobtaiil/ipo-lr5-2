symbol = 0        #инициализация переменной

str_first=str(input("Введите первую строку"))        #ввод с калвиатуры первой строки

str_replace=str_first.replace(" ","")        #удаление пробеллов
 
len_str_first=len(str_replace)        #длина первой строки

str_second=str(input("Введите вторую строку"))        #ввод второй строки

for i in str_second:        #перебор символов второй строки

 if i in str_replace:        #циклы проверки
  symbol += 1
if symbol==len_str_first:
 
  print("Ваша строка анограмма")        #ответ
else:
  print("Ваша строка не анограмма")