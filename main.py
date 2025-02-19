color = input("enter your favorite color:")
favorite_color = color.split(", ")
print("your favorite color are:", favorite_color)
age = int(input("edad nimo madi:"))
is_adult = age >=18 
print("congrats!tigulungs naka!:",is_adult)
#insert
color = input("add another color:")
color=["pink","green","yellow"]
color1=["itom"]
color.insert(1,"itom")
print(color)
#erase
color = input("remove a color:")
color=["pink","itom","green","yellow"]
color1=["pink","green"]
color.remove("pink")
print(color)
#append
place= input("asa ka karon:")
place=["tayo ay nasa bootcamp","robinson","gaisano"]
place1=["NO!!!tayo ay nasa fine dining restaurant"]
place.append("NO!!!tayo ay nasa fine dining restaurant")
print(place1)