# polymorphism

print(len("Samsun Naher"))
print(len([10,20,5,3,4,9]))

def add (x, y=0):
    print(f"Sum = {x+y}")

add(2,3)
add(4)


class Bird:
  def intro(self):
    print("There are many types of birds.")
     
  def flight(self):
    print("Most of the birds can fly but some cannot.")
   
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")
     
# class ostrich(Bird):
#   def flight(self):
#     print("Ostriches cannot fly.")
     
obj_bird = Bird()
obj_spr = sparrow()
# obj_ost = ostrich()
 
obj_bird.intro()
obj_bird.flight()
print("")
obj_spr.intro()
obj_spr.flight()
 
# obj_ost.intro()
# obj_ost.flight()