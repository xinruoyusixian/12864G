








# main.py -- put your code herfr
from LCD_12864G import LCD_12864G
import time,framebuf,_lib,font,ujson
from machine import Pin 
from urequests import get
display=LCD_12864G()
draw=display.draw


def get_weather():
  try:
        data =  ujson.loads(get("http://www.tianqiapi.com/free/day?appid=75982964&appsecret=XtOL4MxG").text)
        print("Weather Update")
        return data
  except:
    print("geng xin shi bai !")
def get_string(s):
      #在指定位置写入8*8的文字 会自动向后显示文字
      w=len(s)*8
      h=8
      buffer0= bytearray(((h // 8) * w) + 1)
      buffer0[0] = 0x40  
      fbuf = framebuf.FrameBuffer(memoryview(buffer0)[1:], w, h, framebuf.MONO_VLSB)
      fbuf.text(s, 0, 0, 0xffff)
      return  buffer0  

def num(numbers,zimo,width=8,x=0,y=1):
  length=len(numbers)
  for a in range(0,length):
    if numbers[a]==':':
      index=10

    elif numbers[a]=='-':
      index=11

    elif numbers[a]=='/':
      index=12
  
    else:
      #print(numbers[a])
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
    i=1
    while 1:
      if i==300:
        _lib.update_time()
        i=1
      i+=1
      for a in range(0,100):
        _t=time.localtime()
        s=str("%02d" % _t[3])+str(":%02d" % _t[4])+str(":%02d" % _t[5])  
        time.sleep_ms(t)
        draw(font.icon8x8['arrow'],8,a,2)
        draw(font.xq[0],16,0,3)
        draw(font.xq[1],16,16,3)
        draw(font.wk[_t[6]],16,32,3)
        num(str("%02d" % _t[0])+str("-%02d" % _t[1])+str(":%02d" % _t[2])  ,font.num8x8,8,50,3)
        num(s,font.num16x32,16,0,5) 
@timed_function
def pic():
  display.pic(font.hlwd[0],32,0,32)

pic()
_lib.update_time()
loop()


def fbuf():
  while 1:
    
    display.fill_rect(0,0,64,8,0)
    time.sleep_ms(10)
    draw(font.icon8x8['arrow'],8,0,3)
    _t=time.localtime()
    s=str("%02d" % _t[3])+str(":%02d" % _t[4])+str(":%02d" % _t[5])
    display.text(s)
    display.fill_rect(10,10,82,8,0)
    display.text(str(time.ticks_us()),10,10)
    display.show()
