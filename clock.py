from datetime import datetime
now = datetime.now()
date = now.strftime('>CLOCK DIGITAL<\n%H:%M:%S %p\n%d/%m/%Y\n========================\n%A, %d %B %Y')
print(date)