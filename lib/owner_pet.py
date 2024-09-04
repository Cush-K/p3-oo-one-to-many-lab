class Pet:
    
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = None
        self.owner = None
        
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception("Pet Type Error: Pet must be in the Pet List")
        
        if owner is not None:
            self.set_owner(owner)
            
        Pet.all.append(self)
                
    def set_owner(self, owner):
        if isinstance(owner, Owner):
            self.owner = owner
        else:
            raise Exception("Owner must be an instance of the Owner class.")
      
class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance (pet, Pet):
            pet.set_owner(self)
        else:
            raise Exception("pet must be an instance of the Pet class.")

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    
        

owner = Owner("Jojo")
cat = Pet("Kitty","cat")

owner.add_pet(cat)

print(cat.name)
print(cat.owner.name)