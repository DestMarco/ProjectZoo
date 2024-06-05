"""Marco De Stefano"""
import unittest
from unittest import TestCase
from src.zoo import  ZooKeeper, Animal, Fence, Zoo

class TestZoo(TestCase):
    def setUp(self):
        
        self.zooKeeper_1 = ZooKeeper(name="Gianni", surname="Rossi", id="1")
        self.fence_1 = Fence(area=100, temperature=25.0, habitat="Savannah")
        self.animal_1 = Animal(name="Pluto", species="Canide", age=5, height=10.0, width=5.0, preferred_habitat="Savannah")
        self.animal_2 = Animal(name="Mickey", species="Mouse", age=2, height=2.0, width=1.0, preferred_habitat="Savannah")
        self.animal_3 = Animal(name="Penguin", species="Spheniscidae", age=2, height=0.4, width=0.5, preferred_habitat="Polar")
        self.fence_2 = Fence(area=50.0, temperature=-5.0, habitat="Polar")
    
    def test_add_animal(self):
        self.zooKeeper_1.add_animal(self.animal_1, self.fence_1)
        result = len(self.fence_1.animals)
        message = "Errore: the function add_animal should add animal_1 into fence_1"
        self.assertEqual(result, 1, message)
        
        self.zooKeeper_1.add_animal(self.animal_1, self.fence_2)
        result = len(self.fence_2.animals)
        message = "Errore: the function add_animal should not add animal_1 into fence_2"
        self.assertEqual(result, 0, message)
    
    def test_add_multiple_animals(self):
        self.zooKeeper_1.add_animal(self.animal_1, self.fence_1)
        self.zooKeeper_1.add_animal(self.animal_2, self.fence_1)
        result = len(self.fence_1.animals)
        message = "Errore: the function add_animal should add both animal_1 and animal_2 into fence_1"
        self.assertEqual(result, 2, message)
    
    def test_add_animal_to_full_fence(self):
        small_fence = Fence(area=1.0, temperature=25.0, habitat="Savannah")
        self.zooKeeper_1.add_animal(self.animal_1, small_fence)
        result = len(small_fence.animals)
        message = "Errore: the function add_animal should not add animal_1 into a full fence"
        self.assertEqual(result, 0, message)

    def test_remove_animal(self):
        self.zooKeeper_1.add_animal(self.animal_1, self.fence_1)
        self.zooKeeper_1.remove_animal(self.animal_1, self.fence_1)
        result = len(self.fence_1.animals)
        message = "Errore: the function remove_animal should remove animal_1 from fence_1"
        self.assertEqual(result, 0, message)
    
    def test_remove_non_existent_animal(self):
        self.zooKeeper_1.remove_animal(self.animal_1, self.fence_1)
        result = len(self.fence_1.animals)
        message = "Errore: the function remove_animal should not alter fence_1 when animal_1 is not in it"
        self.assertEqual(result, 0, message)
    
    def test_feed(self):
        self.zooKeeper_1.add_animal(self.animal_1, self.fence_1)
        self.zooKeeper_1.feed(self.animal_1)
        self.assertAlmostEqual(self.animal_1.height, 10.0 * 1.02, places=2, msg="Errore: height should increase by 2%")
        self.assertAlmostEqual(self.animal_1.width, 5.0 * 1.02, places=2, msg="Errore: width should increase by 2%")
        self.assertAlmostEqual(self.animal_1.health, 100 * (1 / 5) * 1.01, places=2, msg="Errore: health should increase by 1%")
    
    
    def test_feed_insufficient_area(self):
        self.zooKeeper_1.add_animal(self.animal_1, self.fence_1)
        self.fence_1.area = 0  
        self.zooKeeper_1.feed(self.animal_1)
        
        self.assertAlmostEqual(self.animal_1.height, 10.0, places=2, msg="Errore: height should not increase when area is insufficient")
        self.assertAlmostEqual(self.animal_1.width, 5.0, places=2, msg="Errore: width should not increase when area is insufficient")
        self.assertAlmostEqual(self.animal_1.health, 100 * (1 / 5), places=2, msg="Errore: health should not increase when area is insufficient")
    

    def test_clean(self):
        self.zooKeeper_1.add_animal(self.animal_1, self.fence_1)
        self.zooKeeper_1.add_animal(self.animal_2, self.fence_1)
        area_occupied = self.zooKeeper_1.clean(self.fence_1)
        expected_area_occupied = (self.animal_1.height * self.animal_1.width) + (self.animal_2.height * self.animal_2.width)
        self.assertAlmostEqual(area_occupied, expected_area_occupied / (self.fence_1.area + expected_area_occupied), places=2, msg="Errore: cleaning occupancy rate is incorrect")

# Run the tests
if __name__ == '__main__':
    unittest.main()