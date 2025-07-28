class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
ob1=parrot("Ramby",12)
ob2=parrot("Riggy",11)
print(f"The species of Ramby is {ob1.species}")
print(f"The species of Riggy is {ob1.species}")
print(f"{ob1.name} age is {ob1.age} old")
print(f"{ob2.name} age is {ob2.age} old")