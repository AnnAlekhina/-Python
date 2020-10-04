sec=int(input('Введите время в секундах: '))
hours=0
minute=0
if (sec // 3600)>0:
    hours= sec//3600
    sec=sec-3600*hours
if (sec//60)>0:
    minute=sec//60
    sec=sec-60*minute
res=('%02d:%02d:%02d'%(hours,minute,sec))
print('Результат: ', res)