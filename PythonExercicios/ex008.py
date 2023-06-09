n = float(input('Digite um número em metros: '))
dm = n*10
cm = n*100
mm = n*1000
dam = n/10
hm = n/100
km = n/1000
print('A medida {:.0f} em metros, é correspondente a: \n{:.1f}dm \n{:.1f}cm \n{:.1f}mm \n{:.1f}dam \n{:.1f}hm \n{:.1f}km'.format(n, dm, cm, mm, dam, hm, km))
