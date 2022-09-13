
   # Condition case 1

raining = False
print("Let's go to the", 
        'beach' if not raining else 'library')

raining = True
print("Let's go to the",
         'beach' if not raining else 'library')


   # Condition case 2

age = 12
s = 'minor' if age <= 12 else 'adult'
print(s)

   # Condition case 3

print("yes " if ("lol" in ["lol ", " nope" , "lmao"]) else  "no")


 # we use "pass" to escape from indentation error
if True:
    pass
print('foo')