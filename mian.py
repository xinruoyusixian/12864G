from LCD_12864G import LCD_12864G
import time,framebuf,font,
display=LCD_12864G()

def num(numbers,zimo,width=8,x=0,y=1):
  length=len(numbers)
  for a in range(0,length):
    if numbers[a]==':':
      index=10
    else:
      index=int(numbers[a])
    draw(zimo[index],width,x,y)
    x+=width
  
#使用 @timed_function
def timed_function(f, *args, **kwargs):
    myname = str(f).split(' ')[1]
    def new_func(*args, **kwargs):
        t = time.ticks_us()
        result = f(*args, **kwargs)
        delta = time.ticks_diff(time.ticks_us(), t)
        print('Function {} Time = {:6.3f}ms'.format(myname, delta/1000))
        return result
    return new_func  

def loop(t= 10):
    while 1:
      Pin(15,1)
      Pin(12,0)
      for a in range(0,100):
        _t=time.localtime()
        s=str("%02d" % _t[3])+str(":%02d" % _t[4])+str(":%02d" % _t[5])  
        time.sleep_ms(t)
        num(s,font.num16x32,16,0,5) 
        draw(font.hlwd[0],32,a)
        draw(font.hlwd[1],32,a+32)
        draw(font.hlwd[2],32,a+64)
        draw(font.hlwd[3],32,a+64+32)
      Pin(15,0)
      Pin(12,1)
      for a in range(0,100):
        _t=time.localtime()
        s=str("%02d" % _t[3])+str(":%02d" % _t[4])+str(":%02d" % _t[5])  
        time.sleep_ms(t)
        draw(font.hlwd[0],32,100-a)
        draw(font.hlwd[1],32,100-a-32)
        draw(font.hlwd[2],32,100-a-64)
        draw(font.hlwd[3],32,100-a-64-32)
        num(s,font.num16x32,16,0,5) 

      
loop()
display.pic1(font.hlwd[0],32,0,0)
display.pic(font.hlwd[2],32,64,0)
display.show()












