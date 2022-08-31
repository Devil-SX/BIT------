import random 
from datetime import date, timedelta

f = open('Temperature.txt','w',encoding='utf-8')

d = date.today() + timedelta(days = -13)
for i in range(14):
	temp = 36.5+round(random.random()*(37.2-36.5),1)# 人体标准体温36.5-37.2度（来自百度）
	string = str(d.month)+'.'+str(d.day)+' '+str(temp)+'℃;'
	f.write(string)
	d += timedelta(days = 1)