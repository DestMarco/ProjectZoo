"""


1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.

2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age, height, width, preferred_habitat,
 health che è uguale a round(100 * (1 / age), 3).

3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere uno o più animali.
 I recinti possono hanno gli attributi area, temperature e habitat.

4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. I guardiani dello zoo hanno un name, 
un surname, e un id. Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.

Funzionalità:

1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. 
L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, 
ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.

2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo.
 L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.

3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. 
Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, ma le dimensioni dell'animale (height e width)
 vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.

4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo.
 Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. Il tempo di pulizia
   è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata.

5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali. 

E.s.: Se abbiamo un guardiano chiamato Lorenzo Maggi con matricola 1234, e un recinto Fence(area=100, temperature=25, habitat=Continentale)
 con due animali Animal(name=Scoiattolo, species=Blabla, age=25, ...), Animal(name=Lupo, species=Lupus, age=14,...) 
 ci si aspetta di avere una rappresentazione testuale dello zoo come segue:

Guardians:

ZooKeeper(name=Lorenzo, surname=Maggi, id=1234)

Fences:

Fence(area=100, temperature=25, habitat=Continent)

with animals:

Animal(name=Scoiattolo, species=Blabla, age=25)

Animal(name=Lupo, species=Lupus, age=14)
#########################

Fra un recinto e l'altro mettete 30 volte il carattere #.
"""

class Animal:
    # Defines the values for the object of the Animal class
    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)
        self.fen = None

class Fence:
    # Defines the values for the object of the Fence class
    def __init__(self, area: float, temperature: float, habitat: str):
        self.animals = []
        self.area = area
        self.temperature = temperature
        self.habitat = habitat

class ZooKeeper:
    # Defines the values for the object of the ZooKeeper class
    def __init__(self, name: str, surname: str, id: str):
        self.name = name
        self.surname = surname
        self.id = id

    # Function that allows the zookeeper to add a new animal to the zoo
    def add_animal(self, animal: Animal, fence: Fence):
        req_area = animal.height * animal.width
        if animal.preferred_habitat == fence.habitat and fence.area >= req_area:
            fence.animals.append(animal)
            animal.fen = fence
            fence.area -= req_area

    # Function that allows the zookeeper to remove an animal from the zoo
    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.animals:
            fence.animals.remove(animal)
            fence.area += animal.height * animal.width
            animal.fen = None

    # Function that allows the zookeeper to feed all the animals in the zoo
    def feed(self, animal: Animal):
        # Check if there is enough space in the enclosure for the enlarged animal
        if  animal.fen.area  >= (animal.height * animal.width * 1.02):
            # Increase the animal's health by 1%

            animal.health *= 1.01
            # Increase the dimensions of the animal by 2%
            animal.height *= 1.02
            animal.width *= 1.02
            animal.fen.area -= (animal.height * animal.width)
    # Function that allows the zookeeper to clean all the enclosures in the zoo
    def clean(self, fence: Fence) -> float:
        area_oc = 0
        for animal in fence.animals:
            area_oc += animal.height * animal.width
        if fence.area == 0:
            return area_oc
        else:
            return area_oc / fence.area
        
class Zoo:
    # Defines the values for the object of the Zoo class
    def __init__(self, fences: list[Fence], zoo_keepers: list[ZooKeeper]) -> None:
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    # Function that describes the information about the zoo, animals, and zookeepers
    def describe_zoo(self):
        print("Guardians:")
        for keeper in self.zoo_keepers:
            print(f"ZooKeeper(name={keeper.name}, surname={keeper.surname}, id={keeper.id})")
        
        print("\nFences:")
        for fence in self.fences:
            if fence.animals:
                print(f"Fence(area={round(fence.area, 3)}, temperature={fence.temperature}, habitat={fence.habitat})")
                print("with animals:")
                for animal in fence.animals:
                    print(f"Animal(name={animal.name}, species={animal.species}, age={animal.age}, height={animal.height:.2f}, width={animal.width:.2f}, health={animal.health:.2f})")
                print("#" * 30)

"""# Define some animals
animal1 = Animal(name="Lion", species="Panthera leo", age=5, height=1.2, width=2.5, preferred_habitat="Savannah")
animal2 = Animal(name="Elephant", species="Loxodonta", age=10, height=3.3, width=6.0, preferred_habitat="Savannah")
animal3 = Animal(name="Penguin", species="Aptenodytes forsteri", age=3, height=0.8, width=1.0, preferred_habitat="Cold")

# Define some fences
fence1 = Fence(area=100.0, temperature=30.0, habitat="Savannah")
fence2 = Fence(area=50.0, temperature=-5.0, habitat="Cold")

# Define a zookeeper
zookeeper = ZooKeeper(name="John", surname="Doe", id="ZK001")

# Define a zoo
zoo = Zoo(fences=[fence1, fence2], zoo_keepers=[zookeeper])

# Describe the initial state of the zoo
print("Initial state of the zoo:")
zoo.describe_zoo()

# Add animals to fences
zookeeper.add_animal(animal1, fence1)
zookeeper.add_animal(animal2, fence1)
zookeeper.add_animal(animal3, fence2)

# Describe the state of the zoo after adding animals
print("\nAfter adding animals:")
zoo.describe_zoo()

# Feed an animal
zookeeper.feed(animal1)
zookeeper.feed(animal2)
zookeeper.feed(animal3)

# Describe the state of the zoo after feeding an animal
print("\nAfter feeding an animal:")
zoo.describe_zoo()

# Remove an animal from a fence
zookeeper.remove_animal(animal2, fence1)

# Describe the state of the zoo after removing an animal
print("\nAfter removing an animal:")
zoo.describe_zoo()

# Clean a fence
print("\nCleaning fence 1:")
clean_area1 = zookeeper.clean(fence1)
print(f"Area cleaned in fence 1: {clean_area1}")

print("\nCleaning fence 2:")
clean_area2 = zookeeper.clean(fence2)
print(f"Area cleaned in fence 2: {clean_area2}")

# Final state of the zoo
print("\nFinal state of the zoo:")
zoo.describe_zoo()"""