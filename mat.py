from forex_python.converter import CurrencyRates
from datetime import *
import matplotlib.pyplot as plt

listetime=list()
listerateusd=list()
listerateeur=list()
listeratejpy=list()
listerategbp=list()
listeratecad=list()
listerateaud=list()
listeratechf=list()
# listeratedkk=list()

dt=date.today()
delta=timedelta(days=1)

c=CurrencyRates()

for i in range(31):
    listetime.append(dt)
    listerateusd.append(c.get_rate("USD", "TRY", dt))
    listerateeur.append(c.get_rate("EUR","TRY",dt))
    listeratejpy.append(c.get_rate("JPY","TRY",dt)*100)
    listerategbp.append(c.get_rate("GBP", "TRY", dt))
    listeratecad.append(c.get_rate("CAD", "TRY", dt))
    listerateaud.append(c.get_rate("AUD","TRY",dt))
    listeratechf.append(c.get_rate("CHF","TRY",dt))
    # listeratedkk.append(c.get_rate("DKK","TRY",dt))
    dt=dt-delta

x=listetime
y=listerateusd
y2=listerateeur
y3=listeratejpy
y4=listerategbp
y5=listeratecad
y6=listerateaud
y7=listeratechf
# y8=listeratedkk

plt.plot(x,y,marker="o")
plt.plot(x,y2,marker="o")
plt.plot(x,y3,marker="o")
plt.plot(x,y4,marker="o")
plt.plot(x,y5,marker="o")
plt.plot(x,y6,marker="o")
plt.plot(x,y7,marker="o")
# plt.plot(x,y8,marker="o")

plt.legend(["USD","EUR","JPY(*100)","GBP","CAD","AUD","CHF"])
plt.show()





