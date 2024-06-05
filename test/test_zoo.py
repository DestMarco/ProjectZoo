import unittest
from unittest import TestCase
from src.zoo import  ZooKeeper, Animal, Fence, Zoo

class TestZoo(TestCase):
    def test_animal(self):
        zooKeeper_1:ZooKeeper=ZooKeeper(name="Gianni",surname="Rossi",id=1)
        fence_1:Fence=Fence(area=100, temperature=25.0, habitat="sea")
        animal_1:Animal=Animal(name="Pluto", species="Canide", age=5, height=300.0, width=1.0,preferred_habitat="savana")
        zooKeeper_1.dd_animal(animal_1,fence_1)
        result:int=len(fence_1.animals)
        message:str=f"Errore: the fuction add_animal should not add self.animal_1 into self.fence_1 "
        self.assertEqual(result, 0, message)

