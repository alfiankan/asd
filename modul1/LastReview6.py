def tigaAtauLima(x):
    if(x%3==0 and x%5==0):
        print('Bilangan itu kelipatan 3 dan 5 sekaligus')
    elif x%3==0:
        print('Bilangan itu adalah kelipatan 3')
    elif x%5==0:
        print('Bilangan itu adalah kelipatan 5')
    else:
        print('Bilangan itu bukan kelipatan 3 maupun 5')

tigaAtauLima(9)
tigaAtauLima(10)
tigaAtauLima(15)
tigaAtauLima(17)