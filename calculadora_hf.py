#sobre a calculadora
print('\nA calculadora consiste em: seu antecessor, seu sucessor, seu dobro, seu triplo, sua raiz quadrada, sua tabuada, tabela de medidas por metro, conversor de moedas e média de 5 algaritmos.')
#informações do número
print('\nInformações do número:')
n = int(input('Digite um número: '))
print('\nAnalisando o número {}, seu antecessor é {} e seu sucessor é {}'.format(n, (n-1), (n+1)))
print('\nO dobro de {}, é {}'.format(n, (n*2)))
print('\nO triplo de {}, é {}'.format(n, (n*3)))
print('\nA raiz quadrada de {}, é {:.2f}'.format(n, (n**(1/2))))
print('\nA tabuada de {} é \n{} x 1 = {}; \n{} x 2 = {}; \n{} x 3 = {}; \n{} x 4 = {}; \n{} x 5 = {}; \n{} x 6 = {}; \n{} x 7 = {}; \n{} x 8 = {}; \n{} x 9 = {}; \n{} x 10 = {}.'.format(n, n, (n*1), n, (n*2), n, (n*3), n, (n*4), n, (n*5), n, (n*6), n, (n*7), n, (n*8), n, (n*9), n, (n*10)))
km = n/10/10/10
hm = n/10/10
dam = n/10
dm = n*10
cm = n*10*10
mm = n*10*10*10
print('\nTabela de medidas por metro do número {}: \n{:.4f} quilômetro(km); \n{} hectômetro(hm); \n{:.4f} decâmetro(dam); \n{} metro(m); \n{} decímetro(dm); \n{} centímetro(cm); \n{} milímetro(mm);\n'.format(n, km, dam, hm, n, dm, cm, mm))
#conversor de moedas
print('Conversor de moedas:')
real = float(input('Digite a quantia: R$ '))
dolarAmericano = real*5.08
euro = real*5.21
libraEsterlina = real*6.16
iene = real*0.038
francoSuiça = real*5.39
dolarCanadense = real*3.27
print('R${} convertido em dolar americano é {}'.format(real, dolarAmericano))
print('R${} convertido em dolar canadense é {}'.format(real, dolarCanadense))
print('R${} convertido em euro é {}'.format(real, euro))
print('R${} convertido em libra esterlina é {}'.format(real, libraEsterlina))
print('R${} convertido em iene é {}'.format(real, iene))
print('R${} convertido em franco suiça é {}\n'.format(real, francoSuiça))