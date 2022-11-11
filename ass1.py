import os
import time

while True:
 for i in range(0,5):
  print("      ",end="")
  for j in range(0,i+1):
   print("*",end="")
  print("\r")
 for j in range(0,13):
  print("*",end="")
 print("\r")
 for i in range(0,5):
  print("      ",end="")
  for j in range(0,5-i):
   print("*",end="")
  print("\r")
 
 time.sleep(1)  
 os.system('cls')
 
 for i in range(0,6):
  print("     *")
 for i in range(0,6):
  for j in range(0,i):
   print(" ",end="")
  for j in range(0,11-2*i):
   print("*",end="")
  print("\r")
 for i in range(0,1):
  print("     *")
 time.sleep(1)  
 os.system('cls')
 
 
 for i in range(0,5):
  for j in range(0,7-i):
   print(" ",end="")
  for j in range(0,i+1):
   print("*",end="")
  print("\r")
 for i in range(0,16):
  print("*",end="")
 print("\r")
 for i in range(0,5):
  for j in range(0,i+3):
   print(" ",end="")
  for j in range(0,5-i):
   print("*",end="")
  print("\r")
 time.sleep(1)  
 os.system('cls')
 
 
 
 for i in range(0,2):
  print("     *")
 for i in range(0,5):
  for j in range(0,4-i):
   print(" ",end="")
  for j in range(0,3+(i*2)):
   print("*",end="")
  print("\r")
 for i in range (0,6):
  print("     *")
 time.sleep(1)  
 os.system('cls')
  
   
  