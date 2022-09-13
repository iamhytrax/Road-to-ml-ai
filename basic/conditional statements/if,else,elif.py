




text = """hello i am you bot assistant what would you want me to do.
        if you want me to check for a word is in a bellow passage click 1 
        if u want me to do find area of a rectangle press 2
        if you want me to find a vloume of a cube press 3
"""
print(text)
a = int(input())
if int(a) == 1 :                                                         #if
    print(" wait for a moment"); print("enter the word")      #while using a if statement we can use ; to use print multiple times in a single line
    x = input()
    if x in text:
        print("yes we found the text", x ,"in the following paragraph")

elif int(a) == 2:                                                          #elif
    print("enter 2 values")
    def area_of_a_rectangle():
        l = int(input())
        b = int(input())
        area = b*l
        print(area)
    area_of_a_rectangle()


elif int(a) == 3:
    print("ther the value to find the volume of a cube")
    def volume_of_cube():
         z= int(input())
         volume = z**3
         print(volume)
    volume_of_cube()


else :                                                                      #else
    print("enter a valid number")                               
