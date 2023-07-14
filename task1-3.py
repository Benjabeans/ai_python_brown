import numpy as np


while(input("Run \"r\", or Terminate \"t\": ")=="r"):print(len(str(input("enter word: ")))) if str(input("\"t\" for time conversion, \"w\" for wordlen: ")== "w") else (print(str(float(input("enter min: "))/60)+"hrs" if input("enter \"h\" for hr-> min, \"m\" for min -> hr: ")=="h" else str(float(input("enter hr: "))*60)+"mins"))