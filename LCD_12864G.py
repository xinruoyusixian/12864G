








import machine,_lib,gc
from machine import Pin
import framebuf,time,micropython





def get_string(s):

      #在指定位置写入8*8的文字 会自动向后显示文字

      #绘画时宽度应为8x字符跟个数

      l=len(s)

      w=l*8
      h=8
      buffer0= bytearray(((h // 8) * w) )
      fbuf = framebuf.FrameBuffer(memoryview(buffer0), w, h, framebuf.MONO_VLSB)
      fbuf.text(s, 0, 0, 0xffff)
      return  (buffer0,l)  
      
class _framebuf:
    def __init__(self,width=128,height=64):
        self.width=width
        self.height=height
        self.buffer =  bytearray(((height // 8) * width) )
        self._framebuf = framebuf.FrameBuffer1(memoryview(self.buffer), width, height)   
        self.hline = self._framebuf.hline         # 横线     hline(x,y,长度,是否填充[0 or 1])
        self.vline = self._framebuf.vline         # 竖线     hline(x,y,长度,是否填充[0 or 1])
        self.line = self._framebuf.line           # 线段     line(x1,y1,x2,y2,是否填充[0 or 1])
        self.rect = self._framebuf.rect           # 矩形     rect(x1,y1,x2,y2,是否填充[0 or 1])
        self.fill_rect = self._framebuf.fill_rect # 填充矩形  rect(x1,y1,x2,y2,是否填充[0 or 1])
        self.blit = self._framebuf.blit           # 绘制另外一个帧缓冲区 blit(fbuf, x, y[, key])
        self.scroll=self._framebuf.scroll        # 滚动画面  scroll(dx, dy)
        self.fill=self._framebuf.fill             # 全屏填充  fill( col 是否填充[0 or 1])
    def text(self,str,x=0,y=0):                   # 英文文字输入
        self._framebuf.text(str, x, y, 1)   
 
    def pixel(self, x, y, col=1):                 #像素填充
        self._framebuf.pixel(x, y, col)
    def show(self):                               #显示到屏幕
        self.draw(self.buffer,128,1,1)




    @micropython.native  
    def pic(self,arr,width,x=0,y=0):             #显示字符画或者汉字
        x1=x
        _len=len(arr)
        #bit=[0,1,2,3,4,5,6,7,8]  #减少range次数 提高性能
        a_times=range(0,_len) #减少range次数 提高性能
        for a in a_times:
               if arr[a]!=0:
                  #p=str("%08d" %  int(bin(arr[a]).replace('0b','')) ) #16进制转二进制方法

                  p=bin(arr[a]).replace('0b','')   #16进制转二进制方法
                  while len(p)<8:
                      p='0'+p

                  #for b in bit:
                  #   self.pixel(x1,y+b,int(p[7-b])) #倒排输出像素点到屏幕
                  self.pixel(x1,y+0,int(p[7]))
                  self.pixel(x1,y+1,int(p[6]))
                  self.pixel(x1,y+2,int(p[5]))
                  self.pixel(x1,y+3,int(p[4]))
                  self.pixel(x1,y+4,int(p[3]))
                  self.pixel(x1,y+5,int(p[2]))
                  self.pixel(x1,y+6,int(p[1]))
                  self.pixel(x1,y+7,int(p[0]))                    
               x1+=1
               if a % 32==0 and a !=0 :
                   y+=8
                   x1=x
                   
"""
    @micropython.native
    def pic(self,arr,width,x=0,y=0):  #字符画方法2
          l=range(0,len(arr)//width)
          i=0
          #bit=[0,1,2,3,4,5,6,7,8] 
          x1_range=range(0,width)
          for b in l: 
              yb=b*8
              for x1 in x1_range:
                if arr[i] != 0 :
                      p=bin(arr[i]).replace('0b','')
                      x2=x+x1
                      while len(p)<8:
                          p='0'+p
                      #for a in bit:  #丢掉for 节省100ms 时间
                      #   self.pixel(x1+x,a+b*8,int(p[7-a]))
                      self.pixel(x2,yb+0,int(p[7]))
                      self.pixel(x2,yb+1,int(p[6]))
                      self.pixel(x2,yb+2,int(p[5]))

                      self.pixel(x2,yb+3,int(p[4]))
                      self.pixel(x2,yb+4,int(p[3]))
                      self.pixel(x2,yb+5,int(p[2]))
                      self.pixel(x2,yb+6,int(p[1]))
                      self.pixel(x2,yb+7,int(p[0]))                         
                             
                i+=1 
                
"""
                
class LCD_12864G(_framebuf):
    def __init__(self,spi,cs=4,reset=5,rs=16):
      #引脚定义
      self.cs=Pin(cs)   #片选 保持高电平即可 
      self.reset=Pin(reset)  #复位
      self.rs=Pin(rs)    #数据/指令 1数据 0 指令  #DC
      self.sda=Pin(13)  #数据信号
      self.sck=Pin(14)    #时钟信号
      self.spi = spi #硬件实现
      self.rate = 20 * 1024 * 1024
      self.rs.init(self.rs.OUT, value=0)
      self.reset.init(self.reset.OUT, value=0)
      self.cs.init(self.cs.OUT, value=1)  
      self.reset.off()# /*低电平复位*/
      time.sleep_us(100)#
      self.reset.on()# /*复位完毕*/
      time.sleep_us(100)#
      self.write_cmd(0xe2)# /*软复位*/
      time.sleep_us(5)#
      self.write_cmd(0x2c)# /*升压步聚 1*/
      time.sleep_us(5)#
      self.write_cmd(0x2e)# /*升压步聚 2*/
      time.sleep_us(5)#
      self.write_cmd(0x2f)# /*升压步聚 3*/
      time.sleep_us(5)#
      self.write_cmd(0x27)# /*粗调对比度，可设置范围 0x20～0x27*/
      self.write_cmd(0x81)# /*微调对比度*/
      self.write_cmd(0x2a)# /*0x1a,微调对比度的值，可设置范围 0x00～0x3f*/
      self.write_cmd(0xa2)# /*1/9 偏压比（bias）*/
      self.write_cmd(0xc8)# /*行扫描顺序：从上到下*/
      self.write_cmd(0xa0)# /*列扫描顺序：从左到右*/
      self.write_cmd(0x40)# /*起始行：第一行开始*/
      self.write_cmd(0xaf)# /*开显示*/ 
      time.sleep(1)
      for a in range(1,3):
        time.sleep_ms(100)
        self.write_cmd(0x27-a)
      self.write_cmd(0xA7) #反显
      self.write_cmd(0x24)
      self.clear_screen()
      super().__init__()

      #0xA0：常规 列地址从左到右，
      #0xA1：反转：列地址从右到左
      #0xA6：常规：正显
      #0xA7：反显 
      #0xA4：常规 显示全部点阵
      #0xA5：显示全部点阵 
      #0XE2 :软件复位。
      #0XC0:普通扫描顺序：从上到下
      #0XC8:反转扫描顺序：从下到上
      #0x20～0x27，粗调 数值越大对比度越浓，越小越淡
      #0x00～0x3F,微调 值越大对比 度越浓，越小越淡
      #0xAC: 关, 0xAD: 开。静态图标的开关设置
 
    #/*全屏清屏*/
    def clear_screen(self):
      for i  in range (1,9):
             self.lcd_address(0,i)
             self.write_data(129)

   
    def write_cmd(self,cmd):
            self.spi.init(baudrate=self.rate, polarity=0, phase=0)
            self.cs.off()
            self.rs.off()
            self.spi.write(bytearray([cmd]))
            
    def write_data(self,cmd):
            self.spi.init(baudrate=self.rate, polarity=0, phase=0)
            self.cs.off()
            self.rs.on()
            self.spi.write(bytearray(cmd))



    def  lcd_address(self,column,page):
           #print(column,page)
           column=column-1; #我们平常所说的第 1 列，在 LCD 驱动 IC 里是第 0 列。所以在这里减去 1.
           page=page-1
           self.write_cmd(0xb0+page); #设置页地址。每页是 8 行。一个画面的 64 行被分成 8 个页。我们平常所说的第 1 页，在 LCD驱动 IC 里是第 0 页，所以在这里减去 1*/
           self.write_cmd(((column>>4)&0x0f)+0x10) #设置列地址的高 4 位
           self.write_cmd(column&0x0f) #设置列地址的低 4 位


#/*显示点阵图像、汉字、生僻字或 32x32 点阵的其他图标*/
      #arr :  16进制数组 0xff
      #width: 字符画宽度
      #x:     x坐标
      #column:行 一行8个像素所以64像素就是8行

    def draw(self,arr,width,x=0,column=1):
      index=0
      l=range(0,int(len(arr)/width))
      for a in l:
        self.lcd_address(x,column)
        column+=1
        self.write_data(arr[index:index+width])
        index+=width
        self.lcd_address(x,column)
        column+=1
        self.write_data(arr[index:index+width])
        index+=width

        



    def flip(self,arr,w):  #图片字体 翻转180度

        tmp=[]

        tmp2=[]

        r=range(0,len(arr)//w)

        for i   in r:

            x=i*w

            tmp.append(arr[i*w:x+w])
        r=range (0,len(tmp))
        for j in r:
            tmp[j]=tmp[j][::-1]
            print(tmp[j])
            tmp2+=tmp[j]
        return tmp2

    def get_string(self,s):
        #"在指定位置写入8像素高的文字,\r绘画时 时宽度应为8x字符个数"
        w=len(s)*8
        h=8
        buffer0= bytearray(((h // 8) * w) )
        fbuf = framebuf.FrameBuffer(memoryview(buffer0), w, h, framebuf.MONO_VLSB)
        fbuf.text(s, 0, 0, 0xffff)
        return  (buffer0,w)        










