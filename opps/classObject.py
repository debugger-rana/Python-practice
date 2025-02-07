class rana:
    def character(self):
        gender:"male"
        age:23
        print("rana")

r1=rana()
r2=rana()
# calling the object's methode with the help of class and passing the object as argument
rana.character(r1)
rana.character(r2)
print()
# calling the object's methode direclty from the oject itself 
r1.character()
r2.character()
    