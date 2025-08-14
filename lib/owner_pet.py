class Pet:
     PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
     all = []

     def __init__(self, name, pet_type, owner=None):
        self.name = name

        # Validate pet type
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.pet_type = pet_type

        # Optional owner check (only if passed)
        if owner is not None and not hasattr(owner, "pets"):
            raise Exception("Owner must be an instance of Owner")
        self.owner = owner

        Pet.all.append(self)

        pass

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # Return all pets owned by this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Must be a Pet instance")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

    pass