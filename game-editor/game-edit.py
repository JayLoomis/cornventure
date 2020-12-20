## Game Editor ###############################################################
# This application manages data files for the Cornventure game engine.
##############################################################################

class GameObjectManager:
    def __init__(self, name):
        # Keep track of the maximum value used for an ID, to ensure that no
        #  duplicates arise. If you delete IDs, those numbers will simply not
        #  appear for this game.
        self.name = name
        self.max_id = 0
        self.rooms = []
        self.areas = []
        self.creatures = []
        self.features = []
        self.items = []


    def load_file(self, filename, type, merge):
        pass


    def get_data_info(self):
        data_info = (self.name, self.max_id)
        return data_info

    def add_room(self, name, desc_short, desc_full, exits=[], areas=[],
                 creatures=[], features=[], items=[], attributes=[]):

        # Create a new room dict and add the universal stuff to it.
        new_room = {}
        new_room["id"] = self.max_id + 1
        self.max_id += 1

        new_room["name"] = name
        new_room["desc_short"] = desc_short
        new_room["desc_full"] = desc_full

        new_room["areas"] = areas
        new_room["exits"] = exits
        new_room["creatures"] = creatures
        new_room["features"] = features
        new_room["items"] = items
        new_room["attributes"] = attributes

        # With the new room put together, add it to the list for this game.
        self.rooms.append(new_room)


    def delete_room(self, room_id):
        for i in range(len(self.rooms)):
            if self.rooms[i]["id"] == room_id:
                del self.rooms[i]

        return None


    def get_room(self, room_id):
        for room in self.rooms:
            if room["id"] == room_id:
                return room

        return None


    # Gets an ID by name for a type of data.
    def get_room_by_name(self, name):
        for room in self.rooms:
            if room["name"] == name:
                return room

        return None


    def add_area(self, parent_room, name, desc_short, desc_full, exits=[], areas=[],
                 creatures=[], features=[], items=[], attributes=[]):

        # Create a new area dict and add the universal stuff to it.
        new_area = {}
        new_area["id"] = self.max_id + 1
        self.max_id += 1

        new_area["name"] = name
        new_area["desc_short"] = desc_short
        new_area["desc_full"] = desc_full

        new_area["areas"] = areas
        new_area["exits"] = exits
        new_area["creatures"] = creatures
        new_area["features"] = features
        new_area["items"] = items
        new_area["attributes"] = attributes

        # With the new area put together, add it to the list for this game.
        self.areas.append(new_area)


    def delete_area(self, area_id):
        for i in range(len(self.areas)):
            if self.areas[i]["id"] == area_id:
                del self.areas[i]

        return None


    def get_area(self, area_id):
        for area in self.areas:
            if area["id"] == area_id:
                return area

        return None


    # Gets an ID by name for a type of data.
    def get_area_by_name(self, name):
        for area in self.areas:
            if area["name"] == name:
                return area

        return None


def main():
    rm_name = input("Enter a room name: ")
    rm_desc_s = input("Enter a short description for the room: ")
    rm_desc_f = input("Enter a full description for the room: ")

    gom = GameObjectManager("Dungeons of Drew")

    gom.add_room(rm_name, rm_desc_s, rm_desc_f)

    new_room = gom.get_room_by_name(rm_name)

    # Print out what we've made!
    print("Information about this game data")
    print("--------------------------------")
    data_info = gom.get_data_info()
    print("Name: {}".format(data_info[0]))
    print("Max ID: {}\n".format(data_info[1]))

    print("Room information")
    print("----------------")
    print(new_room["id"])
    print("\tName: {}".format(new_room["name"]))
    print("\tShort description: {}".format(new_room["desc_short"]))
    print("\tFull description: {}".format(new_room["desc_full"]))
    print("\tAreas: ", end="")
    if len(new_room["areas"]) > 0:
        pass
    else:
        print("None defined")

    print("\tExits: ", end="")
    if len(new_room["exits"]) > 0:
        pass
    else:
        print("None defined")

    print("\tCreatures: ", end="")
    if len(new_room["creatures"]) > 0:
        pass
    else:
        print("None defined")

    print("\tFeatures: ", end="")
    if len(new_room["features"]) > 0:
        pass
    else:
        print("None defined")

    print("\tItems: ", end="")
    if len(new_room["items"]) > 0:
        pass
    else:
        print("None defined")

    print("\tAttributes: ", end="")
    if len(new_room["attributes"]) > 0:
        pass
    else:
        print("None defined")




if __name__ == "__main__":
    main()

