'''
Created on 2022/10/14

@author: t20cs050
'''
import random

hand = []
hand.append([0,"グー"])
hand.append([1,"チョキ"])
hand.append([2,"パー"])

a = random.choice(hand)
b = random.choice(hand)

if(a[0] == b[0]):
    print("Aの手："+a[1]+"v.s.Bの手:"+b[1]+"->引き分け")
      
elif(a[0] == 0 and b[0] == 1):
    print("Aの手："+a[1]+"v.s.Bの手："+b[1]+"-> Aの勝ち")
  
elif(a[0] == 1 and b[0] == 0):
    print("Aの手："+a[1]+"v.s.Bの手："+b[1]+"-> Bの勝ち")
  
elif(a[0] == 0 and b[0] == 2):
    print("Aの手："+a[1]+"v.s.Bの手："+b[1]+"-> Bの勝ち")
      
elif(a[0] == 2 and b[0] == 0):
    print("Aの手："+a[1]+"v.s.Bの手："+b[1]+"-> Aの勝ち")
      
elif(a[0] == 1 and b[0] == 2):
    print("Aの手："+a[1]+"v.s.Bの手："+b[1]+"-> Aの勝ち")
          
elif(a[0] == 2 and b[0] == 1):
    print("Aの手："+a[1]+"v.s.Bの手："+b[1]+"-> Bの勝ち")
