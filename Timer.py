#Making a timer in format: Hours:Minutes:Seconds.fraction
import time
fraction=0
sec=0
minute=0
hour=0
#Clock that runs forever
while True:
    fraction+=1
    time.sleep(.1)
    if fraction==10:
        fraction=0
        sec+=1
    if sec==60:
        sec=0
        minute+=1
    if minute==60:
        minute=0
        hour+=1
    if hour==24:
        hour=0
#Formatted the time so that it would have 0 in the front.
    print((format(hour,'02d')), (format(minute,'02d')), (format(sec,'02d')), (format(fraction,'02d')), sep=':')
 
