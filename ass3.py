state = True
while state: 
 mode = int(input("for seintific_mode-->1    for prog_mode-->2   for exit-->0"))
 if mode==1:
  num1 = int(input("int num1  ")) 
  num2 = int(input("int num2  ")) 
  operator =(input("int operator  ")) 
  seintific_mode={
      "+":num1+num2,
      "-":num1-num2,
      "*":num1*num2,
      }
  print(seintific_mode[operator])
 elif mode==2:
  num = int(input("int num  ")) 
  prog_mode={
    "bin":bin(num),
    "oct":oct(num),
    "hex":hex(num),
    }
  operator =(input("int operator  "))
  print(prog_mode[operator])
 elif mode==0:
  state=False
 else:
  print("rong input")