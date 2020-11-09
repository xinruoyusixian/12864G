



#【0123456789:】8*16
num8x8=[[0x00,0xE0,0x10,0x08,0x08,0x10,0xE0,0x00,0x00,0x0F,0x10,0x20,0x20,0x10,0x0F,0x00],
[0x00,0x10,0x10,0xF8,0x00,0x00,0x00,0x00,0x00,0x20,0x20,0x3F,0x20,0x20,0x00,0x00],
[0x00,0x70,0x08,0x08,0x08,0x88,0x70,0x00,0x00,0x30,0x28,0x24,0x22,0x21,0x30,0x00],
[0x00,0x30,0x08,0x88,0x88,0x48,0x30,0x00,0x00,0x18,0x20,0x20,0x20,0x11,0x0E,0x00],
[0x00,0x00,0xC0,0x20,0x10,0xF8,0x00,0x00,0x00,0x07,0x04,0x24,0x24,0x3F,0x24,0x00],
[0x00,0xF8,0x08,0x88,0x88,0x08,0x08,0x00,0x00,0x19,0x21,0x20,0x20,0x11,0x0E,0x00],
[0x00,0xE0,0x10,0x88,0x88,0x18,0x00,0x00,0x00,0x0F,0x11,0x20,0x20,0x11,0x0E,0x00],
[0x00,0x38,0x08,0x08,0xC8,0x38,0x08,0x00,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x00],
[0x00,0x70,0x88,0x08,0x08,0x88,0x70,0x00,0x00,0x1C,0x22,0x21,0x21,0x22,0x1C,0x00],
[0x00,0xE0,0x10,0x08,0x08,0x10,0xE0,0x00,0x00,0x00,0x31,0x22,0x22,0x11,0x0F,0x00],
[0x00,0x00,0x00,0xC0,0xC0,0x00,0x00,0x00,0x00,0x00,0x00,0x30,0x30,0x00,0x00,0x00],]
#【0123456789:】8*16
num16x32=[
[0x00,0x00,0x00,0x00,0x00,0x80,0xC0,0x40,0x40,0x40,0x80,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xF0,0xFE,0x0F,0x01,0x00,0x00,0x00,0x00,0x01,0x07,0xFE,0xF0,0x00,0x00,0x00,0x00,0x3F,0xFF,0xC0,0x00,0x00,0x00,0x00,0x00,0x00,0x80,0xFF,0x3F,0x00,0x00,0x00,0x00,0x00,0x01,0x03,0x06,0x0C,0x08,0x08,0x08,0x06,0x03,0x01,0x00,0x00,0x00],#"0",0
[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x80,0xC0,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x01,0x01,0x01,0x01,0xFF,0xFF,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xFF,0xFF,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x08,0x08,0x08,0x0C,0x0F,0x0F,0x0C,0x08,0x08,0x08,0x00,0x00,0x00],#"1",1
[0x00,0x00,0x00,0x00,0x80,0x40,0x40,0x40,0x40,0x40,0xC0,0x80,0x80,0x00,0x00,0x00,0x00,0x00,0x1E,0x19,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xC1,0xFF,0x3E,0x00,0x00,0x00,0x00,0x00,0x00,0x80,0x40,0x30,0x18,0x0C,0x06,0x03,0x01,0x00,0xC0,0x00,0x00,0x00,0x00,0x0E,0x0D,0x0C,0x0C,0x0C,0x0C,0x0C,0x0C,0x0C,0x0C,0x0E,0x03,0x00,0x00],#"2",2
[0x00,0x00,0x00,0x80,0x80,0x40,0x40,0x40,0x40,0xC0,0x80,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x0F,0x0F,0x00,0x00,0x00,0x00,0x00,0x80,0xC1,0x7F,0x3E,0x00,0x00,0x00,0x00,0x00,0xC0,0xC0,0x00,0x00,0x01,0x01,0x01,0x03,0x02,0x06,0xFC,0xF0,0x00,0x00,0x00,0x00,0x03,0x07,0x04,0x08,0x08,0x08,0x08,0x08,0x04,0x06,0x03,0x00,0x00,0x00],#"3",3
[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xC0,0xC0,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x80,0x60,0x10,0x0C,0x03,0xFF,0xFF,0x00,0x00,0x00,0x00,0x00,0x00,0x30,0x2C,0x26,0x21,0x20,0x20,0x20,0x20,0xFF,0xFF,0x20,0x20,0x20,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x08,0x08,0x08,0x0F,0x0F,0x08,0x08,0x08,0x00,0x00],#"4",4
[0x00,0x00,0x00,0x00,0xC0,0xC0,0xC0,0xC0,0xC0,0xC0,0xC0,0xC0,0xC0,0xC0,0x00,0x00,0x00,0x00,0x00,0xFF,0x00,0x80,0x40,0x40,0x40,0x40,0xC0,0x80,0x00,0x00,0x00,0x00,0x00,0x00,0xC0,0xC3,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x01,0xFF,0xFC,0x00,0x00,0x00,0x00,0x03,0x04,0x04,0x08,0x08,0x08,0x08,0x08,0x04,0x07,0x03,0x00,0x00,0x00],#"5",5
[0x00,0x00,0x00,0x00,0x00,0x80,0x80,0x40,0x40,0x40,0x40,0x80,0x80,0x00,0x00,0x00,0x00,0x00,0xE0,0xFC,0x07,0x81,0xC0,0x40,0x40,0x40,0xC0,0x83,0x03,0x00,0x00,0x00,0x00,0x00,0x7F,0xFF,0x83,0x00,0x00,0x00,0x00,0x00,0x00,0x01,0xFF,0xFC,0x00,0x00,0x00,0x00,0x00,0x01,0x07,0x06,0x0C,0x08,0x08,0x08,0x0C,0x06,0x03,0x00,0x00,0x00],#"6",6
[0x00,0x00,0x00,0xC0,0xC0,0xC0,0xC0,0xC0,0xC0,0xC0,0xC0,0xC0,0xC0,0xC0,0x00,0x00,0x00,0x00,0x0E,0x03,0x00,0x00,0x00,0x00,0x00,0xE0,0x18,0x06,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xC0,0xFC,0x03,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x0F,0x0F,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],#"7",7
[0x00,0x00,0x00,0x00,0x80,0xC0,0x40,0x40,0x40,0x40,0xC0,0x80,0x00,0x00,0x00,0x00,0x00,0x00,0x3E,0x7F,0xF1,0xC0,0xC0,0x80,0x00,0x00,0x80,0x41,0x7F,0x1E,0x00,0x00,0x00,0xF0,0xFC,0x0E,0x02,0x01,0x01,0x01,0x03,0x07,0x0E,0x1E,0xFC,0xF0,0x00,0x00,0x00,0x01,0x03,0x06,0x04,0x08,0x08,0x08,0x08,0x08,0x04,0x06,0x03,0x01,0x00,0x00],#"8",8
[0x00,0x00,0x00,0x80,0x80,0x40,0x40,0x40,0x40,0x40,0x80,0x00,0x00,0x00,0x00,0x00,0x00,0xFC,0xFF,0x03,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x03,0xFE,0xF8,0x00,0x00,0x00,0x01,0x03,0x07,0x0C,0x08,0x08,0x08,0x08,0x04,0x06,0xE1,0x7F,0x1F,0x00,0x00,0x00,0x00,0x07,0x07,0x08,0x08,0x08,0x08,0x0C,0x06,0x03,0x01,0x00,0x00,0x00,0x00],#"9",9
[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xC0,0xE0,0xE0,0xC0,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x01,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x06,0x0F,0x0F,0x06,0x00,0x00,0x00,0x00,0x00,0x00],#":",10
]

