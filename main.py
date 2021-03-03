x = 1
x = 2

while True:
    accX = Accelerometer.get_x()
    accY = Accelerometer.get_y()
    if accX > 100 and y < 4:
        y +=1
    elif accX < -100 and y > 0: 
        y -=1
    elif accY > 100 and x < 4:
        x +=1
    elif accY < -100 and > 0:
        x -=1
display.clear()
display.set-pixel(x,y,9)
sleep(100)
