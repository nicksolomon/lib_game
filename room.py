import random
import item
import puzzle

class Room:
    def __init__(self, description):
        self.desc = description
        self.monsters = []
        self.characters = []
        self.exits = []
        self.items = []
    def addExit(self, exitName, destination):
        self.exits.append([exitName, destination])
    def getDestination(self, direction):
        for e in self.exits:
            if e[0] == direction:
                return e[1]
    def connectRooms(room1, dir1, room2, dir2):
        #creates "dir1" exit from room1 to room2 and vice versa
        room1.addExit(dir1, room2)
        room2.addExit(dir2, room1)
    def exitNames(self):
        return [x[0] for x in self.exits]
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def addMonster(self, monster):
        self.monsters.append(monster)
    def removeMonster(self, monster):
        self.monsters.remove(monster)
    def addCharacter(self, character):
        self.characters.append(character)
    def removeCharacter(self, character):
        self.characters.remove(character)
    def hasItems(self):
        if self.items != []:
            temp = []
            for item in self.items:
                if item.__class__.__name__ != "Book":
                    temp.append(item)
            return temp != []
        return False
    def hasBook(self):
        # is there a book in here
        for item in self.items:
            if item.__class__.__name__ == "Book":
                return True
        return False
    def getItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False
    def hasMonsters(self):
        return self.monsters + self.characters != []
    def getMonsterByName(self, name):
        for i in self.monsters + self.characters:
            if i.name.lower() == name.lower():
                return i
        return False
    # def randomNeighbor(self):
    #     return random.choice(self.exits)[1]


class Book_room(Room):
    def __init__(self, book, puzzle, description = "There's books in here. Maybe solving the puzzle will get you one you need."):
        Room.__init__(self, description)
        self.book = book
        self.puzzle = puzzle
        self.addItem(self.book)

class Comp_room(Room):
    def __init__(self, book, description = "Maybe this computer can help you find your book."):
        Room.__init__(self, description)
        self.kiosk = item.Kiosk(book)
        self.kiosk.putInRoom(self)

class Study_room(Room):
    def __init__(self, description = "A group study room! Maybe someone in here can help you out."):
        Room.__init__(self, description)

        