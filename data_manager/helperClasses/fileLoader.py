import csv
import os


class InventoryLoader(inventoryFile):

    def __init__(self, inputFile):
        self.inputFile = inputFile

    def open(self):
        with open(self.inputFile, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)


inventoryLoader = InventoryLoader(
    "C:\\Users\\kamano\\Google Drive\\input\\ci_test.txt")
inventoryLoader.open()