#哈罗沃德  32x32
hlwd=[
[0x00,0x00,0x00,0xC0,0x80,0x80,0x80,0x80,0x80,0x80,0xC0,0x80,0x00,0x00,0x00,0x00,0x00,0x80,0xF0,0x7C,0x38,0xC8,0x80,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xFF,0xFF,0x00,0x00,0x00,0x00,0xFF,0xFF,0x80,0x40,0x20,0x50,0x4C,0x46,0x43,0x40,0x40,0x40,0x40,0x41,0x66,0x6C,0x58,0x38,0x70,0x60,0x20,0x00,0x00,0x00,0x00,0x00,0xFF,0xFF,0x10,0x10,0x10,0x10,0x7F,0x7F,0x00,0x00,0x00,0xFC,0xF8,0x08,0x08,0x08,0x08,0x08,0x08,0x08,0x08,0xF8,0xF8,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x03,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x7F,0x3F,0x08,0x08,0x08,0x08,0x08,0x08,0x08,0x08,0x7F,0x3F,0x00,0x00,0x00,0x00,0x00,0x00],#"哈",0
[0x00,0x00,0x00,0x80,0x80,0x80,0x80,0x80,0x80,0xC0,0x80,0x00,0x00,0x00,0x00,0xE0,0xFC,0x58,0x48,0x40,0x40,0x40,0x40,0xC0,0xE0,0xC0,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xFF,0xFF,0x00,0x00,0x00,0x00,0xFF,0x00,0x20,0x10,0x0C,0x03,0x01,0x01,0x06,0x98,0xF0,0xF0,0xF8,0x9E,0x07,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xFF,0x7F,0x08,0x08,0x08,0x48,0x3F,0x30,0x10,0x10,0x08,0xFC,0xFC,0x16,0x13,0x11,0x10,0x10,0x11,0x11,0x13,0xFF,0xF6,0x0E,0x0E,0x04,0x04,0x04,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x7F,0x3F,0x08,0x08,0x08,0x08,0x08,0x08,0x08,0x08,0x3F,0x3F,0x00,0x00,0x00,0x00,0x00,0x00],#"咯",1
[0x00,0x00,0x00,0x00,0x08,0x10,0x70,0xE0,0x00,0x00,0x00,0x40,0x40,0x40,0x40,0x40,0x40,0x40,0xE0,0xE0,0x20,0x20,0x30,0x30,0x30,0x18,0x10,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x18,0x30,0xE0,0x40,0x00,0x00,0xE0,0x1C,0x43,0x40,0x40,0x40,0x40,0x40,0x40,0x40,0xFF,0xFF,0x40,0xC0,0x40,0x40,0x40,0x40,0x40,0x60,0x60,0x40,0x00,0x00,0x00,0x00,0x40,0x40,0xC0,0xE0,0xF8,0x0F,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xC0,0x7C,0x1F,0x01,0x00,0x07,0x38,0xE0,0x80,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x1C,0x3F,0x07,0x00,0x40,0x20,0x20,0x10,0x18,0x0C,0x06,0x03,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x01,0x07,0x0E,0x3C,0x38,0x30,0x10,0x00,0x00],#"沃",2
[0x00,0x00,0x00,0x00,0x00,0x80,0xE0,0x38,0x18,0x00,0x40,0x40,0x40,0x40,0x40,0x40,0x40,0x40,0xC0,0xFC,0x58,0x40,0x40,0x40,0x40,0x40,0x40,0x60,0x40,0x00,0x00,0x00,0x00,0x00,0x08,0x04,0x03,0x81,0xC0,0xF0,0x1E,0x0E,0x04,0x00,0xFE,0xFC,0x04,0x04,0x04,0xFC,0xFF,0x04,0x04,0xFC,0xFC,0x04,0x04,0x04,0xFE,0x04,0x00,0x00,0x00,0x00,0x00,0x00,0x18,0x0C,0x06,0x01,0xFF,0xFF,0x00,0x08,0x08,0x88,0x0F,0x0B,0x09,0xC9,0x09,0x09,0x29,0x69,0xC9,0x89,0x09,0x09,0x09,0x49,0x8B,0x8C,0x0C,0x08,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x7F,0x3F,0x00,0x18,0x1C,0x0F,0x00,0x00,0x00,0x3F,0x30,0x30,0x30,0x30,0x31,0x31,0x20,0x30,0x3F,0x10,0x00,0x01,0x07,0x02,0x00,0x00],#"德",3
]

