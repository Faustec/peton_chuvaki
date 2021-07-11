def NewFunction(sm):
 a = sm % 10
 if a == 1 and sm != 11:
    print("Моя залупа ", sm, " сантиметр")
 elif a > 1 and a < 5 and sm < 20:
    print("Моя залупа ", sm, " сантиметра")
 else: 
    print("Моя залупа ", sm, " сантиметров")   
 
i = 1
while i < 90:
   NewFunction(i)
   i = i + 1