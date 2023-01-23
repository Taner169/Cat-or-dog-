import os
import random
import math
import numpy as np
from PIL import Image
from numpy import asarray

# Globala listor där vi lagrar data.
dogs = []
cats = []
mix = []


# Definerar Animal klassen som även innehåller metoder.
class Animal:
    def __init__(self, animal_type, sum_of_pixels):
        self.animal_type = animal_type
        self.sum_of_pixels = sum_of_pixels

    # Klassmetod som konvrterar och lagrar bilder i globala listor.
    @staticmethod
    def convert_and_store_image(image_to_convert, animal):
        image_to_convert = image_to_convert.convert("L")
        image_to_convert = image_to_convert.resize((32, 32))

        if animal == "dog":
            sum_of_dog_pixels = np.sum(asarray(image_to_convert))
            dogs.append(Animal("dog", sum_of_dog_pixels))

        elif animal == "cat":
            sum_of_cat_pixels = np.sum(asarray(image_to_convert))
            cats.append(Animal("cat", sum_of_cat_pixels))

        elif animal == "test_dog":
            sum_of_test_pixels = np.sum(asarray(image_to_convert))
            return Animal("dog", sum_of_test_pixels)

        elif animal == "test_cat":
            sum_of_test_pixels = np.sum(asarray(image_to_convert))
            return Animal("cat", sum_of_test_pixels)

        elif animal == "mix":
            sum_of_mix_pixels = np.sum(asarray(image_to_convert))
            mix.append(Animal("The animal", sum_of_mix_pixels))

    # Genererar en slumpvis hund
    @staticmethod
    def make_random_dog(amount_of_images_to_scan: int):
        for _ in range(amount_of_images_to_scan):
            dog_img = Image.open("dogs/" + random.choice(os.listdir("dogs")))
            return Animal.convert_and_store_image(dog_img, "test_dog")

    # Genererar en slumpvis katt
    @staticmethod
    def make_random_cat(amount_of_images_to_scan: int):
        for _ in range(amount_of_images_to_scan):
            dog_img = Image.open("cats/" + random.choice(os.listdir("cats")))
            return Animal.convert_and_store_image(dog_img, "test_cat")

    # Genererar en slumpvis djur, kan bli antingen hund eller katt.
    @staticmethod
    def make_random_animal():
        state = random.randrange(1, 3)
        if state == 1:
            return Animal.make_random_dog(1)
        elif state == 2:
            return Animal.make_random_cat(1)

    # Genererar djur baserat på mix mappen, kan bli både hund och katter.
    @staticmethod
    def make_mix_animals(amount_to_make: int):
        for _ in range(amount_to_make):
            mix_img = Image.open("mix/" + random.choice(os.listdir("mix")))
            Animal.convert_and_store_image(mix_img, "mix")

    # Genererar specifik mängd hundar.
    @staticmethod
    def make_dog():
        d_space = 0
        while d_space <= 2:
            dog_img = Image.open(f'dogs/dog.{d_space}.jpg')
            Animal.convert_and_store_image(dog_img, "dog")
            d_space += 1

    # Genererar specifik mängd katter.
    @staticmethod
    def make_cat():
        d_space = 0
        while d_space <= 2:
            dog_img = Image.open(f'cats/cat.{d_space}.jpg')
            Animal.convert_and_store_image(dog_img, "dog")
            d_space += 1

    # Funktion som använder euclidean distance
    @staticmethod
    def euclidean_distance(x, y):
        return math.sqrt((float(x) - float(y)) ** 2)


# Kallar funktioner för att generera data.
mix_animal = Animal.make_random_animal()
print(mix_animal.animal_type)
Animal.make_mix_animals(20)


# Funktion som kollar om en bild är hund eller katt.
def check_animals(animals_to_check: list, test_animal):
    for animals in animals_to_check:
        if animals.sum_of_pixels > test_animal.sum_of_pixels:
            print(f"{animals.animal_type} is probably a dog")
        elif animals.sum_of_pixels < test_animal.sum_of_pixels:
            print(f"{animals.animal_type} is probably a cat")
        else:
            print(f"{animals.animal_type} is 100% a {test_animal.animal_type}")


# Kollar datan.
check_animals(mix, mix_animal)
