import pyautogui as py
import time as ti

a=True
while a == True:
  print ("1. Discord")
  print ("2. Valorant")
  print ("3. Mineraft")
  print ("4. Curse Forge")
  print ("5. Osu")
  print ("6. Epic games")
  print ("7. Steam")
  print ("8. Davinci Resolve")
  print ("9. Medal")
  print ("10. Visual studio Code")
  print ("11. Razer Synapse")
  print ("12.Google")
  User_input=input()
  if User_input == '1':
   py.press ('win')
   py.write ('Discord')
   ti.sleep (1)
   py.press ('enter')
  elif User_input == '2':
    py.press ('win')
    py.write ('Valorant')
    ti.sleep (1)
    py.press ('enter')
  elif User_input == '3':
    py.press ('win')
    py.write ('Lunar Client')
    ti.sleep (1)
    py.press ('enter')
    ti.sleep (3)
    py.moveTo (x=1307, y=561)
    py.click ()
  elif User_input == '4':
    py.press ('win')
    py.write ('curse forge')
    py.sleep (1)
    py.press ('enter')
  elif User_input == '5':
    py.press ('win')
    py.write ('osu')
    ti.sleep (1)
    py.press ('enter')
  elif User_input == '6':
    py.press ('win')
    py.write ('Epic Games')
    ti.sleep (1)
    py.press ('enter')
  elif User_input == '7':
    py.press ('win')
    py.write ('Steam')
    ti.sleep (1)
    py.press ('enter')
  elif User_input == '8':
    py.press ('win')
    py.write ('Davinci Resolve')
    ti.sleep (1)
    py.press ('enter')
  elif User_input == '9':
    py.press ('win')
    py.write ('medal')
    ti.sleep (1)
    py.press ('enter')
  elif User_input == '10':
    py.press ('win')
    py.write ('Visual Studio Code')
    ti.sleep (1)
    py.press ('enter')
  elif User_input == '11':
    py.press ('win')
    py.write ('Razer Synapse')
    ti.sleep (1)
    py.press ('enter')
  elif User_input == '12':
    import google 
  elif User_input == 'Meli':
    break