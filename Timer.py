#Part 1
#Number 1:
#Constructing a rectange using height, width, and character. 
def Make_character_rectangle(height, width, char):
    row = 1
    while(row <= height):
        print(width*char)
        row+=1
#Make_character_rectangle(2, 3, "^")

#Number 2:
#The parallelogram has to be slanted, so we need to consider the spaces that will be present in the beginning
def Make_character_parallelogram(height,width,char):
    row= 1
    while(row <= height):
        #height-row is multiplied by space because the number of space in the beginning is equal to height-row.
       print((height-row)*' '+ (width*char))
       row+=1
#Make_character_parallelogram(8,19,'&')

#Number 3:
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
 
