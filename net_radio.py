#!/usr/bin/env python3
from datetime import datetime
from datetime import date


from time import sleep
import RPi.GPIO as GPIO
import keyboard
import os
from rpi_lcd import LCD

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN,pull_up_down=GPIO.PUD_UP)
lcd = LCD()
today = date.today()
lcd.clear()

lcd.text("Radio Power On,", 1)
sleep(1)
lcd.clear()
lcd.text("Developed by :", 1)
lcd.text("Bineesh Kumar", 2)
sleep(2)
#lcd.text("",2)

#URI = 'https://air.pc.cdn.bitgravity.com/air/live/pbaudio101/chunklist.m3u8 --timeout 60'
#player = omxplayer -o local (URI)
#player.play()

#os.system('omxplayer -o local  https://air.pc.cdn.bitgravity.com/air/live/pbaudio101/chunklist.m3u8 --timeout 60 &')
#sleep(60)
lcd.clear()
lcd.text("BBC Radio", 1)
os.system('sudo omxplayer -o local  http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/nonuk/sbr_low/ak/bbc_world_service.m3u8 --timeout 60 &')
#while True:

 #current_time = now.strftime("%H:%M:%S")
 #print("Current Time =", current_time)
 #lcd.text(current_time, 2)

ch=1
och=0


while True:
  if GPIO.input(7)==0:
   if ch<8:
     ch=ch+1

  #sleep(0.25)

  if GPIO.input(7)==0:
   if ch>7:
    ch=1

  #sleep(0.50)

  print(ch)
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  d4 = today.strftime("%b-%d-%Y")
  lcd.text(current_time, 2)
  #sleep(0.50)
  #lcd.text(d4, 2)

			
  if ch == 1:
      if och != ch:
        os.system('sudo pkill omxplayer ')
        #os.system('sudo omxplayer -o local  https://air.pc.cdn.bitgravity.com/air/live/pbaudio036/chunklist.m3u8 --timeout 60 &')
        #sleep(0.25)
        os.system('sudo omxplayer -o local  http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/nonuk/sbr_low/ak/bbc_world_service.m3u8 --timeout 60 &')
        print("Channel: BBC UK")
        lcd.clear()
        sleep(0.10)
        lcd.text("BBC UK", 1)
        och = 1


  if ch == 2:
      if och != ch:
        os.system('sudo pkill omxplayer ')
        #sleep(0.25)
        os.system('sudo omxplayer -o local  https://air.pc.cdn.bitgravity.com/air/live/pbaudio036/chunklist.m3u8 --timeout 60 &')
        och = 2
        sleep(0.10)
        lcd.clear()
        print("Channel: Thrissur")
        lcd.text("AIR Thrissur", 1)

  if ch == 3:
      if och != ch:
        os.system('sudo pkill omxplayer ')
        #sleep(0.25)
        os.system('sudo omxplayer -o local  http://air.pc.cdn.bitgravity.com/air/live/pbaudio005/playlist.m3u8 --timeout 60 &')
        och = 3
        lcd.clear()
        sleep(0.10)
        print("Channel: FM GOLD")
        lcd.text("FM GOLD", 1)

  if ch == 4:
      if och != ch:
        os.system('sudo pkill omxplayer ')
        #sleep(0.25)
        os.system('sudo omxplayer -o local  http://air.pc.cdn.bitgravity.com/air/live/pbaudio004/playlist.m3u8 --timeout 60 &')
        och = 4
        lcd.clear()
        sleep(0.10)
        print("Channel: FM Rainbow")
        lcd.text("FM Rainbow", 1)

  if ch == 5:
      if och != ch:
        os.system('sudo pkill omxplayer ')
        #sleep(0.25)
        os.system('sudo omxplayer -o local  https://air.pc.cdn.bitgravity.com/air/live/pbaudio189/chunklist.m3u8 --timeout 60 &')
        och = 5
        sleep(0.10)
        lcd.clear()
        lcd.text("FM Kavarathi", 1)

  if ch == 6:
      if och != ch:
        os.system('sudo pkill omxplayer ')
        #sleep(0.25)
        os.system('sudo omxplayer -o local  https://air.pc.cdn.bitgravity.com/air/live/pbaudio045/chunklist.m3u8 --timeout 60 &')

        och = 6
        sleep(0.10)
        lcd.clear()
        print("Channel: Kochi")
        lcd.text("AIR Kochi", 1)

  if ch == 7:
      if och != ch:
        os.system('sudo pkill omxplayer ')
        #sleep(0.25)
        os.system('sudo omxplayer -o local  https://air.pc.cdn.bitgravity.com/air/live/pbaudio101/chunklist.m3u8 --timeout 60 &')

        och = 7
        sleep(0.10)
        lcd.clear()
        print("Channel: Manjeri")
        lcd.text("AIR Manjeri", 1)

  if ch == 8:
      if och != ch:
        os.system('sudo pkill omxplayer ')
        #sleep(0.25)
        os.system('sudo omxplayer -o local  https://air.pc.cdn.bitgravity.com/air/live/pbaudio89/chunklist.m3u8 --timeout 60 &')
        lcd.text("Unknown Channel", 1)
        och = 8
        sleep(0.10)
        lcd.clear()
        print("Channel: Unknown Channel")