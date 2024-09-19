import math
#r=int(input("Введите значение r: "))
#print("Длина кружности равна",round(2*math.pi*r,2),"\nПлощадь круга равна",round(math.pi*(r**2),2))

#x=10
#y=55
#print(x,y)
#x,y=y,x
#print(x,y)

#g=9.81
#l=float(input("Введите значение l"))
#print(round(2*math.pi*((l/g)**0.5),2))

#n1=float(input("n1="))
#n2=float(input("n2="))
#if n2==0:
#    print("Ошибка, деление на ноль")
#else:
#    print("n1/n2=",n1/n2)

#s=float(input("Стоимость покупки= "))
#if s>20:
#    s=s*0.65
#print("Итоговая стоимость:",round(s,2))

a={1:"Январь",2:"Февраль",3:"Март",4:"Апрель",5:"Май",6:"Июнь",7:"Июль",8:"Август",9:"Сентябрь",10:"Октябрь",11:"Ноябрь",12:"Декабрь"}
g=int(input("Номер месяца: "))
if g in a:
    print(a[g])
else:
    print("Ошибка")
