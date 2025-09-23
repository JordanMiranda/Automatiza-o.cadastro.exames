import pyautogui as pa
import time
import ctypes

pa.PAUSE = 0.01


pa.write("155")
for i in range (1,10):
    pa.press('enter')


pa.write("5147")
for i in range (1,10):
    pa.press('enter')

pa.write("108")
for i in range (1,10):
    pa.press('enter')


pa.write("40")
for i in range (1,10):
    pa.press('enter')

pa.write("8987")
for i in range (1,10):
    pa.press('enter')


pa.write("8979")
for i in range (1,10):
    pa.press('enter')
    

pa.write("8978")
for i in range (1,10):
    pa.press('enter')
    


pa.write("8992")
for i in range (1,10):
    pa.press('enter')
    

pa.write("8991")
for i in range (1,10):
    pa.press('enter')
    

pa.write("8966")
for i in range (1,10):
    pa.press('enter')

pa.write("8982")
for i in range (1,10):
    pa.press('enter')


pa.write("9100")
for i in range (1,9):
    pa.press('enter')


libc = ctypes.CDLL("libc.so.6")
    libc.malloc_trim(0)
